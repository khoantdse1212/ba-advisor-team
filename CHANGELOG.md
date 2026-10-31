# Changelog

Các thay đổi đáng chú ý của BA Advisor Team. Mỗi thay đổi ghi loại góp ý dẫn tới nó: nguồn, cách làm, mẫu hoặc cách kiểm.

## [3.1.0] — 2026-11-01

- **Cài đặt:** thêm plugin Codex và danh mục cài từ GitHub; gói chạy chỉ gồm Advisor, BA Setup, tài liệu liên quan và giấy phép. Giữ cách cài skill riêng và bản chat.
- **Cách làm:** chọn công cụ theo đầu ra và khả năng thực có; phân biệt nhìn thấy công cụ, đã kết nối, quyền đọc/ghi và kết quả đã kiểm. Thiếu kết nối thì hướng dẫn phần cần, không ép cài cả bộ.
- **Khởi đầu:** setup dùng lại hồ sơ, mẫu và task đã có; không chạy lại trong việc thường ngày. Không tự cấp quyền, không đóng gói credential hoặc dữ liệu dự án.
- **Giữ:** mode 1/2/3, Q1–Q4, mẫu SRS A/B/C/D, điều kiện dữ liệu thật và phiên bản cũ. Plugin không chứa MCP server riêng; dùng kết nối do nền tảng cung cấp.

Phạm vi đã kiểm và giới hạn: [kết quả v3.1](evals/RESULTS-v3.1.0.md).

## [3.0.0] — 2026-10-25

- **Cách làm:** tổ chức advisor theo ý định giao việc: hỏi/tư vấn/tạo/sửa/rà soát/làm tiếp; lời giao ngắn không đồng nghĩa thiếu mục tiêu hoặc bắt mở SRS.
- **Đơn giản hóa:** bỏ bộ nhãn Đúng ý/Sáng tạo/Lai chồng với mode; việc nhỏ trả tự nhiên, đầu ra lớn vẫn đủ chi tiết và có căn cứ. Thêm tài liệu chọn cách làm theo tình huống BA, chỉ đọc khi cần.
- **Cách kiểm:** bộ bốn ca giả lập, đầu vào tách phiếu kiểm; thử độc lập và báo đúng giới hạn, không công bố tỷ lệ tiết kiệm chưa đo.
- **Phát hành:** công cụ sinh chat và ZIP từ cùng nguồn, kiểm liên kết/metadata/mẫu SRS, bộ test công cụ; tag và ZIP v3 từ cùng commit, không thay release v2.2.
- **Giữ:** tên skill, ba mode, Q1–Q4, cấu trúc A/B/C/D, ưu tiên mẫu dự án, điều kiện bảo mật dữ liệu thật và hồ sơ hiện có. Không thêm agent bắt buộc, không tự cài framework hay di chuyển dữ liệu dự án.

Chi tiết bằng chứng và phần chưa thử ở [kết quả kiểm v3](evals/RESULTS-v3.0.0.md). Thay đổi lớn ở cách tổ chức, thử và phát hành; không phải cam kết AI hiểu đúng mọi yêu cầu.

## [2.2.0] — Cập nhật 2026-10-23

- **Cách làm:** phân biệt mục đích với phương án được đề nghị; hỏi quyết định có tác động lớn bằng lựa chọn dễ hiểu, không khuyến nghị thay nghiệp vụ chưa biết và không hỏi lại phần đã chốt.
- **Cách làm:** chọn công đoạn theo đầu ra, nguồn và công cụ thực có; dùng ví dụ tốt đúng phạm vi, không mang nghiệp vụ cũ sang việc mới. Làm rõ mode 2 và cách dùng mẫu dự án trong mode 3.
- **Cách kiểm:** ảnh hưởng thay đổi dẫn tới vị trí/phiên bản đã đọc; phân biệt nội dung đã soạn, thao tác đã thực hiện và BA đã chấp nhận.
- **Cách kiểm:** hướng dẫn thử khi sửa skill/đổi mô hình, có ca mới, lần thử lặp lại và BA khác; ghi thời gian gồm kiểm/sửa, lỗi và lần cần hỗ trợ khi đánh giá hiệu quả.
- **Mẫu:** README có cách thử một công việc thật trong team; ghi chú tiếp tục giữ đầu ra, người nhận và tiêu chí. Giữ số phiên bản v2.2.0, phân biệt bằng ngày cập nhật hoặc commit.

