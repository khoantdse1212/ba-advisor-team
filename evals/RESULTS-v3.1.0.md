# Kiểm v3.1.0

Bản ghi ngày 01/11/2026, trước phát hành. Kết quả v3.0.0 không được tính là lần chạy của bản này. Chỉ dùng dữ liệu giả lập, không truy cập hệ thống khách hàng.

## Đóng gói và cài đặt thật

- `python3 scripts/release.py build` và `check`: đồng bộ nguồn, chat, gói skill/plugin, liên kết và mẫu SRS. 16 test đóng gói qua, gồm kiểm phiên bản, đường dẫn onboarding, bản cài cũ và tệp lạ trong thư mục plugin.
- SRS A/B/C/D, mẫu hồ sơ và hướng dẫn dữ liệu thật không thay đổi so với bản nền trước cập nhật.
- Codex CLI `0.166.0-alpha.5.1`: thêm marketplace local, chạy `codex plugin add ba-advisor-team@ba-advisor-team`; kết quả trả phiên bản **3.1.0**, danh sách xác nhận **installed: true, enabled: true**. 11 tệp trong cache cài đặt khớp từng byte với gói nguồn, không có tệp thừa.
- Một phiên Codex mới, dùng bản cài thật: yêu cầu gọi `$ba-setup` thuộc plugin và xác nhận tệp đã đọc. Phiên này nhận diện `ba-advisor-team:ba-setup`, mở đúng SKILL.md trong cache v3.1.0 và trả đúng phiên bản. Đây là kiểm nạp bằng lời gọi rõ ràng, chưa chứng minh tự chọn skill trong mọi yêu cầu.
- `quick_validate.py` của skill-creator chưa chạy được vì môi trường thiếu PyYAML. Frontmatter và metadata đã được đọc bằng Ruby YAML; bộ kiểm riêng và trình nạp Codex đều chạy được. Không coi đó là đã chạy quick_validate.

## Hai lượt thử hành vi độc lập

Agent nhận bản sao nội dung plugin đã cài và nguồn giả trong thư mục riêng; không nhận tiêu chí chấm hoặc đáp án dự kiến. Mỗi tình huống chạy một lần. Công cụ bên ngoài không được phép dùng trong hai lượt này.

| Yêu cầu | Đầu vào | Kết quả quan sát |
|---|---|---|
| “Thiết lập rồi tiếp tục XUAT; hồ sơ đủ; trao đổi trong chat” | Hồ sơ chỉ đúng task, mode 3, đã chốt Excel theo bộ lọc; còn quyền xuất chưa chốt | Đọc Setup → Advisor → hồ sơ; giữ mode 3, hỏi đúng quyền xuất, không dựng lại dự án hoặc mở lại định dạng đã chốt |
| “Làm UI spec; nếu được dựng Figma; làm phần được, không bắt cài cả bộ” | Hai màn hình Khu vực; Mã 10, Tên 80 ký tự; trùng mã/quyền/lỗi chưa chốt | Tạo tệp UI spec hai màn hình với mockup và nhãn đề xuất; giữ giới hạn/điểm mở; nói rõ chưa tạo Figma, không giả node/link hoặc yêu cầu cài thêm |

UI spec được đối chiếu lại với nguồn sau lượt thử. Bản nháp khá chi tiết; mức gọn và bố cục cần BA đánh giá theo mục đích trao đổi. Không quy đổi các quan sát này thành điểm thông minh, tỷ lệ giảm lỗi hay thời gian tiết kiệm.

## Chưa kiểm chứng

Demo `docs/index.html` được kiểm bằng trình duyệt trên desktop và viewport mobile 390px: bắt buộc, quá dài, ba lựa chọn mã trùng, Lưu/Hủy, đổi giới hạn, trạng thái Figma mô phỏng, chuyển mẫu câu/bảng, tải UI spec/prompt và lưu/khôi phục phiên. Prompt giữ mẫu riêng/tiêu chí nhập, không dùng mẫu để đổi nghiệp vụ; nội dung người dùng nhập được hiển thị như văn bản. Đây là kiểm phần mềm demo, **không phải lượt thử AI bổ sung hoặc phép đo hiệu quả của plugin**. Việc áp dụng mẫu tùy ý do AI thật chưa được kiểm trong bản HTML.

- Nút Setup trong giao diện desktop, thiết lập ngay giữa hội thoại hoặc tự chọn plugin khi không gọi tên.
- Đọc/ghi Figma, Drive hoặc dịch vụ thật, đăng nhập OAuth, hết hạn quyền và lỗi ghi từ connector thật. Hai lượt giả lập không thay cho thử tích hợp.
- Nhiều BA, nhiều model, Windows, mọi nền tảng hoặc độ ổn định sau nhiều lượt. Skill riêng/chat vẫn được đóng gói nhưng plugin mới tập trung Codex.

Cách lặp lại: cài gói vào Codex, mở phiên mới và thử gọi đúng skill; sau đó dùng nguồn giả với một việc đọc và một việc ghi trong dịch vụ được phép. Đối chiếu Q1–Q4, phiên bản và kết quả thực tế; không dùng dữ liệu dự án thật để thử khi chưa đáp ứng điều kiện của nhóm.
