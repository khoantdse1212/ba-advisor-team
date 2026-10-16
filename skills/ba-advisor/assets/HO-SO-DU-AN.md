# Hồ sơ dự án — <Tên dự án>

> Đặt tệp này ở gốc thư mục dự án, cùng `nguon/` (bản gốc tài liệu đầu vào) và `ket-qua/<viec>/` (đầu ra, ghi chú của từng việc). ba-advisor đọc tệp ở mỗi việc, nên giữ ngắn và chỉ ghi điều đã có căn cứ hoặc đã chốt; chi tiết để trong tài liệu nguồn và dẫn tới.

Cập nhật: <ngày> · Người phụ trách hồ sơ: <tên/vai trò>

## 1. Môi trường AI

- Xác nhận môi trường cục bộ: <Có/Chưa> · Người xác nhận: <…> · Ngày: <…> · Công cụ/mô hình: <…> · Phạm vi dữ liệu: <…>
- Nơi lưu mẫu xác nhận và bằng chứng: <đường dẫn tại máy>
- Kiểm lại khi đổi công cụ, mô hình, tiện ích hoặc phạm vi (theo `references/bao-mat-du-lieu.md` của skill ba-advisor).

## 2. Phạm vi và nguồn chính thức

Phạm vi: <…>

| SRC-ID | Tài liệu/vị trí | Phiên bản/ngày | Hiệu lực, thẩm quyền |
|---|---|---|---|

## 3. Mẫu đang dùng

SRS: <đường dẫn> · URD: <…> · Word: <…>

## 4. Thuật ngữ

| Thuật ngữ | Nghĩa | Cách gọi thống nhất |
|---|---|---|

## 5. Quyết định đã chốt

Chỉ ghi quyết định dùng chung; quyết định riêng dẫn tới ghi chú của việc tương ứng. Khi có quyết định thay thế, giữ liên kết để biết phần nào còn hiệu lực.

| ID | Nội dung, phạm vi áp dụng | Người, ngày | Căn cứ / quyết định thay thế |
|---|---|---|---|

## 6. Câu hỏi còn mở

Chỉ ghi câu hỏi dùng chung; câu hỏi riêng đặt ở ghi chú của việc đó hoặc dẫn tới vị trí trong đầu ra, không chép thành hai danh sách.

| ID | Câu hỏi | Người trả lời | Hạn | Trạng thái |
|---|---|---|---|---|

## 7. Quy tắc riêng (ghi nhớ)

Áp dụng đúng phạm vi đã chọn. Quy tắc riêng của một việc hoặc bản demo lưu trong ghi chú việc đó; chỉ quy tắc dùng chung mới đặt ở đây. Thêm bằng lệnh `ghi nhớ: …`.

| Ngày | Quy tắc và phạm vi áp dụng | Căn cứ / điều kiện thay thế (nếu có) | Ví dụ đúng |
|---|---|---|---|

## 8. Skill riêng của dự án

| Skill | Dùng khi |
|---|---|

## 9. Các việc đang mở

| Việc | Ghi chú để tiếp tục |
|---|---|

Mỗi việc cần làm tiếp có một ghi chú tại `ket-qua/<viec>/` (dùng tệp hiện có nếu phù hợp). Bản hiện hành, trạng thái và bước tiếp theo lưu ở ghi chú đó, không chép lại ở đây. Việc nhỏ làm một lần không cần tạo ghi chú.

Khung ghi chú để phiên sau đọc lại; điền phần đã biết. Khi ghi chú cũ dài, rút nội dung trùng với đầu ra/nguồn thành đường dẫn. Chỉ giữ tóm tắt quyết định chưa có nơi lưu khác, cùng căn cứ và phạm vi. Không dùng ghi chú này làm bản thứ hai của báo cáo thay đổi hoặc Q1–Q4.

- **Việc / mode / phạm vi:** <mục tiêu hiện tại>.
- **Đang dùng / mốc cần giữ:** <tệp, phiên bản, trạng thái>; <bản BA chọn và điều được chọn>.
- **Nguồn / quyết định:** <đường dẫn, phần còn hiệu lực hoặc bị thay thế>; <quyết định chỉ có trong chat: nội dung, người, ngày, phạm vi, căn cứ>.
- **Còn mở:** <dẫn tới câu hỏi, mâu thuẫn và ảnh hưởng bước sau>.
- **Đã kiểm / chưa kiểm:** <kết luận ngắn kèm vị trí đối chiếu; giới hạn>.
- **Tiếp theo:** <việc cần làm hoặc quyết định đang chờ>.
