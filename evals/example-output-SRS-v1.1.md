# SRS — Tạo vùng

Phiên bản: 1.1. Trạng thái: Bản nháp. Chưa được duyệt; CR-02 xác nhận thay đổi nghiệp vụ, không duyệt trước bản SRS sửa.
Lịch sử duyệt: bản 1.0 — Đã duyệt. Người duyệt: Lan (PO), 20/10/2026, toàn bộ bản 1.0, xác nhận giả lập SRC-D1.
Nguồn nghiệp vụ: SRC-D1 — nội dung bản 1.0 được PO xác nhận trong ca giả lập; CR-02.md — Lan (PO) xác nhận giả lập ngày 22/10/2026, thay giới hạn Tên vùng 80 ký tự bằng 120 ký tự và thông báo tương ứng. Các điều kiện khác giữ nguyên SRC-D1.

## A. Mô tả tóm tắt

| Nội dung | Mô tả |
|---|---|
| Mục đích | Quản trị viên tạo vùng để lập danh mục |
| Đối tượng | Quản trị viên |
| Điểm vào | Danh mục → Vùng → Thêm mới |
| Điều kiện | Đã đăng nhập với quyền quản trị |
| Kết quả | Lưu vùng và trở lại danh sách |
| Nguồn | SRC-D1 |

## B. Yêu cầu giao diện

### B.1 — UI-01: Thêm vùng

Hình UI-01 — mockup đã được xác nhận cùng SRC-D1, không phải ảnh hệ thống chạy thật.

```text
+--------------------------+
| Thêm vùng                |
| Tên vùng * [           ] |
| Ghi chú    [           ] |
| [Hủy]             [Lưu]  |
+--------------------------+
```

| Thành phần/nhãn | Vị trí trong hình | Chức năng | Điều kiện/trạng thái |
|---|---|---|---|
| Tên vùng | Dòng 2 | Nhập tên | Bắt buộc |
| Ghi chú | Dòng 3 | Nhập ghi chú | Không bắt buộc |
| Hủy | Cuối trái | Về danh sách | SC-03 |
| Lưu | Cuối phải | Lưu vùng | SC-01, SC-02 |

| Từ màn hình | Thao tác/điều kiện | Đích/trạng thái | Dữ liệu giữ/đổi |
|---|---|---|---|
| Danh sách | Thêm mới | UI-01 | Form rỗng |
| UI-01 | Lưu hợp lệ — SC-01 | Danh sách | Thêm vùng |
| UI-01 | Hủy — SC-03 | Danh sách | Bỏ dữ liệu đang nhập |

## C. Mô tả trường thông tin

### C.1 — UI-01

Nguồn cho toàn bộ bảng: SRC-D1; riêng giới hạn 120 ký tự và thông báo vượt độ dài của Tên vùng áp dụng CR-02.md, phần Lan (PO) xác nhận ngày 22/10/2026.

| Trường thông tin | Kiểu điều khiển | Độ dài | Giá trị mặc định | Mô tả trường thông tin & Ràng buộc/điều kiện | Bắt buộc |
|---|---|---|---|---|---|
| Tên vùng | Textbox | 1–120 ký tự | Rỗng | Giữ nguyên khoảng trắng; kiểm khi bấm Lưu. Rỗng: “Nhập tên vùng”. Vượt 120 ký tự: “Tên vùng tối đa 120 ký tự”. Không đổi hoa/thường. | Có |
| Ghi chú | Textarea | Tối đa 500 ký tự | Rỗng | Giữ nguyên nội dung; khi Lưu vượt 500 ký tự: “Ghi chú tối đa 500 ký tự”. | Không |

## D. Các tình huống sử dụng

Nguồn cho SC-01, SC-02, SC-03: SRC-D1; riêng giới hạn Tên vùng trong SC-01, SC-02 áp dụng CR-02.md, phần Lan (PO) xác nhận ngày 22/10/2026, theo C.1.

### SC-01 — Lưu hợp lệ

Điều kiện: quản trị viên đang ở UI-01.

| Đối tượng | Hoạt động | Thông tin đầu vào | Thông tin đầu ra |
|---|---|---|---|
| Quản trị viên | Bấm Lưu | Tên 1–120 ký tự và ghi chú hợp lệ theo C.1 | Tạo vùng, về danh sách và hiển thị “Đã tạo vùng” |

### SC-02 — Dữ liệu lỗi

Điều kiện: quản trị viên đang ở UI-01.

| Đối tượng | Hoạt động | Thông tin đầu vào | Thông tin đầu ra |
|---|---|---|---|
| Quản trị viên | Bấm Lưu | Tên rỗng, vượt 120 ký tự hoặc ghi chú vượt 500 ký tự | Giữ UI-01 và dữ liệu đã nhập, hiển thị thông báo tương ứng ở C.1, không lưu |

### SC-03 — Hủy

Điều kiện: quản trị viên đang ở UI-01.

| Đối tượng | Hoạt động | Thông tin đầu vào | Thông tin đầu ra |
|---|---|---|---|
| Quản trị viên | Bấm Hủy | Dữ liệu đang nhập | Về danh sách, bỏ dữ liệu đang nhập, không hiện hộp xác nhận |
