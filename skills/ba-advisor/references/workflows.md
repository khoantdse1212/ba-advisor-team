# Cách làm, prompt và BMAD — v1.1.2

Đọc khi cần tư vấn công cụ/workflow, tạo prompt chuyển tiếp hoặc thiết lập context. Đây là hướng dẫn chọn bước, không là danh mục phải chạy hết.

## Chọn cách làm ít bước

| Nhu cầu | Cách ưu tiên | Nếu công cụ hiện tại thiếu khả năng |
|---|---|---|
| Biên bản, câu hỏi, rule, phản biện | Làm ngay bằng nguồn văn bản trong phiên | Xin đúng đoạn nguồn, không bắt tạo context dự án |
| SRS một màn hình | ba-srs với nguồn/mẫu/ảnh; cho phép mockup Markdown có nhãn nếu chưa có hình | Xin BA-SRS-CHAT.md hoặc chuẩn bị prompt kèm đúng tài nguyên cho nền tảng khác |
| Hiểu thiết kế | Đọc ảnh/export hoặc frame thật được cung cấp; đối chiếu UI với rule | Không đọc được Figma thì xin ảnh/export, không giả vờ đã xem link |
| Bảng dữ liệu lớn hoặc đối chiếu định lượng | Dùng công cụ bảng tính/tính toán sẵn có nếu phù hợp | Chuẩn bị prompt, mô tả cột/dữ liệu/mục tiêu và cách đối chiếu kết quả |
| Word/PDF có mẫu cố định | Soạn nội dung + dùng công cụ xuất giữ mẫu khi khả dụng và được giao | Giao Markdown/nội dung cùng prompt xuất; kiểm lại ảnh/bảng/phân trang, không đổi đuôi file |
| Câu hỏi về công cụ/model hiện hành | Kiểm nguồn chính thức phù hợp khi có truy cập | Nêu chưa xác minh phiên bản/tính năng; không khuyên đổi công cụ bằng trí nhớ như sự thật |

Tư vấn chỉ cần: cách phù hợp + lý do + điều kiện cần + hành động tiếp theo. Không liệt kê hàng loạt sản phẩm hoặc ép cài plugin. Việc một công cụ “có thể” làm không chứng minh nó đã được kết nối/cho quyền trong phiên.

## Prompt chuyển tiếp — hoàn chỉnh nhưng gọn

Chỉ trả prompt khi được yêu cầu hoặc cần chuyển môi trường. Điền phần đã biết, chỉ giữ dấu [cần cung cấp] cho thông tin thật sự thiếu:

```text
Việc cần làm: [hành động và đối tượng].
Mục tiêu/người dùng kết quả: [...]. Mode: [mode hiện tại].
Nguồn sẽ được đính kèm: [tệp/mục/phiên bản; không giả định đọc được đường dẫn máy khác].
Phạm vi và điều đã chốt: [...]. Ngoài phạm vi: [...].
Phần chưa rõ: [...]; chỉ hỏi phần chặn, không tự xác nhận.
Đầu ra: [nội dung/định dạng/mẫu; với SRS đính kèm cả BA-SRS-CHAT.md].
Hãy làm kết quả nếu có khả năng; nếu không, nêu đúng giới hạn.
Kiểm Q1 nguồn/phạm vi, Q2 đủ và rõ phần thiếu, Q3 nhất quán, Q4 dùng/kiểm được.
Trả một kết luận kiểm ngắn có bằng chứng; không tự phê duyệt.
```

Chỉ prompt không được gọi là “đã hoàn thành nghiệp vụ”. Không chép mọi hướng dẫn team vào prompt nếu nguồn/skill đã có; vẫn phải đủ độc lập khi chuyển sang công cụ không có lịch sử chat.

## Khi nào đề xuất BMAD

Mặc định làm task BA trực tiếp. Chỉ đề xuất khi quy mô/điểm khó cho thấy một workflow có lợi ích rõ, hoặc BA yêu cầu. Nêu **workflow phù hợp — vấn đề nó giải quyết — input cần có — đầu ra dự kiến — phần ngoài phạm vi task nhỏ**; không chạy cho tới khi BA yêu cầu. Nếu BA đã yêu cầu chạy cụ thể và workflow khả dụng, dùng đúng chỉ dẫn thực và phạm vi đó, không hỏi lại cùng quyết định.

| Tình huống | Ứng viên BMAD để đối chiếu bản cài thực tế | Không cần cho |
|---|---|---|
| Mục tiêu/scope sản phẩm rộng cần PRD | bmad-prd | Sửa một trường hoặc tóm tắt biên bản |
| Luồng trải nghiệm/nhiều màn hình chưa thành hình | bmad-ux | Một màn hình và rule đã đủ rõ |
| Cần thử thách lập luận, đào sâu phần phân tích | bmad-advanced-elicitation | Câu hỏi trực tiếp đã có đáp án trong nguồn |
| Muốn phản biện sâu một tài liệu sẵn có | bmad-review-adversarial-general | Kiểm nhanh vài dòng theo Q1–Q4 |

Tên trên được đối chiếu metadata bộ BMAD hiện có lúc đóng gói, không bảo đảm mọi bản cài dùng cùng tên. Trước khi đề xuất lệnh cụ thể phải kiểm danh sách/phiên bản khả dụng; chưa có thì tư vấn mục đích và prompt thường, không báo đã kích hoạt. Không sao chép memlog, agent menu hoặc quy trình phê duyệt của BMAD vào mọi task. Workflow ngoài có thể sinh thêm tài liệu/tốn thêm lượt: nói rõ trước khi BA chọn. Không khuyên tự bỏ kiểm tra của workflow đang dùng.

Quy chuẩn team gắn với đầu ra liên quan; cách dùng mẫu khác và tùy chỉnh của BMAD xem [hướng dẫn chính thức về áp dụng theo team](https://docs.bmad-method.org/vi-vn/customize/adopt-bmad-across-a-team/). Bộ này không yêu cầu cài BMAD.

## Project Context khi thực sự cần

Tạo/cập nhật context khi BA yêu cầu setup hoặc nhiều task cần dùng chung thông tin. Chưa có file context vẫn làm được task nhỏ nếu nguồn hiện tại đủ. Rà soát context là đọc và báo điểm cần sửa.

Context ngắn gồm: dự án/mục tiêu; trong/ngoài phạm vi; Context Owner và người xác nhận nghiệp vụ (có thể khác nhau); phiên bản/trạng thái; ngày cập nhật; ngày/phạm vi đã rà soát; review_due nếu Owner đã chốt; nguồn chính thức theo phạm vi; thuật ngữ/quyết định chung đang có hiệu lực và bằng chứng; mẫu đầu ra; câu hỏi còn mở. Giữ cấu trúc context đang có khi cập nhật, không nhân đôi rule chi tiết của SRS.

Chưa có Owner/ngày review thì ghi chưa xác định/chưa đặt lịch; không chặn bản nháp một task đã rõ. Chỉ cảnh báo quá hạn khi có review_due đã chốt và ngày hiện tại lớn hơn hạn. Quá hạn không tự làm rule sai; nguồn mới/mâu thuẫn vẫn cần kiểm dù chưa đến hạn. Không tự đặt 7/30/90 ngày, tự gia hạn, hoặc coi mở file là đã rà soát. Không có nhắc lịch tự động.

Lưu, trạng thái và chuyển tiếp phần đủ dữ liệu theo BA-CORE; không có vòng khởi tạo riêng của context.
