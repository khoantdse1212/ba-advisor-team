# Bài tập phát hiện lỗi

**BẢN LỖI CÓ CHỦ ĐÍCH — chỉ để luyện kiểm Q1–Q4.** Không phải output thật của một model không dùng skill; không dùng để tuyên bố skill cải thiện chất lượng hay hiệu suất. Đối chiếu với SRC-W1 trong 01-INPUT.md, không dùng bài này làm nguồn nghiệp vụ.

## Trích đoạn cần review

1. Mã vùng được tự đổi thành chữ in hoa và chỉ cần duy nhất trong cùng Loại vùng.
2. Loại vùng mặc định Hành chính; có thêm trường Trạng thái mặc định Hoạt động.
3. Tên vùng tối đa 100 ký tự trong bảng trường; kịch bản Lưu chấp nhận tên có 150 ký tự.
4. Lưu thành công: hệ thống xử lý và thông báo phù hợp. Hủy: hệ thống xử lý phù hợp. Không nêu lỗi theo trường hoặc kết quả khi hủy.
5. UI tuân thủ Figma đã duyệt; đường dẫn /regions/create. SLA tối đa 2 giây.

Yêu cầu: trả Q1–Q4, vị trí lỗi, căn cứ SRC-W1 và ảnh hưởng tới Dev/Tester; không sửa file và không dùng từ “đạt” nếu chưa kiểm nguồn.