Đã kiểm cấu trúc, liên kết, đồng bộ bản chat/ZIP và giữ nguyên mẫu A/B/C/D. Hai lượt thử AI độc lập với dữ liệu giả cho thấy cập nhật đúng CR đã xác nhận, giữ phần ngoài thay đổi, chỉ ra đầu ra liên quan chưa sửa và hỏi nguyên nhân trước yêu cầu bỏ trường còn mơ hồ. Đây là kiểm tra có phạm vi, chưa phải so sánh hiệu quả trước/sau; chưa kiểm chứng độ ổn định qua nhiều lần chạy, mọi nền tảng hoặc đợt dùng thử với BA thật.

## [2.2.0] — Cập nhật 2026-10-16

Giữ số phiên bản theo lựa chọn của chủ repo; nội dung cập nhật trên `main` và hai gói ZIP đính kèm. Tag gốc giữ lịch sử phát hành ban đầu.

- **Cách làm:** khi tiếp tục, tìm đúng việc, bản hiện hành và nguồn/quyết định liên quan; ghi chú chung chuyển thành chỉ mục từng việc.
- **Mẫu:** giữ mốc đầu ra BA chọn theo đúng phần và phạm vi; quy tắc demo hoặc một việc lưu tại việc đó, không lan thành quy tắc chung.
- **Cách kiểm:** Q3 đối chiếu trước/sau, gồm cả phần phải giữ nguyên; áp dụng cho mọi đầu ra được giao cập nhật.
- **Nguồn:** giữ trạng thái đề nghị/đã xác nhận khi chuyển tài liệu; tách lời nhắc biên soạn khỏi quy tắc hệ thống; ghi chú ngắn dẫn nguồn thay vì trở thành nguồn thay thế.
- **Cách làm:** khôi phục khi thiếu bản hiện hành hoặc lẫn việc; hỗ trợ ghi chú gửi lại ở công cụ chỉ có chat. Giữ mode, mẫu SRS và điều kiện dữ liệu hiện có.

Đã thử một số tình huống bằng phiên AI độc lập với dữ liệu giả: chọn mốc, đổi việc, sửa theo CR và tiếp tục phiên. Chưa kiểm chứng hội thoại rất dài hoặc mọi nền tảng; lượt thử lưu ghi chú cuối bị giới hạn dịch vụ trước khi hoàn tất hội thoại, phần tệp đã được đối chiếu riêng.

## [2.2.0] — Phát hành 2026-10-14

Một skill `ba-advisor`; mọi yêu cầu đi qua một điểm vào. Hợp nhất bản 1.3.3 với các cải tiến về đầu ra và bối cảnh thực tế.

