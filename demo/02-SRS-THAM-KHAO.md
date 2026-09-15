# Đặc tả tham khảo — UI-02 Tạo vùng

Phiên bản 0.1 · DRAFT · Nguồn SRC-W1: [01-INPUT.md](01-INPUT.md). Đây là mẫu biên soạn để thảo luận Q1–Q4, không phải kết quả một phép thử độc lập hoặc bản nghiệp vụ đã duyệt. Phạm vi chỉ UI-02; UI-01 là điểm vào/ra. OQ về lỗi hệ thống cần chốt trước áp dụng thật.

## A. Mô tả tóm tắt

| Nội dung | Mô tả |
|---|---|
| Mục đích | Cán bộ Quản trị dữ liệu tạo thông tin một vùng để dùng về sau |
| Vai trò | Quản trị dữ liệu; có thao tác tạo theo SRC-W1 §1 |
| Điểm vào | Dữ liệu → Danh mục vùng → Tạo mới |
| Điều kiện bắt đầu | Người dùng đã vào UI-02 từ UI-01; danh mục hiện có được dùng kiểm trùng, không tự xác định cơ chế truy cập |
| Kết quả | Khi lưu hợp lệ tạo một bản ghi, về UI-01 và hiện “Đã tạo vùng”; khi hủy không tạo bản ghi |
| Nguồn | SRC-W1 §1–3; giới hạn ở §4 |

## B. Yêu cầu giao diện

### UI-02 — Tạo vùng

```text
┌───────────────────────────────────────────────┐
│ Dữ liệu > Danh mục vùng > Tạo mới              │
│ TẠO VÙNG                                      │
│                                               │
│ Mã vùng *     [____________________________]  │
│ Tên vùng *    [____________________________]  │
│ Loại vùng *   [Chọn loại vùng             ▾]  │
│                                               │
│                         [ Hủy ]  [ Lưu ]      │
└───────────────────────────────────────────────┘
```

Hình UI-02: mockup Markdown **ĐỀ XUẤT — CHƯA XÁC NHẬN**, bố cục OQ-01. Ba trường và hai nút từ SRC-W1 §1–3; dấu * minh họa trường bắt buộc, vị trí bố cục chưa chốt. “Chọn loại vùng” là placeholder đề xuất, không phải giá trị mặc định hay lựa chọn thứ ba. Không có ảnh UX/Figma trong nguồn.

| Thành phần | Vị trí trên hình | Chức năng | Điều kiện/trạng thái |
|---|---|---|---|
| Đường dẫn | Đầu hình | Thể hiện điểm vào nghiệp vụ | Nhãn menu theo nguồn; bố trí chỉ đề xuất, không suy ra có thể bấm |
| Ba trường | Giữa hình | Nhập/chọn giá trị theo bảng C | Chưa nhập/chọn khi mở; không có giá trị mặc định |
| Hủy | Cuối hình | Trở về UI-01 không lưu | Theo SC-04 |
| Lưu | Cuối hình | Kiểm dữ liệu và xử lý lưu | Theo SC-02/03; không tự đặt trạng thái khóa nút |
| Lỗi từng trường | Không minh họa ở trạng thái trống | Hiển thị khi Lưu lỗi | Theo C; vị trí chính xác OQ-01 |

| Từ | Thao tác | Đích/trạng thái | Dữ liệu |
|---|---|---|---|
| UI-01 | Tạo mới | UI-02 | Ba trường chưa có giá trị |
| UI-02 | Lưu có lỗi | UI-02 + lỗi | Giữ input, không tạo bản ghi |
| UI-02 | Lưu hợp lệ | UI-01 + thông báo | Tạo đúng một bản ghi |
| UI-02 | Hủy | UI-01 | Không tạo bản ghi, không hỏi xác nhận |

Nguồn bảng: SRC-W1 §1–3. URL chưa chốt: OQ-02. Bảng trường ở C, tình huống ở D.

## C. Mô tả trường thông tin

### UI-02 — Tạo vùng

