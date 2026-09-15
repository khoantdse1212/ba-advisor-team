---
name: ba-srs
description: Tạo, cập nhật, rà soát SRS hoặc đặc tả một chức năng/màn hình từ nguồn BA; giữ mẫu và bốn phần tóm tắt, giao diện, trường, tình huống. Dùng trực tiếp cho việc SRS, không điều phối lại task BA chung, không tự sửa Figma hay triển khai phần mềm.
---

# BA SRS — v1.1.2

Đọc [BA-CORE](references/ba-core.md) và [mẫu đặc tả](references/srs-format.md). Khi cập nhật/rà soát, đọc thêm [change-review.md](references/change-review.md). Dùng lại việc advisor đã tiếp nhận; không mở vòng setup hoặc bộ kiểm khác.

## Chọn đầu ra

- **Tạo:** nhận PRD, biên bản, mô tả trực tiếp và nguồn UI đọc được; không bắt URD hay PROJECT_CONTEXT.md.
- **Cập nhật:** cần bản nền/phiên bản và thay đổi; mặc định Delta theo mẫu, chỉ hợp nhất khi được giao. Cách rút gọn và kiểm ảnh hưởng nằm ở change-review.
- **Rà soát:** trả phát hiện và kết luận theo BA-CORE; thiếu nguồn thì giới hạn đúng phần có thể kiểm, không tự sửa bản nền.
- **Một chức năng/màn hình:** đặc tả A/B/C/D với metadata/nguồn/OQ/kiểm tra gọn; không mở rộng thành toàn dự án hay tự sinh CRUD.
- **SRS đầy đủ:** giữ mẫu dự án đã chọn; chưa có mẫu thì dùng khung đầy đủ trong srs-format. Xung đột mẫu cần BA chốt cách ánh xạ trước khi đổi.

## Nhịp soạn SRS

Mode 1/2 theo BA-CORE, không thêm bốn vòng chốt. Mode 3 soạn lần lượt A → B → C → D; các màn hình có phần riêng trong cùng công đoạn. Chốt D cho phép hợp nhất/rà cuối trong phạm vi. Update/Review một mục không quay lại A.

Nháp chat có thể tóm tắt nhưng bản bàn giao phải đủ từng màn hình, hình/chú thích, từng trường và tình huống theo mẫu; chi tiết chưa cho BA xem không được gọi là đã chốt. Thiếu hành vi cốt lõi phải hỏi trước phần phụ thuộc, không che bằng OQ để kết luận đã đủ dùng.

Mẫu quy định vị trí rule/AC và nguồn: dữ liệu ở C, xử lý/UX ở D; một rule có vị trí chủ, nơi khác dẫn lại. Tự kiểm, trạng thái và ghi chú tiếp tục theo BA-CORE; không tự sửa Figma/API/test/context ngoài việc được giao.
