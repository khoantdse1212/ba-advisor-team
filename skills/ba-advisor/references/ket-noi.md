# Dùng công cụ và kết nối đúng việc

Đọc khi cần truy cập nguồn hoặc thao tác trên đầu ra qua công cụ. Áp dụng cùng phạm vi, mode, nguồn và điều kiện dữ liệu trong SKILL.md; không tạo vòng hỏi riêng.

## Từ việc cần làm tới khả năng thực có

1. Xác định thao tác cần cho **đầu ra đã giao**: đọc tài liệu, tìm nguồn, sửa tệp, dựng hình, chỉnh thiết kế hoặc kiểm kết quả. Một câu trả lời từ nguồn đã đủ không cần gọi connector.
2. Tìm skill/công cụ liên quan trong danh sách thực sự được host cung cấp; chỉ khám phá nhóm khả năng cần dùng. Ưu tiên kết nối đang có. Đọc hướng dẫn của skill chuyên môn trước thao tác khi công cụ yêu cầu.
3. Kiểm dữ liệu được phép dùng trước truy cập; rồi dùng thao tác đọc hẹp nhất vào đúng tài liệu/vị trí để xác định có quyền và đúng nguồn. Công cụ hiện tên chưa chứng minh đã đăng nhập; đọc được chưa chứng minh ghi được.
4. Thực hiện phần đã được giao và đủ điều kiện. Không hỏi lại quyền sửa đã rõ trong yêu cầu; link tham khảo, quyền đọc hoặc việc cài plugin không phải yêu cầu sửa. Không tự gửi tin, công khai, cài dịch vụ hoặc tăng quyền chỉ để hoàn thành nhanh.
5. Đối chiếu kết quả theo khả năng công cụ: mở lại đúng tệp/vị trí/phiên bản, xem thay đổi hoặc ảnh nếu liên quan. Nêu rõ phần đã tạo, đã đối chiếu và chưa thử. Không gọi “đã đồng bộ” khi mới có bảng liên kết.

| Việc cần | Khả năng tìm trong môi trường | Nếu thiếu |
|---|---|---|
| Lấy nguồn được phép dùng | Đọc tệp đính kèm/local hoặc connector tài liệu | Xin bản được phép đọc hoặc làm phần đã có nguồn |
| Hoàn thiện đặc tả | Skill tài liệu/SRS, công cụ ghi đúng định dạng | Soạn nội dung hoàn chỉnh trong chat, nói rõ chưa có tệp |
| Đối chiếu/chỉnh Figma | Skill thiết kế và công cụ đọc/ghi Figma tương ứng | Giao UI spec/prompt chuyển tiếp nếu hữu ích; không giả đã tạo node |
| Kiểm prototype | Công cụ chạy/mở trình duyệt và kiểm hành vi | Phân biệt rà nội dung với thử thao tác thật |
| Tiếp tục công việc | Hồ sơ và bản hiện hành đúng task | Hỏi vị trí/bản còn thiếu; không lấy dữ liệu từ task khác |

Tên dịch vụ ở bảng là ví dụ, không phải phụ thuộc cần cài. Không gọi tên hàm hoặc tham số từ trí nhớ nếu host chưa cung cấp mô tả.

## Thiếu kết nối, quyền hoặc nguồn

- Thiếu công cụ: nói ngắn **cần khả năng gì → phần nào bị chặn → cách làm được ngay**. Nếu có công cụ tìm plugin của host, tìm đúng khả năng rồi đề xuất lựa chọn cần thiết; chỉ cài khi được giao. Không gửi dữ liệu dự án vào truy vấn tìm plugin.
- Chưa đăng nhập/thiếu quyền: hướng dẫn BA kết nối hoặc cấp đúng quyền bằng giao diện của nền tảng. Không xin mật khẩu/token trong chat; không đổi cấu hình quyền thay BA khi chưa được giao. Không dùng đường khác để vượt hạn chế của nguồn.
- Nhiều bản: dùng chỉ mục/phiên bản đã xác nhận; mâu thuẫn cốt lõi thì hỏi trước phần phụ thuộc. Không chọn “mới nhất” chỉ theo ngày sửa.
- Lỗi ghi/timeout: kiểm xem thay đổi đã xảy ra trước khi thử lại, tránh tạo trùng. Không lặp lại khi điều kiện không đổi. Phần độc lập tiếp tục trong phạm vi giao.
- Quy định hiện tại yêu cầu dữ liệu dự án thật xử lý hoàn toàn local: connector đám mây vẫn không được dùng để gửi/đọc dữ liệu thật vào môi trường AI ngoài phạm vi đó. Kết nối có sẵn không làm mất điều kiện này. Dữ liệu giả/công khai/đã làm sạch được phép dùng theo yêu cầu; không ép setup bảo mật lại.

## Lưu vừa đủ để lần sau dùng tiếp

Trong ghi chú task đã có, lưu đường dẫn nguồn/đầu ra, phiên bản, thao tác đã kiểm và phần thiếu. Không lưu credential hoặc bản sao dữ liệu không cần thiết. Có thể ghi kết nối đã dùng và ngày kiểm; lần sau kiểm lại thao tác cần thiết, không coi trạng thái cũ là quyền còn hiệu lực. Không tạo thêm sổ kết nối cho mỗi task.
