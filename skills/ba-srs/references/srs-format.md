# Mẫu SRS — v1.1.2

## Chọn mức tài liệu

Mẫu dự án đã chọn có ưu tiên về cấu trúc. Giữ tiêu đề, thứ tự và cột; mục không áp dụng ghi N/A — lý do, chưa biết dùng OQ. Không đổi cấu trúc chỉ vì chuyển mode hoặc cập nhật skill.

Nếu yêu cầu một chức năng/màn hình và không có mẫu khác: metadata ngắn (tên/ID, phiên bản, phạm vi, nguồn, trạng thái) + bốn phần A/B/C/D dưới đây; OQ và kết quả kiểm đặt cạnh phần đặc tả, không là phần chức năng thứ năm. Một màn hình chỉ mô tả điểm vào/ra liên quan, không tự sinh thêm CRUD.

Nếu yêu cầu SRS đầy đủ chưa có mẫu riêng, dùng mười mục:
1. Thông tin tài liệu.
2. Mục tiêu.
3. Phạm vi.
4. Nguồn tham chiếu.
5. Thuật ngữ.
6. Actor và quyền.
7. Đặc tả chức năng — lặp A/B/C/D theo chức năng.
8. Câu hỏi mở và mâu thuẫn.
9. Yêu cầu bổ sung: 9.1 Tích hợp/API, 9.2 NFR, 9.3 Xử lý nền/dữ liệu/ràng buộc khác.
10. Kết quả rà soát theo Q1–Q4.

Phần toàn tài liệu dùng thông tin thật; không tự tạo SLA/NFR/actor. Metadata nguồn ghi SRC-ID, tệp/mục/phiên bản/ngày, trạng thái/thẩm quyền/người xác nhận thực có. Thiếu URD không cần tạo URD trung gian. Không gọi mẫu này là mẫu chính thức chung VNPT.

## A. Mô tả tóm tắt

Giữ các dòng của mẫu dưới đây. Viết kết quả ở mức tóm tắt; không lặp đầy đủ thông báo/nhánh xử lý sẽ đặc tả ở B/D.

| Nội dung | Mô tả |
|---|---|
| Mục đích | Ai đạt kết quả gì |
| Đối tượng sử dụng | Vai trò/quyền theo nguồn |
| Điểm vào | Menu/breadcrumb, màn hình trước |
| Điều kiện bắt đầu | Dữ liệu/trạng thái cần có; không tự thêm cơ chế đăng nhập |
| Kết quả | Dữ liệu và phản hồi quan sát được |
| Nguồn | SRC-ID/vị trí |

## B. Yêu cầu giao diện

Liệt kê màn hình thuộc phạm vi trước; lặp B.n — UI-ID/tên cho từng màn hình.

Mỗi màn hình gồm:
- Ưu tiên nguồn UI đúng phạm vi/phiên bản: UX → Figma/ảnh được cung cấp → mockup Markdown có nhãn đề xuất.
- **Hình/khung:** ảnh thực đã xem hoặc mockup Markdown được hiển thị, không chỉ đường dẫn trống.
- **Chú thích:** hình thể hiện gì; tên/phiên bản/frame nguồn; nếu dựng mới ghi “ĐỀ XUẤT — CHƯA XÁC NHẬN”. Chú thích chung không tự xác nhận các thành phần không có nguồn.
- **Thành phần:** vị trí/nhãn trong hình, chức năng, điều kiện hiển thị thật có. Trạng thái rỗng/tải/lỗi chỉ mô tả khi liên quan; chưa rõ thành OQ.
- **Đường đi:** menu/breadcrumb mong muốn; route có nguồn hoặc OQ; thao tác đi tới đâu, giữ/đổi dữ liệu gì. Dẫn SC-ID tương ứng.

| Thành phần/nhãn | Vị trí trong hình | Chức năng | Điều kiện/trạng thái |
|---|---|---|---|

| Từ màn hình | Thao tác/điều kiện | Đích/trạng thái | Dữ liệu giữ/đổi |
|---|---|---|---|

Điểm B kết nối với bảng trường cùng UI-ID ở C. Không giấu bảng trường bên trong B. Nếu task API/job thật sự không có UI, giữ mục và ghi N/A có căn cứ, không vẽ giả.

## C. Mô tả trường thông tin

Lặp C.n — UI-ID/tên, một bảng riêng mỗi màn hình. Trường xuất hiện ở nhiều màn hình vẫn nêu trạng thái nhập/đọc và dẫn rule chủ, không gộp tất cả màn hình vào một bảng.

| Trường thông tin | Kiểu điều khiển | Độ dài | Giá trị mặc định | Mô tả trường thông tin & Ràng buộc/điều kiện | Bắt buộc |
|---|---|---|---|---|---|

- Mỗi trường/cột dữ liệu có dòng, nút có dòng khi cần đặc tả. Kiểu điều khiển là textbox/dropdown/label…, không thay bằng kiểu CSDL.
- Độ dài nêu min/max và đơn vị thực; giá trị mặc định phân biệt “không có” theo nguồn với “chưa rõ”. Bắt buộc: Có/Không/Có khi…/N/A cho chỉ hiển thị; không dùng dấu gạch mơ hồ.
- Cột mô tả giữ ý nghĩa, nguồn giá trị, đọc/sửa, dữ liệu/format/rule nhập, điều kiện kiểm và kết quả/thông báo; lồng Data Validation và AC dữ liệu tại đây. Chưa có thông báo/thời điểm kiểm thì OQ, không viết “validate hợp lệ” để che thiếu.
- Không tự trim, đổi hoa/thường, làm tròn, thêm trường audit/default, min/max, regex hoặc nguồn danh mục. Giữ quy tắc rỗng, duy nhất và phụ thuộc trường thật có; dẫn SRC-ID/vị trí sát mệnh đề.
- Rule xuyên trường có một vị trí chủ; nơi khác dẫn lại. Quyết định trạng thái/luồng nghiệp vụ nằm ở D, không nhét cả workflow vào một ô.

## D. Các tình huống sử dụng

Mỗi SC-ID có tên/mục tiêu, điều kiện bắt đầu, nguồn và bảng bốn cột. Mô tả luồng chính, thay thế, lỗi có liên quan từ nguồn; còn thiếu thì OQ, không ép số lượng tình huống cố định.

| Đối tượng | Hoạt động | Thông tin đầu vào | Thông tin đầu ra |
|---|---|---|---|

Với UI, mỗi dòng là thao tác người dùng; xử lý/phản hồi hệ thống nằm trong ô Đầu ra của dòng đó. Chỉ tách actor hệ thống khi sự kiện nền độc lập có căn cứ. Nêu điều kiện nhánh, dữ liệu/trạng thái trước/sau, đích màn hình và phản hồi quan sát được. Lồng rule/AC về Business Logic, UX và phản hồi ở Đầu ra; lỗi dữ liệu dẫn C/UI/trường, không sao chép nhiều bộ validation dễ lệch.

## Cập nhật / SRS Delta

Giữ sáu mục: (1) Thông tin thay đổi và bản nền; (2) Bảng hiện tại/đề xuất/lý do/nguồn; (3) Đặc tả sau thay đổi — chỉ A/B/C/D liên quan theo thứ tự, dẫn bản nền phần không đổi; (4) Change Impact; (5) OQ/CF; (6) Kiểm tra Q1–Q4. Cách viết gọn từng mục ở [change-review.md](change-review.md). “Không đổi” không là N/A nghiệp vụ. Hợp nhất bản mới chỉ khi được yêu cầu, giữ bản nền và nguồn phê duyệt.
