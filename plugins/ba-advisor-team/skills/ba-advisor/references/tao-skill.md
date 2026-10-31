# Tạo skill mới cho việc lặp lại

Đọc khi BA muốn tạo, sửa skill hoặc cần dùng lại một cách làm chuyên môn. Đích đến: hướng dẫn nhỏ theo chuẩn Agent Skills, có đầu vào, ví dụ và cách kiểm để BA khác sử dụng được. Khả năng nạp skill, công cụ và chất lượng đầu ra cần thử trên nền tảng thực dùng.

## Chọn nơi lưu đúng

| Điều BA muốn giữ lại | Nơi phù hợp |
|---|---|
| Quyết định của một việc | `ket-qua/<viec>/` cùng đầu ra |
| Quy ước, mẫu, thuật ngữ, quy tắc của một dự án | `HO-SO-DU-AN.md` (lệnh `ghi nhớ`) |
| Việc làm một lần | Làm trực tiếp |
| Kiểm cơ học: đủ cột, đúng định dạng ID | Checklist hoặc script |
| Quy trình lặp lại cần kiến thức AI chưa có: mẫu riêng, cách làm đã đúc kết, lỗi hay gặp | Skill mới |

Nêu nơi phù hợp kèm lý do; khi BA đã giao tạo hoặc sửa thì làm trong phạm vi đó. Sửa skill có sẵn: đọc toàn bộ skill trước, giữ tên, sửa đúng phần cần đổi. Sửa lỗi ở đầu ra trước; chỉ biến thành hướng dẫn dùng chung khi có nguyên nhân và phạm vi áp dụng rõ.

## Xác định việc cần hỗ trợ

Đọc cuộc trò chuyện và tài liệu BA đã đưa, dùng lại điều đã chốt; chỉ hỏi phần thiếu có thể đổi cách làm:

1. Skill làm việc gì, cho ai. Tách skill khi cách dùng và kiến thức chuyên môn khác nhau; các công đoạn liên quan có thể dùng chung một skill.
2. Ai dùng đầu ra, và họ cần đầu ra đúng điều gì.
3. Những câu BA thường gõ để giao việc này, và những câu gần giống thuộc việc khác.
4. Kiến thức AI chưa có: mẫu, một ví dụ BA đã chấp nhận, những góp ý BA hay phải sửa và điều kiện áp dụng. Ví dụ chưa được chấp nhận thì ghi rõ, chưa dùng làm đáp án chuẩn.
5. Phần nào cần bám nguồn, phần nào được đề xuất; đầu ra kiểm bằng gì.

Trình ngắn phạm vi và tệp cần sửa/tạo. Mode 1 và phạm vi đã rõ thì thực hiện; mode 2/3 dùng điểm chốt tương ứng. Lựa chọn làm thay đổi phạm vi vẫn cần BA quyết định.

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
Q1–Q4 của ba-advisor, kèm bằng chứng riêng của đầu ra.
```

Khung trên là gợi ý. Giữ phần làm thay đổi quyết định hoặc chất lượng đầu ra; chỉ dẫn chung dùng từ advisor, phần chuyên môn ghi cách làm và bằng chứng cần kiểm. Nếu skill cần dùng độc lập, đóng gói đủ phần cần thiết hoặc nêu rõ phụ thuộc phải nạp.

## Chuẩn tối thiểu

- `name`: chữ thường, số, gạch nối, tối đa 64 ký tự, trùng tên thư mục, có tiền tố của team.
- `description`: tối đa 1024 ký tự, có "Dùng khi" và cụm từ BA gõ thật. Description nói khi nào dùng; các bước làm nằm trong thân skill.
- SKILL.md ngắn nhất đủ dùng. Tài liệu chuyên biệt để trong `references/`, ghi rõ khi nào đọc; chất lượng trên mô hình cục bộ phải kiểm riêng.
- Mỗi dòng giữ lại phải giúp AI làm đúng hơn; dòng nói điều AI vốn làm đúng thì bỏ.
- Viết điều cần làm kèm lý do, dạng khẳng định.
- Skill dùng chung chứa cách làm; dữ liệu, tên khách hàng, quyết định riêng nằm trong hồ sơ dự án.
- Thư mục skill chứa tệp AI dùng; hướng dẫn cho người đọc đặt ở README của repo.

## Thử trước khi dùng rộng

Áp dụng khi tạo/sửa skill hoặc đổi mô hình, nền tảng; không thêm bước đo lường vào mọi task BA.

1. Chọn một việc thường gặp và vài trường hợp có thể làm sai: nguồn thiếu/mâu thuẫn, yêu cầu cập nhật, tiếp tục phiên mới. Dùng dữ liệu giả hoặc đã làm sạch; giữ đầu vào, đầu ra đã được BA chấp nhận và điều cần kiểm. Đáp án dùng để đánh giá, tách khỏi phiên thực hiện.
2. Chạy trên cấu hình thực dùng; ghi phiên bản skill/commit, mô hình, công cụ. Muốn so cách cũ và mới thì giữ nguồn, mẫu, yêu cầu và điều kiện tương đương; tránh dùng cùng hội thoại đã biết đáp án. Thử thêm một việc chưa dùng để chỉnh skill và lặp lại trường hợp quan trọng để nhận ra kết quả thiếu ổn định.
3. Đối chiếu Q1–Q4 và kết quả thực: tệp có tồn tại/mở được, phần sửa có đúng, phần phải giữ có còn nguyên; xem cả câu hỏi AI đặt. Thay cách diễn đạt mà giữ nghiệp vụ thì kết quả cần nhất quán; đổi "đề nghị" thành "đã xác nhận" thì trạng thái cần đổi đúng. Thử cả câu gọi gần giống nhưng nằm ngoài phạm vi skill.
4. Nhờ một BA khác thử với hướng dẫn hiện có khi có điều kiện. Ghi lỗi, vị trí và lần cần hỗ trợ; chỉ sửa chỉ dẫn khi xác định vấn đề đến từ skill, thay vì nguồn thiếu, công cụ hoặc môi trường. Có thể rút bỏ quy tắc cũ khi phép thử cho thấy nó không còn cần thiết; chạy lại trường hợp bị ảnh hưởng.
5. Khi đánh giá hiệu quả, ghi tổng thời gian gồm giao việc/kiểm/sửa, lỗi quan trọng còn sót và lần cần người hỗ trợ. Phân biệt thời gian thực đo với ước tính; thiếu bản so sánh thì chưa kết luận tiết kiệm. Ghi phần chưa thử là **Chưa kiểm chứng**. Skill cài được chưa chứng minh nghiệp vụ đúng hoặc hiệu quả trên mọi nền tảng.

Lưu ca thử và kết quả ở khu vực kiểm thử của người quản lý, tách khỏi thư mục skill AI nạp. Repo có thể kèm bộ ca giả lập công khai cho người kiểm; không đưa dữ liệu thật hoặc lịch sử riêng vào đó. Khi BA giao cài, ghi skill vào mục Skill riêng của hồ sơ dự án để advisor tìm đúng; chỉ báo đã cài khi đã thực hiện.

Vị trí cài: Codex và Antigravity dùng `.agents/skills/<ten-skill>/`; Claude Code dùng `.claude/skills/<ten-skill>/`. Mở phiên mới sau khi cài.
