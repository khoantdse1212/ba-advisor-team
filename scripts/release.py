#!/usr/bin/env python3
"""Build/check public distributions or prepare fictional trials; Python stdlib only."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = Path('skills/ba-advisor')
RUNTIME = (
    'SKILL.md', 'agents/openai.yaml', 'assets/HO-SO-DU-AN.md',
    'references/cong-viec-ba.md', 'references/srs.md',
    'references/tao-skill.md', 'references/bao-mat-du-lieu.md',
)
PUBLIC = (
    'README.md', 'CHANGELOG.md', 'LICENSE', '.gitignore',
    'ba-advisor-team-overview.png', 'ba-advisor-team-overview-v2.2.0.png',
    'evals/README.md', 'evals/cases.json', 'evals/RUBRIC.md',
    'evals/RESULTS-v3.0.0.md', 'evals/example-output-SRS-v1.1.md',
    'scripts/release.py', 'tests/test_release.py',
)
CHAT = ('chat/BA-ADVISOR-CHAT.md', 'chat/BA-SRS-CHAT.md')
LINK = re.compile(r'\[[^\]\n]*\]\(([^)\n]+)\)')


def read(root, name):
    path = root / name
    if path.is_symlink():
        raise ValueError(f'Symlink không được đóng gói: {name}')
    return path.read_text(encoding='utf-8')


def metadata(text):
    """Parse this repo's deliberately simple YAML scalar frontmatter, not arbitrary YAML."""
    match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not match:
        raise ValueError('Thiếu frontmatter')
    data = {}
    for line in match[1].splitlines():
        key, sep, value = line.partition(':')
        if not sep or key in data:
            raise ValueError('Frontmatter không đúng cấu trúc scalar của repo')
        value = value.strip()
        data[key] = json.loads(value) if value.startswith('"') else value
    return data, text[match.end():].lstrip()


def version(root):
    body = metadata(read(root, SKILL / 'SKILL.md'))[1]
    match = re.search(r'^# BA Advisor — v(\d+\.\d+\.\d+)\s*$', body, re.M)
    if not match:
        raise ValueError('Thiếu phiên bản trong SKILL.md')
    return match[1]


def chat_bytes(root, srs=False):
    parts = ['SKILL.md', 'references/cong-viec-ba.md',
             'references/srs.md' if srs else 'references/tao-skill.md',
             'references/bao-mat-du-lieu.md', 'assets/HO-SO-DU-AN.md']
    anchors = {p: 'section-' + str(i) for i, p in enumerate(parts)}
    title = 'BA SRS' if srs else 'BA Advisor'
    intro = (
        f'# {title} — bản chat v{version(root)}\n\n'
        'Bản sinh tự động từ cùng nguồn với skill; không sửa trực tiếp. '
        'Gửi tệp này đầu phiên và yêu cầu AI dùng như hướng dẫn cho việc được giao. '
        'Chỉ nạp một bản chat; không cần nạp cả bản Advisor và SRS.\n\n'
        'Các phần đã gộp ở dưới. Nếu công việc cần tài liệu chỉ có ở liên kết ngoài tệp, '
        'xin người dùng gửi tệp tương ứng, không giả đã đọc hoặc tự tải dữ liệu dự án. '
        'Ví dụ/hồ sơ mẫu không phải nghiệp vụ đã xác nhận. Không có quyền đọc/ghi tệp '
        'thì trao đổi trong chat và nói rõ việc người dùng cần lưu lại.\n\n'
    )
    chunks = []
    for part in parts:
        text = read(root, SKILL / part)
        if part == 'SKILL.md':
            text = metadata(text)[1]
        def replace(match):
            target = match[1]
            if target in RUNTIME:
                dest = '#' + anchors[target] if target in anchors else '../skills/ba-advisor/' + target
                return match[0].replace('(' + target + ')', '(' + dest + ')')
            return match[0]
        text = LINK.sub(replace, text)
        chunks.append(f'<a id="{anchors[part]}"></a>\n\n{text.rstrip()}\n')
    return (intro + '\n---\n\n'.join(chunks)).encode('utf-8')


def zip_bytes(files):
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_STORED) as archive:
        for name, data in sorted(files.items()):
            if name.startswith('/') or '..' in Path(name).parts:
                raise ValueError('Tên tệp ZIP không an toàn')
            item = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
            item.create_system = 3
            item.external_attr = 0o100644 << 16
            archive.writestr(item, data)
    return output.getvalue()


def runtime_files(root):
    expected = set(RUNTIME)
    actual = {p.relative_to(root / SKILL).as_posix() for p in (root / SKILL).rglob('*') if p.is_file()}
    if actual != expected:
        raise ValueError(f'Tệp runtime khác danh sách cho phép: {sorted(actual ^ expected)}')
    return {'ba-advisor/' + p: read(root, SKILL / p).encode('utf-8') for p in RUNTIME}


def generated(root):
    outputs = {CHAT[0]: chat_bytes(root), CHAT[1]: chat_bytes(root, True),
               'packages/ba-advisor.zip': zip_bytes(runtime_files(root))}
    for name in CHAT:
        text = outputs[name].decode('utf-8')
        anchors = set(re.findall(r'<a id="([^"]+)"', text))
        for match in LINK.finditer(text):
            target = match[1]
            if target.startswith('#'):
                if target[1:] not in anchors:
                    raise ValueError('Mục trong bản chat không tồn tại: ' + target)
            elif '://' not in target and not (root / name).parent.joinpath(target).is_file():
                raise ValueError('Liên kết bản chat hỏng: ' + target)
    return outputs