| Trường thông tin | Kiểu điều khiển | Độ dài | Giá trị mặc định | Mô tả trường thông tin & Ràng buộc/điều kiện | Bắt buộc |
|---|---|---|---|---|---|
| Mã vùng | Textbox | 2–10 ký tự | Không có | Nhập A–Z hoặc 0–9; không trim/đổi hoa thường. Khi Lưu, rỗng/sai ký tự/độ dài báo “Mã vùng gồm 2–10 chữ in hoa hoặc chữ số”; trùng toàn danh mục báo “Mã vùng đã tồn tại”. Trùng khác loại vẫn không được tạo: AB12 Hành chính đã có thì AB12 Chuyên đề cũng lỗi. Giữ input, không tạo bản ghi. Nguồn SRC-W1 §2–3 | Có |
| Tên vùng | Textbox | 1–100 ký tự | Không có | Không trim. Khi Lưu, rỗng/toàn khoảng trắng/vượt 100 báo “Tên vùng phải có từ 1 đến 100 ký tự và không chỉ gồm khoảng trắng”; giữ input, không tạo bản ghi. Nguồn SRC-W1 §2 | Có |
| Loại vùng | Dropdown | N/A — danh mục cố định | Không có | Chọn Hành chính hoặc Chuyên đề. Khi Lưu, chưa chọn/ngoài danh mục báo “Vui lòng chọn loại vùng hợp lệ”; giữ input, không tạo bản ghi. Không suy ra độ dài CSDL. Nguồn SRC-W1 §2 | Có |
| Hủy | Nút | N/A — không nhập dữ liệu | N/A — nút | Theo SC-04, SRC-W1 §3 | N/A — thao tác |
| Lưu | Nút | N/A — không nhập dữ liệu | N/A — nút | Kiểm toàn bộ trường theo SC-02/03; nếu nhiều trường lỗi, hiện lỗi liên quan cùng lúc, giữ input và UI-02, không tạo bản ghi. Nguồn SRC-W1 §2–3 | N/A — thao tác |

## D. Các tình huống sử dụng

### SC-01 — Mở tạo vùng

Điều kiện: Quản trị dữ liệu đang ở UI-01. Nguồn SRC-W1 §1–2.

| Đối tượng | Hoạt động | Thông tin đầu vào | Thông tin đầu ra |
|---|---|---|---|
| Quản trị dữ liệu | Chọn Tạo mới | Không nhập dữ liệu mới | Mở UI-02, ba trường chưa có giá trị, không tự chọn loại |

### SC-02 — Lưu hợp lệ

Điều kiện: đang UI-02, dữ liệu thỏa C. Nguồn SRC-W1 §2–3.

| Đối tượng | Hoạt động | Thông tin đầu vào | Thông tin đầu ra |
|---|---|---|---|
| Quản trị dữ liệu | Nhập/chọn ba trường, nhấn Lưu | Ví dụ AB13 chưa tồn tại, tên “Vùng mẫu”, loại Chuyên đề | Kiểm toàn bộ dữ liệu; tạo đúng một bản ghi chứa ba giá trị; về UI-01, thấy bản ghi mới và “Đã tạo vùng” |

### SC-03 — Lưu không hợp lệ

Điều kiện: đang UI-02, ít nhất một giá trị vi phạm C. Nguồn SRC-W1 §2–3.

| Đối tượng | Hoạt động | Thông tin đầu vào | Thông tin đầu ra |
|---|---|---|---|
| Quản trị dữ liệu | Nhấn Lưu | Thiếu/sai dữ liệu theo C, hoặc AB12 loại Chuyên đề khi AB12 Hành chính đã tồn tại | Kiểm tất cả trường; hiện lỗi tương ứng tại từng trường cùng lúc nếu nhiều lỗi; giữ nguyên input và UI-02; không tạo bản ghi. Câu lỗi theo C, không lặp thành bộ quy tắc khác |

### SC-04 — Hủy

Điều kiện: đang UI-02. Nguồn SRC-W1 §3.

| Đối tượng | Hoạt động | Thông tin đầu vào | Thông tin đầu ra |
|---|---|---|---|
| Quản trị dữ liệu | Nhấn Hủy | Dữ liệu đang nhập, nếu có | Về UI-01; không tạo bản ghi, không hỏi xác nhận |

---

Câu hỏi mở: OQ-01 bố cục/placeholder/vị trí lỗi; OQ-02 URL và cơ chế truy cập nếu cần đặc tả; OQ-03 mất kết nối/ghi đồng thời; OQ-04 SLA. Người cần chốt: BA Owner của bài áp dụng thật, chưa có xác nhận. Nguồn SRC-W1 §4. Không gọi tài liệu này là đã đủ triển khai hệ thống thật.

Cách kiểm: Q1 đối chiếu từng rule với SRC-W1 §2–3; Q2 giữ mọi ý nguồn và OQ; Q3 đối chiếu C/Mã vùng với SC-03; Q4 thử hai biên mã 1 và 2 ký tự, tên 100 và 101 ký tự, trùng khác loại và hủy. Đánh giá của người soạn cần BA kiểm chéo, không là bằng chứng cải thiện giữa các BA.
