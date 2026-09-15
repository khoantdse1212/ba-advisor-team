# BA Advisor Team v1.1.2 — bổ sung định hướng và học từ phản hồi

Ngày chuẩn bị: 15/09/2026. Bản nền v1.1.1 giữ nguyên. Chỉ bổ sung bốn điều chỉnh đã được audit; không cài đè vào workspace đang dùng và không thêm skill, công cụ hoặc tài liệu hướng dẫn riêng.

## 1. Thay đổi đã thực hiện

| Phần | Thay đổi v1.1.2 | Giữ nguyên |
|---|---|---|
| Định hướng mode 1 | Khi nhận task, nói ngắn hiểu việc/đầu ra/cách làm; chỉ đưa options khi có đánh đổi, không tạo lượt xin xác nhận thừa | Mode 1/2/3 và nguyên tắc chờ khi cần quyết định |
| Chọn skill | Bản đồ rõ: advisor cho phân tích/tư vấn, srs cho SRS/màn hình; task chưa rõ bắt đầu ở advisor | Hai tên skill, handoff một lần |
| Độ chắc chắn | Hiển thị nhãn Đã có căn cứ / Đề xuất / Cần xác nhận / Mâu thuẫn cạnh nội dung quan trọng | Q1–Q4, nguồn và OQ/CF |
| Cải tiến | Phân loại lỗi phản hồi theo nguồn/workflow/mẫu/cách kiểm; chỉ cập nhật skill khi lỗi lặp lại/ảnh hưởng đáng kể và thêm ca thử | Bộ test, audit và quản lý phiên bản |

Quy tắc Q1–Q4 được giữ nguyên: SRS/Delta đầy đủ, kể cả bản nháp, phải có một bảng đủ bốn dòng; “gom kiểm tra” không có nghĩa thay bảng bằng câu “đã kiểm”. Nháp một công đoạn đang chờ chốt và việc nhỏ vẫn dùng vài dòng.

Không áp dụng những đề xuất ngoài ba việc đã chọn: không bỏ mode, BMAD, Context Owner, lịch rà soát hoặc năng lực tư vấn. Không đổi tên hai skill, UI metadata, cấu trúc SRS và cột bảng.

## 2. Các điều kiện được bảo toàn

- Bốn phần A/B/C/D theo thứ tự; từng màn hình có hình/chú thích, thành phần, đường đi và bảng trường riêng.
- Bảng trường sáu cột, tình huống bốn cột; rule/AC dữ liệu ở C, xử lý/UX ở D.
- Không bắt URD hoặc context cho task nhỏ; không tự điền rule/default/quyền/route thiếu nguồn.
- Mode 1 mặc định, mode 2 chọn hướng, mode 3 từng công đoạn; giữ mode khi tiếp tục, không coi im lặng là đồng ý.
- Truy nguồn sát phần thay đổi, giữ bản cũ, phân biệt chưa biết với N/A; DRAFT/READY_FOR_REVIEW/APPROVED không lẫn với kết luận kiểm.
- Hai bản BA-CORE đồng nhất và hai bản gộp chat đủ tài nguyên, dùng độc lập.
- Năm tệp demo giữ nguyên từ v1.1.0, là ví dụ được biên soạn, không phải output kiểm thử v1.1.2 hoặc bằng chứng hiệu quả.

## 3. Kiểm tra

| Hạng mục | Hiện trạng |
|---|---|
| Cấu trúc hai SKILL.md | Hợp lệ qua quick_validate.py |
| Đồng bộ lõi, bundle, liên kết, mẫu bảng và danh sách file | Đã kiểm; không thêm/bớt tệp trong gói |
| Bản v1.1.0 | Đối chiếu mã kiểm toàn thư mục trước/sau, không thay đổi |
| Ca advisor v1.1.2 | Đã chạy bằng phiên Codex độc lập với biên bản giả lập: AI chọn đúng ba-advisor, mở đầu bằng phạm vi/căn cứ, tách hai việc và ba câu cần làm rõ, không tự gán hạn/người duyệt |
| Ca SRS v1.1.2 | Đã chạy bằng phiên Codex độc lập với hai nguồn giả lập: đầu ra đủ A/B/C/D, mockup có nhãn đề xuất, bảng trường/bảng tình huống và một bảng Q1–Q4; các điểm thiếu được gắn Cần xác nhận |
| ZIP | Kiểm CRC và đối chiếu từng tệp với thư mục phát hành trước bàn giao; không có output/log thử hoặc công cụ build trong ZIP |

Các lượt thử v1.1.2 dùng nguồn giả lập, không gửi tài liệu dự án thật. Hai kết quả cho thấy hành vi mới ở một ca advisor và một ca SRS; đây là bằng chứng định tính ban đầu, không phải phép đo nhân quả hoặc tỷ lệ cải thiện giữa nhiều BA/model.

Máy thử có chỉ dẫn cá nhân “chỉ trình bày checklist khi được yêu cầu”, có thể tác động việc hiện bảng kiểm khi prompt không yêu cầu rõ. Vì vậy ca SRS v1.1.2 dùng đúng câu yêu cầu bảng Q trong hướng dẫn; chưa kết luận mọi lời giao ngắn đều tự sinh bảng kiểm.

Nhật ký nguyên văn, prompt, phiên bản chỉ dẫn trước/sau sửa và kết quả kiểm nằm ngoài ZIP tại hồ sơ kiểm thử của người giữ gói. Không đưa log kỹ thuật vào SRS hay bắt BA sử dụng phải đọc chúng.

## 4. Chưa được kiểm chứng

Chưa chứng minh hiệu quả giữa nhiều BA/model, chưa chạy bundle trên Claude/Antigravity, chưa thử lại toàn bộ mode 2/3 hoặc mọi ca R1–R12 trên v1.1.2. Không suy kết quả v1.1.0 sang bản mới. Chưa thử phần mềm, Figma/API hoặc nguồn nghiệp vụ thật.

Thao tác cài trên máy người nhận và thời lượng buổi chia sẻ cần họ thử. Trang HTML giữ nguyên, không chạy AI; kiểm HTML của bản v1.1.0 không thay cho kiểm hành vi skill.

## 5. Bàn giao

Đọc [hướng dẫn sử dụng](HUONG-DAN-SU-DUNG.md) để bắt đầu. Thay đúng hai thư mục skill khi nâng cấp; bản gộp chat được tạo lại từ cùng tài nguyên. Không cài song song hai phiên bản cùng tên. Giữ bản v1.1.0 ngoài nơi tự nạp để quay lại khi cần.

Nguồn đường dẫn nạp: [OpenAI](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills), [Antigravity](https://antigravity.google/docs/skills). Đây là căn cứ hướng dẫn, không bảo đảm máy/tài khoản nào cũng có cùng khả năng.