- **Cách làm:** tổ chức chỉ dẫn theo vai trò, đầu ra và người nhận; làm rõ phạm vi áp dụng, nguồn cần đọc, cách xử lý thông tin thiếu và kiểm tra trước khi bàn giao.
- **Cách làm:** Đúng ý và sáng tạo: nội dung sáng tạo mang dấu [Đề xuất] và vào tài liệu sau khi BA chọn.
- **Mẫu:** Đầu ra sạch: Nội dung bàn giao (dán thẳng vào tài liệu) và Ghi chú cho BA; lời dặn "không/đừng/chỉ" của BA được áp dụng và vắng mặt trong phần bàn giao.
- **Cách làm:** câu hỏi kèm đáp án đề xuất; việc nhiều bước nêu 2–4 tiêu chí đạt; trả lời câu hỏi của Dev; hướng dẫn BA mới bắt đầu bằng một việc nhỏ; báo đúng thao tác đã làm.
- **Nguồn:** Bối cảnh Việt Nam: văn bản pháp lý, địa giới hành chính 2 cấp từ 01/07/2025, dữ liệu định danh, định dạng ngày số, nguồn dạng tin nhắn, ảnh, bản scan.
- **Nguồn:** điều kiện dữ liệu theo xác nhận môi trường; hướng dẫn làm sạch tài liệu, checklist kỹ thuật, mẫu xác nhận chuyển vào `references/bao-mat-du-lieu.md`.
- **Cách làm:** lệnh nhanh `chốt`, `sửa`, `ghi nhớ`, `kiểm`, `làm tiếp`, `gọn`; bảng nơi lưu (việc, dự án, skill); cấu trúc thư mục dự án `HO-SO-DU-AN.md`, `nguon/`, `ket-qua/<viec>/`.
- **Mẫu:** gộp `ba-srs` vào `references/srs.md`; cập nhật sửa trên bản hiện hành, giữ bản nền phục hồi được; Delta khi BA yêu cầu; thêm luồng, bản mẫu, đối chiếu Figma, nhiều use case, mẫu Word, URD, hệ thống có sẵn, web và di động.
- **Cách kiểm:** thống nhất bốn câu hỏi Q1–Q4; định nghĩa Đạt / Cần sửa / Chưa đủ căn cứ, thêm Chưa kiểm chứng; kết quả kiểm ở Ghi chú cho BA hoặc mục kiểm của mẫu dự án; trạng thái theo dự án, mặc định Bản nháp / Chờ rà soát / Đã duyệt.
- Repo: README có bước thiết lập cho công cụ AI (giữ tùy chỉnh, báo cáo thiết lập), thử ngay với biên bản giả lập; `packages/ba-advisor.zip` cho ứng dụng Claude có Skills; `.gitignore` giữ dữ liệu dự án ngoài repo. Demo, ca thử, công cụ đóng gói thuộc bộ công cụ của người quản lý.

## [1.3.3] — 2026-10-14

- Viết gọn chỉ dẫn bằng hành động cụ thể; gom lời nhắc và điều kiện lặp.
- Chuẩn hóa tài liệu bảo mật thành điều kiện sử dụng, checklist và mẫu xác nhận.
- Làm gọn hướng dẫn bắt đầu, tài liệu bảo trì và chú thích demo; đồng bộ bản chat và ZIP.

## [1.3.2] — 2026-10-14

- Bổ sung điều kiện dữ liệu, checklist kỹ thuật và mẫu xác nhận môi trường.
- Thêm `compatibility` cho hai skill và kèm tài liệu bảo mật trong ZIP.

## [1.3.1] — 2026-10-14

- Gộp chỉ dẫn chung và làm rõ cách bàn giao Q1–Q4 theo mẫu dự án.
- Rút lời nhắc trong demo; bổ sung kiểm liên kết và đồng bộ gói.

## [1.3.0] — 2026-10-14

- Gom quy tắc về mode, nguồn, kiểm chất lượng, trạng thái và tiếp tục phiên.
- Rút cấu trúc cố định; ưu tiên mẫu dự án và hồ sơ vừa đủ.
- Tách tài liệu bảo trì; đóng gói theo danh sách tệp xác định.

## [1.2.0] — 2026-10-13

- Thêm lời giao việc thiết lập và hướng dẫn nạp theo nền tảng.
- Bổ sung tổ chức hồ sơ, tiếp tục phiên và tái sử dụng cách làm.
- Tự kiểm Q1–Q4 và sinh đồng bộ core, chat, ZIP.

## [1.1.2] — 2026-09-15

- Phát hành hai skill `ba-advisor` và `ba-srs`; bản chat và demo.
- **Cách làm:** khi nhận việc, AI nói ngắn hiểu việc, đầu ra, cách làm; đưa lựa chọn khi có đánh đổi.
- **Cách kiểm:** nhãn độ chắc chắn cạnh nội dung quan trọng; phân loại góp ý theo nguồn, cách làm, mẫu, cách kiểm.
- Thêm giấy phép MIT.
