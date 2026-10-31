# Bảo mật dữ liệu dự án

Đọc khi BA hoặc người phụ trách kỹ thuật thiết lập môi trường dùng dữ liệu thật, hoặc khi BA cần làm sạch tài liệu. Skill là tệp chỉ dẫn; người phụ trách kỹ thuật là người thiết lập, kiểm tra và xác nhận môi trường.

## 1. Chọn dữ liệu theo môi trường

| Điều kiện | Dữ liệu được dùng |
|---|---|
| Chưa có xác nhận môi trường | Dữ liệu giả, bản đã làm sạch được đơn vị cho phép, hoặc tư vấn chung |
| Có xác nhận còn hiệu lực cho đúng cấu hình và phạm vi | Dữ liệu dự án thật trong phạm vi đã xác nhận |

Codex, Claude Code, Antigravity, Claude và các ứng dụng khác áp dụng cùng điều kiện này; các ứng dụng mặc định gọi mô hình trên đám mây cần được cấu hình chạy cục bộ và xác nhận trước khi nhận dữ liệu thật.

Môi trường xử lý dữ liệu thật đáp ứng:

- Mô hình và mọi thành phần đọc, OCR, trích xuất, tra cứu, chỉ mục chạy trên cùng máy cục bộ; dịch vụ AI chỉ nhận kết nối từ chính máy đó; kết nối ra ngoài và cơ chế chuyển lên đám mây được chặn.
- Tài liệu, câu lệnh, kết quả, lịch sử, chỉ mục, tệp tạm, nhật ký lưu tại máy có phân quyền; đồng bộ, sao lưu đám mây, gửi chẩn đoán được tắt; dữ liệu dự án chỉ phục vụ công việc, nằm ngoài việc huấn luyện, tinh chỉnh mô hình.
- Người phụ trách kỹ thuật xác nhận bằng bằng chứng kiểm cấu hình, lưu trữ, kết nối, và kiểm lại khi đổi công cụ, mô hình, phiên bản, tiện ích hoặc phạm vi.

## 2. Làm sạch tài liệu

BA làm sạch **trước khi** đưa tài liệu vào môi trường chưa xác nhận, bằng cách đơn vị cho phép, ngay trong môi trường được phép. Rà: nghiệp vụ riêng, thông tin nhận dạng (họ tên, CCCD, mã số thuế, số điện thoại, địa chỉ), khóa, mật khẩu, ảnh chụp, metadata, comment, đường dẫn, liên kết nội bộ. Khi còn phân vân bản đã sạch hay chưa, dùng dữ liệu giả. Việc làm sạch bản gốc diễn ra trong môi trường được phép, tách khỏi AI bên ngoài.

## 3. Checklist kỹ thuật

Thử bằng dữ liệu giả. Đánh dấu khi đã có bằng chứng; xác nhận đúng phạm vi đã kiểm.

| Đã kiểm | Nội dung | Bằng chứng lưu tại máy |
|---|---|---|
| ☐ | Mô hình và các thành phần xử lý chạy cục bộ; dịch vụ chỉ nhận kết nối từ chính máy | Thành phần, phiên bản, nơi chạy, cấu hình lắng nghe |
| ☐ | Lưu trữ có phân quyền; đồng bộ, sao lưu đám mây, chẩn đoán, huấn luyện, tinh chỉnh đã tắt | Vị trí lưu, quyền, cấu hình |
| ☐ | Toàn luồng đọc nguồn → xử lý → tạo kết quả chạy được khi ngắt mạng | Ca thử, kết quả |
| ☐ | Kết nối ra của các thành phần xử lý bị chặn và duy trì chặn khi dùng dữ liệu thật | Quy tắc chặn, phạm vi, kết quả kiểm |
| ☐ | Nhật ký ứng dụng, kết nối và dữ liệu chờ gửi khi mạng trở lại đã được rà bằng nguồn giả | Mốc thời gian, kết nối phát hiện, cách xử lý, vùng chưa quan sát được |
| ☐ | Tiện ích, connector, workflow ngoài (ví dụ BMAD có bước tra cứu web) đã được rà; chọn cách làm chạy cục bộ | Thành phần được dùng, thành phần đã tắt, bước bị giới hạn |
| ☐ | Cấu hình, phạm vi thay đổi đã được kiểm lại trước khi dùng dữ liệu thật | Kết quả kiểm lại, xác nhận mới |

Kết luận dựa trên cả cấu hình, kiểm soát kết nối và nhật ký. Khi bằng chứng còn thiếu, dùng dữ liệu giả, bản đã làm sạch hoặc tư vấn chung.

## 4. Mẫu xác nhận môi trường

Chép vào hồ sơ dự án tại máy có phân quyền để người phụ trách kỹ thuật điền; mục Môi trường AI của `HO-SO-DU-AN.md` dẫn tới bản này.

| Nội dung | Ghi nhận |
|---|---|
| Người phụ trách kỹ thuật, đơn vị | |
| Ngày kiểm tra và xác nhận | |
| Máy, môi trường; công cụ, mô hình, phiên bản, tiện ích | |
| Phạm vi công việc và dữ liệu được phép | |
| Nơi lưu cấu hình và bằng chứng checklist | |
| Kết luận | ☐ Đáp ứng trong phạm vi trên · ☐ Chưa đáp ứng · ☐ Chưa đủ bằng chứng |
| Hạn chế và việc cần xử lý | |
| Chữ ký, xác nhận | |
