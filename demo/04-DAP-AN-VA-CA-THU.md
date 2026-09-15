# Dành cho người hướng dẫn / người đánh giá

Không đính kèm tệp này khi chạy demo tạo mới; đây là đáp án và ca kiểm để đối chiếu. Các kết quả mẫu được biên soạn, không là kết quả benchmark. Báo cáo phát hành nêu mức kiểm chứng thật.

## Đáp án bài review có chủ đích

| Vị trí bài tập | Phát hiện và căn cứ | Tiêu chí |
|---|---|---|
| 1 | SRC-W1 §2 cấm đổi hoa/thường; mã phải duy nhất toàn danh mục, không chỉ trong loại. AB12 khác loại vẫn lỗi theo §3 | Q1, Q3 |
| 2 | Nguồn không có default loại; không có field Trạng thái theo §1. Không biến lựa chọn UI thường gặp thành requirement | Q1, Q2 |
| 3 | Bảng 100 và kịch bản 150 mâu thuẫn; nguồn §2 chỉ cho 100 | Q1, Q3 |
| 4 | Thiếu lưu một bản ghi, đích UI-01 và câu thành công; thiếu hủy không tạo bản ghi/không xác nhận; lỗi phải tại trường, giữ dữ liệu và không tạo bản ghi | Q2, Q4 |
| 5 | Không có Figma đã duyệt; URL/SLA chưa chốt theo §1/4 | Q1, Q2 |

Một phát hiện có thể ảnh hưởng nhiều tiêu chí, không tính thành nhiều lỗi để tăng số liệu. Không bắt người thử diễn đạt đúng từng chữ đáp án; phải chỉ ra nội dung, căn cứ và hậu quả đúng. Không cố tìm thêm lỗi không có bằng chứng để đủ số.

Với SRS tham khảo: Q1 đối chiếu source; Q2 giữ OQ-01–04, chưa đầy đủ để triển khai thật; Q3 C và SC-03 phải cùng trùng toàn danh mục; Q4 đầu vào/đầu ra cụ thể. Mockup đề xuất không tự là lỗi, nhưng chưa thành thiết kế được duyệt. Trạng thái DRAFT được giữ vì phần lỗi hệ thống chưa đủ căn cứ cho ứng dụng thật.

## Chạy trước/sau công bằng

Lần A: phiên sạch không nạp hai skill hay bundle, gửi SRC-W1 + “Đặc tả UI-02 Tạo vùng để Dev/Tester dùng; chỉ phạm vi trong nguồn”. Lần B: cùng model/thiết lập/nguồn/câu giao việc, nạp skill/bundle trước. Lưu prompt, kết quả và tên model thực. Không đưa đáp án vào phiên B và không chọn riêng lần A tệ nhất.

Nếu model/công cụ hoặc số lượt làm rõ khác, ghi rõ khác biệt; không quy mọi chênh lệch cho skill. Lần A đã tốt thì ghi nhận. Bài lỗi ở 03 chỉ để luyện review khi cần, luôn gắn nhãn minh họa. Bản 02 cũng là tham khảo do biên soạn, không phải chứng cứ B tốt hơn A.

Hai BA dùng cùng Q1–Q4 kiểm độc lập một output; sau đó đối chiếu vị trí/căn cứ khi kết luận khác nhau. Chưa có dữ liệu người tham gia thì chưa kết luận nhất quán hơn. Nếu đo: ghi số lỗi nguồn/logic quan trọng còn bị bỏ sót và số tiêu chí có kết luận khác nhau; không đo độ giống câu chữ.

## Ca thử trước buổi chia sẻ

Các ca dưới là yêu cầu kiểm, không mặc định đã chạy đạt. Chạy trong thư mục/phiên riêng; đầu ra tự tạo không đưa vào bản cài team. Lưu bằng chứng mới cạnh bản thử của bạn.

| Ca | Prompt / input | Điều cần quan sát |
|---|---|---|
| R1 — mode 1 | SRC-W1, tạo đặc tả một màn hình, không ghi mode | Làm trực tiếp, không đòi setup/Owner/lịch/7 câu hỏi; đủ A/B/C/D và Q1–Q4 |
| R2 — mode 2 | “Giúp chọn phạm vi một module mới từ nguồn này, mode 2” | Hỏi/chốt hướng khi có đánh đổi; sau BA chọn không hỏi lại hoặc tự chuyển mode 3 |
| R3 — mode 3 | SRC-W1, mode 3; chốt A rồi yêu cầu sửa B cụ thể | Giữ mode qua advisor→SRS; làm đúng phần, không hỏi có muốn sửa, chưa sang C trước chốt |
| R4 — nguồn thiếu | “Đặc tả form gồm Mã và Tên; chưa biết bắt buộc/độ dài”; không gửi SRC-W1 | Hỏi tối đa 3 điểm chặn, không mượn 2–10/100/default từ demo |
| R5 — phản biện | SRC-W1; BA nói “để mặc định Hành chính vì ai cũng làm vậy”, chỉ hỏi đánh giá | Chỉ ra nguồn không default, nêu thay đổi cần chốt; không tự sửa hoặc coi thói quen là nguồn |
| R6 — Update | Bản nền tham khảo; CR: Tên 100→150 và đổi câu lỗi tương ứng, giữ mọi thứ khác | Delta/ảnh hưởng tại Tên và tình huống/biên; giữ Mã/Loại; API/test không có tài liệu thật thì không bịa ID |
| R7 — advisor ngoài SRS | “Biên bản: chị Lan tổng hợp thiếu dữ liệu; anh Minh gửi danh mục ngày thứ Sáu, chưa chốt thứ Sáu nào. Tách việc, người, hạn, câu hỏi.” | Tạo bảng công việc, hạn chưa rõ giữ câu hỏi; không dựng SRS/context/BMAD |
| R8 — chỉ prompt | “Chỉ tạo prompt để tôi chuyển đặc tả này sang công cụ xuất Word, theo mẫu tôi sẽ đính kèm” | Prompt đủ nguồn/mẫu/phạm vi/đầu ra/check; không báo tạo Word hoặc đoán tool có sẵn |
| R9 — BMAD tùy chọn | Ca A: sửa một trường; ca B: cần lập PRD module rộng, muốn cân nhắc BMAD | A không ép BMAD; B đề xuất đúng mục đích/input/output, kiểm workflow khả dụng trước lệnh; không tự chạy |
| R10 — tiếp tục/duyệt | Sau chốt B mode 3, chuyển phiên với ghi chú; yêu cầu sửa bản đã được duyệt có bằng chứng | Giữ mode và tiến độ; bản sửa DRAFT, không kế thừa APPROVED; không dựng lịch sử còn thiếu |
| R11 — context | Yêu cầu setup context có review_due đã quá ngày hiện tại; bản khác chưa đặt lịch | Chỉ cảnh báo theo ngày thực; không tự gia hạn hoặc coi chưa lịch là không làm được task |
| R12 — công cụ khác | Đính kèm một bundle chat và SRC-W1 ở nền tảng thử | Đọc đúng tên/phiên bản/core; không giả native install hay đường dẫn; thiếu SRS bundle thì xin đúng tệp, không quay vòng setup |

## Một việc thật sau buổi

BA chọn trước một yêu cầu nhỏ đang làm, cung cấp nguồn/mẫu đúng task rồi dùng advisor. Hoàn thành khi có đầu ra liên quan công việc thật, BA tự chỉ ra nguồn, điểm còn mở và cách kiểm Q1–Q4; chạy xong demo giả lập chưa chứng minh đạt tiêu chí này.
