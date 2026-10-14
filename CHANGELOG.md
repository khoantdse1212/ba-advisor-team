# Changelog

Các thay đổi đáng chú ý của BA Advisor Team. Mỗi thay đổi ghi loại góp ý dẫn tới nó: nguồn, cách làm, mẫu hoặc cách kiểm.

## [2.2.0] — 2026-10-14

Một skill `ba-advisor`; mọi yêu cầu đi qua một điểm vào. Hợp nhất bản 1.3.3 với các cải tiến về đầu ra và bối cảnh thực tế.

- **Cách làm:** lõi viết theo vai trò, đầu ra, người nhận; các mục chính theo sáng kiến: Phạm vi áp dụng, Nguồn cần đọc, Khi thiếu thông tin, Kiểm trước khi bàn giao. Toàn bộ chỉ dẫn viết dạng khẳng định.
- **Cách làm:** Đúng ý và sáng tạo: nội dung sáng tạo mang dấu [Đề xuất] và vào tài liệu sau khi BA chọn.
- **Mẫu:** Đầu ra sạch: Nội dung bàn giao (dán thẳng vào tài liệu) và Ghi chú cho BA; lời dặn "không/đừng/chỉ" của BA được áp dụng và vắng mặt trong phần bàn giao.
- **Cách làm:** câu hỏi kèm đáp án đề xuất; việc nhiều bước nêu 2–4 tiêu chí đạt; trả lời câu hỏi của Dev; hướng dẫn BA mới bắt đầu bằng một việc nhỏ; báo đúng thao tác đã làm.
- **Nguồn:** Bối cảnh Việt Nam: văn bản pháp lý, địa giới hành chính 2 cấp từ 01/07/2025, dữ liệu định danh, định dạng ngày số, nguồn dạng tin nhắn, ảnh, bản scan.
- **Nguồn:** điều kiện dữ liệu theo xác nhận môi trường; hướng dẫn làm sạch tài liệu, checklist kỹ thuật, mẫu xác nhận chuyển vào `references/bao-mat-du-lieu.md`.
- **Cách làm:** lệnh nhanh `chốt`, `sửa`, `ghi nhớ`, `kiểm`, `làm tiếp`, `gọn`; bảng nơi lưu (việc, dự án, skill); cấu trúc thư mục dự án `HO-SO-DU-AN.md`, `nguon/`, `ket-qua/<viec>/`.
- **Mẫu:** gộp `ba-srs` vào `references/srs.md`; cập nhật sửa trên bản hiện hành, giữ bản nền phục hồi được; Delta khi BA yêu cầu; thêm luồng, bản mẫu, đối chiếu Figma, nhiều use case, mẫu Word, URD, hệ thống có sẵn, web và di động.
- **Cách kiểm:** câu hỏi Q1–Q4 đúng nguyên văn sáng kiến; định nghĩa Đạt / Cần sửa / Chưa đủ căn cứ, thêm Chưa kiểm chứng; kết quả kiểm ở Ghi chú cho BA hoặc mục kiểm của mẫu dự án; trạng thái theo dự án, mặc định Bản nháp / Chờ rà soát / Đã duyệt.
- Repo: README có bước thiết lập cho công cụ AI (giữ tùy chỉnh, báo cáo thiết lập), thử ngay với biên bản giả lập; `packages/ba-advisor.zip` cho ứng dụng Claude có Skills; `.gitignore` giữ dữ liệu dự án ngoài repo. Demo, ca thử, công cụ đóng gói thuộc bộ công cụ của người quản lý.

## [1.3.3] — 2026-10-14

- Viết gọn chỉ dẫn bằng hành động cụ thể; gom lời nhắc và điều kiện lặp.
- Chuẩn hóa tài liệu bảo mật thành điều kiện sử dụng, checklist và mẫu xác nhận.
- Làm gọn hướng dẫn bắt đầu, tài liệu bảo trì và chú thích demo; đồng bộ bản chat và ZIP.

## [1.3.2] — 2026-10-14

- Bổ sung điều kiện dữ liệu, checklist kỹ thuật và mẫu xác nhận môi trường.
- Thêm `compatibility` cho hai skill và kèm tài liệu bảo mật trong ZIP.

## [1.3.1] — 2026-10-14

- Gộp chỉ dẫn chung và làm rõ cách bàn giao Q1–Q4 theo mẫu dự án.
- Rút lời nhắc trong demo; bổ sung kiểm liên kết và đồng bộ gói.

## [1.3.0] — 2026-10-14

- Gom quy tắc về mode, nguồn, kiểm chất lượng, trạng thái và tiếp tục phiên.
- Rút cấu trúc cố định; ưu tiên mẫu dự án và hồ sơ vừa đủ.
- Tách tài liệu bảo trì; đóng gói theo danh sách tệp xác định.

## [1.2.0] — 2026-10-13

- Thêm lời giao việc thiết lập và hướng dẫn nạp theo nền tảng.
- Bổ sung tổ chức hồ sơ, tiếp tục phiên và tái sử dụng cách làm.
- Tự kiểm Q1–Q4 và sinh đồng bộ core, chat, ZIP.

## [1.1.2] — 2026-09-15

- Phát hành hai skill `ba-advisor` và `ba-srs`; bản chat và demo.
- **Cách làm:** khi nhận việc, AI nói ngắn hiểu việc, đầu ra, cách làm; đưa lựa chọn khi có đánh đổi.
- **Cách kiểm:** nhãn độ chắc chắn cạnh nội dung quan trọng; phân loại góp ý theo nguồn, cách làm, mẫu, cách kiểm.
- Thêm giấy phép MIT.
