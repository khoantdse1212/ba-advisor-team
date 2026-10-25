"""Distribution invariants, not LLM behavior scores."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('release', ROOT / 'scripts/release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        files = list(release.PUBLIC) + [str(release.SKILL / p) for p in release.RUNTIME] + list(release.CHAT) + ['packages/ba-advisor.zip']
        for name in files:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)

    def tearDown(self):
        self.tmp.cleanup()

    def build(self, check=False):
        with contextlib.redirect_stdout(io.StringIO()):
            release.build(self.root, check)

    def test_build_is_reproducible_and_check_read_only(self):
        self.build()
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.build(check=True)
        self.build()
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)

    def test_runtime_zip_has_only_exact_runtime_sources(self):
        self.build()
        with zipfile.ZipFile(self.root / 'packages/ba-advisor.zip') as archive:
            expected = release.runtime_files(self.root)
            self.assertEqual(set(archive.namelist()), set(expected))
            for name, data in expected.items():
                self.assertEqual(archive.read(name), data)

    def test_stale_chat_detected(self):
        self.build()
        (self.root / release.CHAT[0]).write_text('stale', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'chưa đồng bộ'):
            self.build(check=True)

    def test_unexpected_runtime_file_rejected(self):
        (self.root / release.SKILL / 'private.md').write_text('test', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'danh sách cho phép'):
            self.build()

    def test_unlisted_project_file_not_in_full_zip(self):
        (self.root / 'project-private.txt').write_text('fiction', encoding='utf-8')
        self.build()
        archive_path = self.root / 'dist' / f'ba-advisor-team-v{release.version(self.root)}.zip'
        with zipfile.ZipFile(archive_path) as archive:
            self.assertFalse(any('project-private' in p for p in archive.namelist()))

    def test_broken_link_rejected(self):
        path = self.root / 'README.md'
        path.write_text(path.read_text(encoding='utf-8') + '\n[bad](missing.md)\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Liên kết tệp hỏng'):
            self.build()

    def test_unsafe_fixture_path_rejected(self):
        path = self.root / 'evals/cases.json'
        cases = json.loads(path.read_text(encoding='utf-8'))
        cases['cases'][0]['files']['../escape.md'] = 'test'
        path.write_text(json.dumps(cases), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'không an toàn'):
            release.case_data(self.root)

    def test_prepare_excludes_reviewer_and_results(self):
        with contextlib.redirect_stdout(io.StringIO()):
            dest = release.prepare(self.root, '01-bien-ban')
        try:
            files = {p.relative_to(dest).as_posix() for p in dest.rglob('*') if p.is_file()}
            expected = {'TASK.md', 'bien-ban.md'} | {'skill/ba-advisor/' + p for p in release.RUNTIME}
            self.assertEqual(files, expected)
        finally:
            shutil.rmtree(dest)

    def test_bad_metadata_rejected(self):
        path = self.root / release.SKILL / 'agents/openai.yaml'
        path.write_text(path.read_text(encoding='utf-8').replace('$ba-advisor', 'advisor'), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Metadata'):
            self.build()

    def test_stale_zip_detected(self):
        self.build()
        (self.root / 'packages/ba-advisor.zip').write_bytes(b'old package')
        with self.assertRaisesRegex(ValueError, 'chưa đồng bộ'):
            self.build(check=True)

    def test_generated_chat_has_embedded_security_and_no_missing_anchors(self):
        for name, data in release.generated(self.root).items():
            if name.endswith('.md'):
                text = data.decode('utf-8')
                self.assertIn('# Bảo mật dữ liệu dự án', text)
                self.assertNotIn('(references/', text)


if __name__ == '__main__':
    unittest.main()
