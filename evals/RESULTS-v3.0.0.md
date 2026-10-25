# Kiểm chứng v3.0.0

Ngày thực hiện: **25/10/2026**. Nguồn hoàn toàn giả lập. Kết luận: có bằng chứng hoạt động trong các ca dưới đây; **chưa đủ để kết luận hiệu quả trên toàn team hoặc mọi nền tảng**.

## Cách thử

Thực hiện sáu lượt trong các phiên AI độc lập của Codex: bốn ca ban đầu, một lần thử lại ca cập nhật và một biến thể yêu cầu bảng kiểm rõ ràng. Mỗi phiên đọc skill, yêu cầu và đầu vào cần thiết; không được cung cấp rubric, đáp án hay lịch sử thiết kế. Phiên không được cách ly kỹ thuật khỏi toàn bộ máy; giới hạn đọc là chỉ dẫn. Mô hình/cấu hình được kế thừa từ phiên Codex; mã model không được ghi nhận độc lập, nên đây không phải benchmark tái lập đầy đủ.

Người tổng hợp đối chiếu đầu ra với rubric, so tệp trước–sau và kiểm sự tồn tại của tệp. Chưa có BA thứ hai chấm độc lập. Bốn ca đầu chạy bản dự thảo v3 trước khi làm rõ cách trình bảng kiểm; ca 02b chạy lõi cuối cùng. Không gọi một lần thử là bằng chứng ổn định.

## Quan sát thực tế

| Lượt | Kết quả quan sát được | Giới hạn |
|---|---|---|
| 01 — Biên bản | Có nội dung gửi nhóm ngay; giữ Mai/27-10, Bình chưa rõ hạn, loại trùng là đề nghị; hỏi ý nghĩa 5.000 và phạm vi lọc. API được tách thành việc xác nhận nội bộ. | Có thêm câu hỏi ngày đối soát, được trình như câu hỏi chứ không bịa hạn. Chưa có BA thật đánh giá văn phong. |
| 02 — Cập nhật, lần đầu | C.1, SC-01, SC-02 đổi 80 → 120; không áp dụng 200/trim; giữ bản nguồn, A/B, ghi chú 500 và SC-03; báo ảnh hưởng prototype/testcase, API/Figma chưa xác định. | Bàn giao có căn cứ dạng văn nhưng không có bảng Q1–Q4 theo mặc định mong đợi. |
| 03 — Tiếp tục | Đúng XUAT/mode 3/bản 0.2; chỉ soạn nhóm Quyền xuất theo ba cột, dừng chờ; không mang giới hạn 200 của NHAP hoặc 2.000 của bản cũ vào. | Không thử tiếp hội thoại dài hoặc thay model. |
| 04 — Làm rõ | Không bỏ trường; hỏi một câu về bước chậm, nhập lại hay chờ hệ thống; gợi ý có điều kiện. | Chưa có câu trả lời BA để kiểm bước triển khai sau. |
| 02 — thử lại sau sửa câu chỉ dẫn | Nội dung SRS và phạm vi vẫn đúng; tiếp tục không có bảng kiểm. | Hỏi chẩn đoán sau thử cho thấy phiên ưu tiên cấu hình người dùng “không trình checklist khi chưa được yêu cầu”. Đây là xung đột cấu hình, không chứng minh skill tự bảo đảm cách trình bày. |
| 02b — yêu cầu rõ bảng kiểm | Có bốn dòng Q1–Q4 với nguồn/vị trí, nêu phần mềm chưa thử và bản mới chưa duyệt; tệp SRS hoàn chỉnh. | Đây là biến thể có yêu cầu bổ sung, không thay thế kết quả ca 02 ban đầu. |

## Bằng chứng để xem trực tiếp

[SRS-v1.1 được tạo ở lượt 02b](example-output-SRS-v1.1.md) là output giả lập nguyên bản, không chỉnh câu chữ sau thử; nguồn và CR nằm trong [cases.json](cases.json), ca 02. Đối chiếu A/B và SC-03 cho thấy nội dung giữ nguyên từng ký tự; mọi tệp đầu vào của ba lượt cập nhật khớp nguồn ca thử. Đã kiểm cả phần còn lại qua diff: metadata/nguồn và giới hạn Tên vùng là phần thay đổi.

Các trích đoạn từ câu trả lời thực tế:

- Ca 01: “Bình tổng hợp câu hỏi; hạn hoàn thành chưa rõ.”; “Đây mới là đề nghị của An, chưa được chốt.”
- Ca 03: “Những vai trò hoặc nhóm người dùng nào được phép xuất Excel cho đợt đối soát?”; “Tôi chưa làm nhóm Định dạng và chưa lưu tệp.”
- Ca 04: “chưa đủ căn cứ để bỏ trường bắt buộc”; hỏi tình huống chậm ở “nhập/tra cứu, phải nhập lại hay chờ hệ thống”.
- Ca 02b: bảng Q1 dẫn CR-02 → C.1/SC-01/SC-02; Q2 dẫn các dòng 54/67/75 của output; Q3 báo đã so toàn bộ khác biệt; Q4 nêu điều kiện, thời điểm kiểm và biên 120/121. Đã mở output đối chiếu các vị trí này.

Mã SHA256 lõi cuối được thử ở 02b: `0838351c356ad8111eac920a9b95cea2ac2f02aaa1c412041550a816353d3404`.

Mã SHA256 output SRS đính kèm: `1cfe7b8cf067b0745d2204c1f89d3ea3a63794a0c392c705c605e0bff7b979d7`.

## Điều chỉnh có căn cứ sau thử

Làm rõ bàn giao SRS mặc định có bảng Q1–Q4, nhưng phải tôn trọng yêu cầu trình bày của người dùng. README có câu dùng ngay khi team cần hình thức kiểm thống nhất: “Kèm bảng Q1–Q4 và vị trí đối chiếu để tôi kiểm”. Không sửa cấu hình cá nhân hoặc buộc skill ghi đè chỉ dẫn cao hơn. Giữ phần nội dung và cách kiểm đúng; không thêm quy trình bắt buộc khác.

## Kiểm kỹ thuật

- `build` và `check` thành công: tên/description/compatibility, metadata giao diện, mục/cột mẫu SRS, liên kết tệp, mục liên kết trong bản chat, đồng bộ chat và ZIP theo byte.
- **11 phép thử công cụ đóng gói đạt:** gồm tái tạo cùng nội dung, kiểm không ghi, ZIP chỉ có runtime, phát hiện chat/ZIP cũ, tệp runtime lạ, liên kết hỏng, metadata sai, đường dẫn ca thử không an toàn, tách rubric khỏi phiên thực hiện, loại tệp dự án ngoài danh sách khỏi ZIP.
- YAML được kiểm thêm bằng trình đọc Ruby. Trình `quick_validate.py` có sẵn của môi trường không chạy do thiếu PyYAML; không gọi đó là đã đạt. Bộ kiểm riêng chỉ kiểm schema scalar đang dùng, không phải trình phân tích YAML tổng quát.
- So với bản nền v2.2.0: mẫu A/B/C/D, hồ sơ dự án và tài liệu bảo mật giữ nguyên nội dung; tài liệu SRS chỉ đổi câu tham chiếu tới cách cộng tác mới.

## Chưa kiểm chứng

Tốc độ/chi phí so với cách cũ, chất lượng qua nhiều BA, auto-trigger trên từng nền tảng, model cục bộ, chat-only, toàn trình Figma, SRS nhiều màn hình, mode 2 và các biến thể còn lại. Chưa dùng nguồn dự án thật. Cài được và đúng cấu trúc không chứng minh các phần này đã chạy đúng.
