# SRC-W1 — Màn hình Tạo vùng

Dữ liệu giả lập cho buổi chia sẻ BA, phiên bản 1.0, ngày 12/09/2026; không phải nghiệp vụ dự án thật hoặc mẫu bắt buộc của VNPT. Các mục dưới là nguồn duy nhất của ca demo. BA tham gia đóng vai người rà soát, không có phê duyệt tổ chức thật.

## 1. Mục tiêu và phạm vi

Cán bộ Quản trị dữ liệu tạo một vùng trong danh mục để sử dụng về sau. Chỉ đặc tả màn hình UI-02 — Tạo vùng; không cần setup Project Context. UI-01 — Danh mục vùng chỉ là điểm vào/ra, không đặc tả toàn màn hình danh sách. Không có polygon, import, sửa/xóa, tích hợp API hay job nền trong demo. Chưa có UX/Figma; được dùng mockup Markdown đề xuất.

Điểm vào: Dữ liệu → Danh mục vùng → Tạo mới. UI-02 có Mã vùng, Tên vùng, Loại vùng; hai nút Lưu, Hủy. Không có field Trạng thái. Chưa chốt URL hoặc cơ chế đăng nhập; không tự thêm.

## 2. Trường và validation

| Trường | Quy định |
|---|---|
| Mã vùng | Textbox, bắt buộc, 2–10 ký tự A–Z hoặc 0–9, không mặc định. Không trim, không đổi hoa/thường. Duy nhất toàn danh mục, kể cả khác Loại vùng |
| Tên vùng | Textbox, bắt buộc, 1–100 ký tự, không mặc định, không trim. Rỗng hoặc toàn khoảng trắng không hợp lệ |
| Loại vùng | Dropdown, bắt buộc chọn Hành chính hoặc Chuyên đề, không mặc định, không nhận ngoài danh mục. Độ dài: N/A vì không nhập text tự do, chưa đặc tả độ dài CSDL |

Kiểm tất cả trường khi nhấn Lưu; nhiều trường lỗi thì hiển thị từng lỗi cùng lúc tại trường liên quan. Giữ nguyên dữ liệu và UI-02, không tạo bản ghi nếu có lỗi.
- Mã rỗng/sai độ dài/sai ký tự: “Mã vùng gồm 2–10 chữ in hoa hoặc chữ số”.
- Mã trùng: “Mã vùng đã tồn tại”.
- Tên không hợp lệ: “Tên vùng phải có từ 1 đến 100 ký tự và không chỉ gồm khoảng trắng”.
- Loại chưa chọn/ngoài danh mục: “Vui lòng chọn loại vùng hợp lệ”.

## 3. Thao tác và kết quả

Lưu hợp lệ: tạo đúng một bản ghi chứa ba giá trị; về UI-01, thấy bản ghi mới và thông báo “Đã tạo vùng”. Hủy: về UI-01, không tạo bản ghi, không hỏi xác nhận. Không có bước duyệt bản ghi.

Đã có Mã AB12, Loại Hành chính trong dữ liệu giả lập. Tạo AB12 loại Chuyên đề vẫn bị lỗi trùng. Đây là điểm dễ bỏ sót, phải thể hiện trong đặc tả dù không có BR-ID.

## 4. Chưa chốt

Bố cục ảnh/mockup, URL, vị trí lỗi chính xác (trên/dưới trường), xử lý mất kết nối/ghi đồng thời và SLA chưa được quyết định. Ghi rõ giới hạn; bản demo không phải đặc tả sẵn sàng triển khai ngoài phạm vi giả lập.