def case_data(root):
    data = json.loads(read(root, 'evals/cases.json'))
    ids = [case['id'] for case in data['cases']]
    if data['schema'] != 1 or len(ids) != len(set(ids)):
        raise ValueError('Danh sách ca thử không hợp lệ')
    for case in data['cases']:
        if not case['prompt'] or not case['files']:
            raise ValueError('Ca thử thiếu đầu vào')
        for name in case['files']:
            if Path(name).is_absolute() or '..' in Path(name).parts or '\\' in name:
                raise ValueError('Đường dẫn ca thử không an toàn')
    return data


def validate_sources(root):
    runtime_files(root)
    data, body = metadata(read(root, SKILL / 'SKILL.md'))
    if data.get('name') != 'ba-advisor' or not 1 <= len(data.get('description', '')) <= 1024:
        raise ValueError('Tên/mô tả skill không hợp lệ')
    if not data.get('compatibility'):
        raise ValueError('Thiếu điều kiện môi trường')
    v = version(root)
    if f'## [{v}]' not in read(root, 'CHANGELOG.md') or f'v{v}' not in read(root, 'README.md'):
        raise ValueError('Phiên bản chưa khớp README/CHANGELOG')
    ui = read(root, SKILL / 'agents/openai.yaml')
    values = dict(re.findall(r'^  (\w+): (".*")$', ui, re.M))
    short = json.loads(values['short_description'])
    if not 25 <= len(short) <= 64 or '$ba-advisor' not in json.loads(values['default_prompt']):
        raise ValueError('Metadata giao diện chưa đúng')
    srs = read(root, SKILL / 'references/srs.md')
    for heading in ('A. Mô tả tóm tắt', 'B. Yêu cầu giao diện', 'C. Mô tả trường thông tin', 'D. Các tình huống sử dụng'):
        if '## ' + heading not in srs:
            raise ValueError('Thiếu phần mẫu SRS: ' + heading)
    if '| Trường thông tin | Kiểu điều khiển | Độ dài | Giá trị mặc định | Mô tả trường thông tin & Ràng buộc/điều kiện | Bắt buộc |' not in srs:
        raise ValueError('Cột mẫu trường SRS đã đổi')
    if '| Đối tượng | Hoạt động | Thông tin đầu vào | Thông tin đầu ra |' not in srs:
        raise ValueError('Cột tình huống SRS đã đổi')
    case_data(root)
    for name in (*PUBLIC, *(str(SKILL / p) for p in RUNTIME)):
        path = root / name
        if not path.is_file() or path.is_symlink():
            raise ValueError('Thiếu tệp công khai hoặc symlink: ' + name)
        if path.suffix not in ('.md', '.json', '.yaml'):
            continue
        text = read(root, name)
        if re.search(r'(?:/Users/|/home/|gh[pousr]_[A-Za-z0-9]{20,})', text):
            raise ValueError('Cần rà đường dẫn riêng/chuỗi giống token: ' + name)
        if path.suffix == '.md':
            for match in LINK.finditer(text):
                link = match[1].split('#')[0]
                if not link or '://' in link or link.startswith('mailto:'):
                    continue
                if not (path.parent / link).is_file():
                    raise ValueError(f'Liên kết tệp hỏng: {name} → {link}')


def full_files(root, outputs):
    files = {p: (root / p).read_bytes() for p in PUBLIC}
    files.update({str(SKILL / p): read(root, SKILL / p).encode('utf-8') for p in RUNTIME})
    files.update(outputs)
    return {f'ba-advisor-team-v{version(root)}/{p}': data for p, data in files.items()}


def build(root, check=False):
    validate_sources(root)
    outputs = generated(root)
    for name, expected in outputs.items():
        path = root / name
        if path.is_symlink():
            raise ValueError('Không ghi vào symlink: ' + name)
        if check:
            if not path.is_file() or path.read_bytes() != expected:
                raise ValueError('Bản sinh chưa đồng bộ: ' + name)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(expected)
    archive = zip_bytes(full_files(root, outputs))
    filename = f'ba-advisor-team-v{version(root)}.zip'
    dist = root / 'dist'
    if check:
        if (dist / filename).exists() and (dist / filename).read_bytes() != archive:
            raise ValueError('Bộ đầy đủ trong dist đã cũ')
    else:
        dist.mkdir(exist_ok=True)
        (dist / filename).write_bytes(archive)
        (dist / 'ba-advisor.zip').write_bytes(outputs['packages/ba-advisor.zip'])
        hashes = ''.join(f'{hashlib.sha256(data).hexdigest()}  {name}\n' for name, data in
                         ((filename, archive), ('ba-advisor.zip', outputs['packages/ba-advisor.zip'])))
        (dist / 'SHA256SUMS.txt').write_text(hashes, encoding='utf-8')
    print(f'OK v{version(root)}: nguồn, mẫu SRS, metadata, liên kết tệp, chat và ZIP. Chưa phải kiểm hành vi AI.')


def prepare(root, case_id):
    cases = {c['id']: c for c in case_data(root)['cases']}
    if case_id not in cases:
        raise ValueError('Chọn ca: ' + ', '.join(cases))
    runtime_files(root)
    dest = Path(tempfile.mkdtemp(prefix='ba-advisor-trial-'))
    for name in RUNTIME:
        target = dest / 'skill/ba-advisor' / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / SKILL / name, target)
    case = cases[case_id]
    for name, text in case['files'].items():
        path = dest / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
    (dest / 'TASK.md').write_text(case['prompt'] + '\n', encoding='utf-8')
    print(dest)
    return dest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('build', 'check', 'prepare'))
    parser.add_argument('case', nargs='?')
    args = parser.parse_args()
    try:
        if args.action == 'prepare':
            prepare(ROOT, args.case)
        else:
            build(ROOT, check=args.action == 'check')
    except (ValueError, OSError, KeyError) as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
