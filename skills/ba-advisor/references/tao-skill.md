# Tạo skill mới cho việc lặp lại

Đọc khi một loại việc lặp lại từ lần thứ ba, hoặc BA muốn tạo, sửa một skill. Đích đến: một skill nhỏ theo chuẩn Agent Skills (agentskills.io), chạy được trên Codex, Claude Code, Antigravity và công cụ cục bộ, để người khác dùng được ngay.

## Chọn nơi lưu đúng

| Điều BA muốn giữ lại | Nơi phù hợp |
|---|---|
| Quyết định của một việc | `ket-qua/<viec>/` cùng đầu ra |
| Quy ước, mẫu, thuật ngữ, quy tắc của một dự án | `HO-SO-DU-AN.md` (lệnh `ghi nhớ`) |
| Việc làm một lần | Làm trực tiếp |
| Kiểm cơ học: đủ cột, đúng định dạng ID | Checklist hoặc script |
| Quy trình lặp lại cần kiến thức AI chưa có: mẫu riêng, cách làm đã đúc kết, lỗi hay gặp | Skill mới |

Nêu nơi phù hợp kèm lý do; BA quyết định. Sửa skill có sẵn: đọc toàn bộ skill trước, giữ tên, sửa đúng phần cần đổi.

## Chốt 5 điều

Đọc cuộc trò chuyện và tài liệu BA đã đưa, rồi hỏi phần còn thiếu, mỗi câu kèm đáp án đề xuất:

1. Skill làm việc gì, cho ai. Hai mục đích là hai skill.
2. Ai dùng đầu ra, và họ cần đầu ra đúng điều gì.
3. Những câu BA thường gõ để giao việc này, và những câu gần giống thuộc việc khác.
4. Kiến thức AI chưa có: mẫu, một ví dụ tốt, những góp ý BA hay phải sửa.
5. Phần nào Đúng ý, phần nào Sáng tạo; đầu ra kiểm bằng gì.

Trình bản tóm tắt: tên, một dòng mục đích, description, danh sách tệp kèm một dòng mô tả. BA đồng ý thì tạo tệp.

## Khung SKILL.md

```markdown
---
name: <tien-to-team>-<viec>
description: "<Làm gì, một câu>. Dùng khi BA nói '<cụm từ 1>', '<cụm từ 2>' hoặc khi <tình huống>."
---

# <Tên skill>

<Vai trò của AI với BA>. <Đầu ra cần có>. <Ai dùng đầu ra và họ cần điều gì>.

## Phạm vi áp dụng
## Nguồn cần đọc
## Khi thiếu thông tin
## Cách làm
## Kiểm trước khi bàn giao
Q1–Q4 của ba-advisor, cộng các câu kiểm riêng của việc này.
```

Bốn mục Phạm vi áp dụng, Nguồn cần đọc, Khi thiếu thông tin, Kiểm trước khi bàn giao là phần chung của mọi skill trong bộ hướng dẫn. Mục Cách làm ghi các bước và những điểm BA từng phải sửa.

## Chuẩn tối thiểu

- `name`: chữ thường, số, gạch nối, tối đa 64 ký tự, trùng tên thư mục, có tiền tố của team.
- `description`: tối đa 1024 ký tự, có "Dùng khi" và cụm từ BA gõ thật. Description nói khi nào dùng; các bước làm nằm trong thân skill.
- SKILL.md ngắn nhất có thể, dưới 500 dòng; mô hình cục bộ làm tốt hơn với chỉ dẫn ngắn. Tài liệu dài để trong `references/`, ghi rõ khi nào đọc, chỉ một cấp.
- Mỗi dòng giữ lại phải giúp AI làm đúng hơn; dòng nói điều AI vốn làm đúng thì bỏ.
- Viết điều cần làm kèm lý do, dạng khẳng định.
- Skill dùng chung chứa cách làm; dữ liệu, tên khách hàng, quyết định riêng nằm trong hồ sơ dự án.
- Thư mục skill chứa tệp AI dùng; hướng dẫn cho người đọc đặt ở README của repo.

## Thử trước khi dùng rộng

1. Chọn 2–3 yêu cầu thật, dùng dữ liệu giả hoặc đã làm sạch. Mỗi yêu cầu chạy trong phiên mới, một lần có skill, một lần chưa có; so hai kết quả bằng Q1–Q4.
2. Viết 6–10 câu gọi: một nửa thuộc skill, một nửa gần giống nhưng thuộc việc khác; kiểm skill được gọi đúng.
3. Thử thêm trên một việc khác với nguồn tối thiểu, giữ đáp án mẫu tách khỏi phiên thử; ghi kết quả quan sát được, phần chưa thử ghi **Chưa kiểm chứng**.
4. Ghi skill vào mục Skill riêng của hồ sơ dự án để ba-advisor chỉ đường tới.

Vị trí cài: Codex và Antigravity dùng `.agents/skills/<ten-skill>/`; Claude Code dùng `.claude/skills/<ten-skill>/`. Mở phiên mới sau khi cài.
