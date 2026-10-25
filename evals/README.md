# Thử xem skill có giúp đúng việc không

Cho người quản lý hoặc BA muốn so sánh. **Dữ liệu hoàn toàn giả lập**, không phải minh chứng năng suất dự án. Bộ này nằm ngoài thư mục skill AI nạp.

## Thử một ca trong 5–10 phút chuẩn bị

1. Chọn một ca trong [cases.json](cases.json): biên bản, cập nhật SRS, làm tiếp hoặc làm rõ yêu cầu.
2. Dùng phiên mới với skill cần thử. Chỉ gửi `prompt` và các tệp ở `files` của ca đó; không gửi phiếu kiểm, kết quả cũ hoặc cả lịch sử xây skill. Nếu có Python 3, lệnh dưới tạo sẵn thư mục tạm gồm skill, đầu vào và `TASK.md`:

   ```bash
   python3 scripts/release.py prepare 01-bien-ban
   ```

   Mở thư mục được báo; yêu cầu AI đọc `skill/ba-advisor/SKILL.md` và thực hiện `TASK.md`. Không có Python thì sao chép thủ công phần `files`; tên tệp là tên khóa trong JSON.
3. Lưu câu trả lời và tệp thật được tạo. Người kiểm mở [RUBRIC.md](RUBRIC.md), so với nguồn và kiểm Q1–Q4. Mục chưa chạy phải ghi Chưa kiểm chứng.

Mỗi ca chỉ thực hiện việc được giao. Không cần cho AI đọc toàn repo; nếu thử trong agent có quyền đọc toàn máy, việc không đọc rubric là giới hạn hướng dẫn, không phải cách ly kỹ thuật. Muốn kiểm mù chặt hơn, chỉ cấp thư mục tạm cho phiên thử. Ghi cả cấu hình người dùng có thể ảnh hưởng đầu ra (ví dụ không hiện checklist nếu chưa được hỏi); skill không được ghi đè chỉ dẫn có độ ưu tiên cao hơn.

Biến thể **02b**: chuẩn bị ca 02, thêm vào `TASK.md` câu “Kèm bảng Q1–Q4 và vị trí đối chiếu để tôi kiểm”. Đây là một yêu cầu bàn giao riêng, không tính kết quả thay thế cho ca 02 ban đầu.

## So sánh cách cũ với v3

Chạy lại cùng ca ở hai phiên độc lập với cùng model/công cụ. Giữ đầu vào, quyền và tiêu chí như nhau; khác mỗi cách làm/phiên bản skill. Giữ output gốc, ghi lỗi và phần phải sửa, không chọn chỉ lượt đẹp nhất. Thử thêm một việc mới chưa dùng để chỉnh skill và lặp lại ca quan trọng trước khi dùng rộng.

Nếu cần đo hiệu quả, ghi: **tổng thời gian gồm kiểm/sửa, lỗi quan trọng còn lại, số lần cần hỗ trợ**. Thời gian agent chạy không thay thời gian BA kiểm. Chưa có baseline thì chưa kết luận nhanh hơn hoặc giảm bao nhiêu phần trăm.

| Lần thử | Skill/commit, model/công cụ | Ca | Bằng chứng Q1–Q4 | Phần cần sửa/chưa kiểm | BA xác nhận |
|---|---|---|---|---|---|

Kết quả của đợt phát hành: [v3.0.0](RESULTS-v3.0.0.md). Chỉ là thử có giới hạn, không bảo đảm mọi nền tảng hoặc mọi công việc.
