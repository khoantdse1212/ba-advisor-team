# Phần chuyên môn: SRS, URD, luồng, bản mẫu và tài liệu theo mẫu

Đọc khi BA giao tạo, cập nhật, rà soát SRS hoặc đặc tả chức năng, màn hình; lập bảng trường; vẽ luồng, dựng bản mẫu, đối chiếu Figma; chuyển SRS sang URD; soạn vào mẫu Word. Phần này dùng chế độ **Đúng ý** và cách trình bày **Đầu ra sạch** trong SKILL.md.

Mẫu của dự án (ghi trong hồ sơ dự án hoặc BA gửi) được ưu tiên: giữ tiêu đề, thứ tự, cột của mẫu đó. Mẫu A/B/C/D dưới đây là mẫu tham khảo của bộ hướng dẫn, dùng khi dự án chưa có mẫu. Mẫu dự án và yêu cầu của BA khác nhau, hoặc mẫu thiếu chỗ cho nội dung cần bàn giao (ví dụ hình màn hình), thì nêu cách áp dụng, chờ BA chốt rồi mới đổi cấu trúc.

## Chọn đầu ra

| Việc | Đầu ra |
|---|---|
| Đặc tả một chức năng hoặc màn hình | Thông tin tài liệu (tên/ID, phiên bản, phạm vi, nguồn, trạng thái) + A/B/C/D + Câu hỏi mở. Bắt đầu được từ PRD, biên bản, mô tả trực tiếp và nguồn giao diện đọc được. Phạm vi gồm màn hình được giao và các điểm vào, điểm ra liên quan. |
| SRS đầy đủ, dự án chưa có mẫu | 9 mục: (1) Thông tin tài liệu và lịch sử phiên bản, (2) Mục tiêu, (3) Phạm vi, (4) Nguồn tham chiếu: SRC-ID, tệp/mục, phiên bản/ngày, thẩm quyền, (5) Thuật ngữ, (6) Actor và quyền, (7) Đặc tả chức năng, lặp A/B/C/D cho từng chức năng, (8) Câu hỏi mở và mâu thuẫn, (9) Yêu cầu bổ sung: tích hợp/API, phi chức năng, xử lý nền. Actor, yêu cầu phi chức năng, SLA lấy từ nguồn. |
| Cập nhật theo thay đổi | Sửa trên bản hiện hành, giữ bản nền phục hồi được (mục Cập nhật). Bản thay đổi riêng (Delta) khi BA yêu cầu. |
| Rà soát | Danh sách phát hiện (mục Rà soát); bản gốc giữ nguyên, sửa khi BA giao |
| Nhiều use case cùng đợt | Mục Nhiều use case |
| Luồng nghiệp vụ, bản mẫu, đối chiếu Figma | Mục Luồng, bản mẫu, Figma |
| Chuyển SRS sang URD | Mục URD |

Kết quả kiểm Q1–Q4 nằm ở Ghi chú cho BA, hoặc ở mục kiểm khi mẫu dự án có mục đó.

Mode 3 đi lần lượt A → B → C → D, chờ BA chốt từng phần; chốt một phần là chốt công đoạn, việc duyệt tài liệu là bước riêng. Sửa một mục thì làm đúng mục đó. Mode 1, 2 làm một lượt. Bản bàn giao đủ từng màn hình, hình, trường, tình huống; chi tiết BA đã xem mới tính là đã chốt. Hành vi cốt lõi còn thiếu thì hỏi trước khi viết phần phụ thuộc vào nó.

Mỗi quy tắc có một vị trí chủ, nơi khác dẫn lại: quy tắc dữ liệu ở C, xử lý, luồng, trải nghiệm ở D. Dẫn SRC-ID hoặc vị trí nguồn sát mệnh đề quan trọng; một dẫn chung đặt sát bảng khi nó bao phủ cả bảng. Giữ ID cũ khi sửa.

## A. Mô tả tóm tắt

| Nội dung | Mô tả |
|---|---|
| Mục đích | Ai đạt kết quả gì |
| Đối tượng sử dụng | Vai trò, quyền theo nguồn |
| Điểm vào | Menu/breadcrumb, màn hình trước |
| Điều kiện bắt đầu | Dữ liệu, trạng thái cần có theo nguồn |
| Kết quả | Dữ liệu và phản hồi quan sát được, ở mức tóm tắt |
| Nguồn | SRC-ID/vị trí |

## B. Yêu cầu giao diện

Liệt kê các màn hình trong phạm vi, rồi lặp B.n — UI-ID/tên cho từng màn hình:

- **Hình:** ưu tiên thiết kế UX → Figma hoặc ảnh BA cung cấp → mockup Markdown. Hình nằm ngay trong tài liệu.
- **Chú thích:** hình thể hiện gì; tên, phiên bản, frame nguồn. Hình tự dựng mang dòng **ĐỀ XUẤT — CHƯA XÁC NHẬN** để phân biệt với ảnh chụp hệ thống thật.
- **Thành phần** và **đường đi** theo hai bảng dưới; điều kiện hiển thị, trạng thái rỗng, tải, lỗi, route lấy từ nguồn, phần nguồn để ngỏ đưa vào Câu hỏi mở. Mỗi đường đi dẫn tới SC-ID tương ứng ở D.

| Thành phần/nhãn | Vị trí trong hình | Chức năng | Điều kiện/trạng thái |
|---|---|---|---|

| Từ màn hình | Thao tác/điều kiện | Đích/trạng thái | Dữ liệu giữ/đổi |
|---|---|---|---|

Bảng trường của màn hình nằm ở C với cùng UI-ID. Việc thuần API hoặc job nền: mục B ghi N/A kèm lý do.

## C. Mô tả trường thông tin

Một bảng cho mỗi màn hình (C.n — UI-ID/tên). Trường có ở nhiều màn hình được ghi ở từng màn hình, nêu nhập hay chỉ đọc và dẫn về quy tắc chủ.

| Trường thông tin | Kiểu điều khiển | Độ dài | Giá trị mặc định | Mô tả trường thông tin & Ràng buộc/điều kiện | Bắt buộc |
|---|---|---|---|---|---|

- Mỗi trường hoặc cột dữ liệu một dòng; nút có dòng khi có hành vi cần đặc tả. Kiểu điều khiển là textbox, dropdown, label, datepicker…
- Độ dài ghi min/max và đơn vị. Giá trị mặc định ghi "Không có" khi nguồn nói rõ, [Cần xác nhận] khi nguồn để ngỏ.
- Bắt buộc ghi Có / Không / Có khi… / N/A cho trường chỉ hiển thị.
- Cột mô tả gồm: ý nghĩa, nguồn giá trị, cách nhập hoặc chọn, đọc/sửa, quan hệ với trường khác, điều kiện kiểm, thời điểm kiểm và câu thông báo đúng nguyên văn nguồn. Thông báo hoặc thời điểm kiểm còn để ngỏ thì ghi [Cần xác nhận].
- Các xử lý như trim, đổi hoa thường, làm tròn, regex, min/max, trường audit, nguồn danh mục lấy từ nguồn; quy tắc rỗng, duy nhất, phụ thuộc trường giữ đúng như nguồn.

## D. Các tình huống sử dụng

Mỗi SC-ID có tên/mục tiêu, điều kiện bắt đầu, nguồn và bảng bốn cột:

| Đối tượng | Hoạt động | Thông tin đầu vào | Thông tin đầu ra |
|---|---|---|---|

- Mỗi dòng là một thao tác của người dùng; xử lý và phản hồi của hệ thống nằm ở cột Đầu ra cùng dòng. Sự kiện nền độc lập có nguồn thì có dòng riêng cho hệ thống.
- Gồm luồng chính, luồng thay thế, luồng lỗi có trong nguồn; nhánh nguồn để ngỏ đưa vào Câu hỏi mở.
- Đầu ra viết dạng kiểm được: "Khi [thao tác/điều kiện], hệ thống [phản hồi quan sát được]"; "Nếu [lỗi], hệ thống [xử lý], giữ [dữ liệu]". Nêu đích màn hình, dữ liệu trước và sau.
- Lỗi dữ liệu dẫn về dòng trường ở C.

## Cập nhật

1. Xác định bản nền, phiên bản, nguồn thay đổi (CR) và phần được giao; xác định nguồn có hiệu lực ở phần thay đổi.
2. Giữ bản nền phục hồi được (lịch sử phiên bản hoặc bản sao), rồi sửa đoạn, bảng, hình liên quan ngay trên bản hiện hành theo mẫu; giữ ID và các phần ngoài thay đổi.
3. Kiểm ảnh hưởng tới: màn hình, luồng; trường, dữ liệu; quy tắc, tình huống; API, tích hợp; quyền; kiểm thử; tài liệu liên quan như URD.

Bàn giao theo thứ tự: **đã đổi gì, ở đâu → ảnh hưởng và việc còn lại → Q1–Q4 trong ghi chú**. Mục ảnh hưởng liệt kê nhóm **Bị ảnh hưởng** và nhóm **Chưa xác định** (thiếu tài liệu để kiểm, ví dụ API, kiểm thử), mỗi nhóm kèm việc cần làm; các nhóm đã kiểm mà giữ nguyên gom vào một dòng "Đã kiểm, giữ nguyên: …".

**Bản thay đổi riêng (Delta):** khi BA yêu cầu, dùng mẫu CR của dự án; dự án chưa có mẫu thì gồm năm mục: (1) thông tin thay đổi: bản nền, phiên bản mới, CR, trạng thái; (2) chỉ mục thay đổi: Loại (Thêm / Sửa / Bỏ) | Vị trí | Hiện tại | Sau thay đổi | Lý do/nguồn, "Sửa" ghi nội dung mới đầy đủ, "Bỏ" ghi lý do; (3) đặc tả sau thay đổi của các phần A/B/C/D bị tác động; (4) ảnh hưởng như trên; (5) câu hỏi mở mới hoặc bị tác động. Figma, API, kiểm thử được sửa khi BA giao riêng.

**Hệ thống có sẵn:** trước khi đặc tả, xác định chức năng hiện có được giữ, sửa hay làm mới, có dẫn nguồn. Ứng dụng di động đối chiếu với nghiệp vụ web tương ứng bằng bảng khác biệt theo màn hình, thao tác, quyền; khác biệt nguồn để ngỏ đưa vào Câu hỏi mở.

## Rà soát

Đọc phần giới hạn mà tài liệu tự nêu, rồi đối chiếu hai chiều nguồn ↔ tài liệu: tiền điều kiện, thông báo, vị trí giao diện, quy tắc, nhánh hợp lệ, không hợp lệ và biên; so hình, bảng, luồng theo UI-ID. Mỗi phát hiện ghi: vị trí, căn cứ, ảnh hưởng tới dev hoặc tester, hướng xử lý. Tách lỗi xác định với câu hỏi hoặc đề xuất đã ghi rõ trong tài liệu, và nêu điểm nào chặn mục đích bàn giao. Một phát hiện chạm nhiều tiêu chí Q vẫn tính là một. Báo các phát hiện có căn cứ; tài liệu đúng thì kết luận Đạt. Q1–Q4 đánh giá chất lượng đặc tả; phần mềm chạy đúng được kiểm ở bước kiểm thử.

## Luồng, bản mẫu, Figma

| Đầu ra | Cách làm và kiểm |
|---|---|
| Luồng nghiệp vụ | Sơ đồ Mermaid hoặc hình tĩnh theo nhu cầu trao đổi; mỗi bước, nhánh dẫn nguồn; bước, nhánh tự thêm mang dấu [Đề xuất] |
| Bản mẫu (prototype) | Hình tĩnh hoặc trang thao tác thử khi cần trao đổi với khách hàng; ghi rõ là bản đề xuất; hành vi đối chiếu với nguồn và BA xác nhận |
| Đối chiếu Figma, thiết kế | Dùng bản thiết kế hiện hành BA chỉ định, xác định màn hình và phạm vi; đối chiếu nhãn, trường, trạng thái, đường đi với đặc tả; chênh lệch ghi [Mâu thuẫn] kèm vị trí ở cả hai bên |

## Nhiều use case cùng đợt

Dùng danh sách use case được giao làm chỉ mục. Nhóm các use case có cấu trúc giống nhau, dựng khung một lần rồi dùng cho cả nhóm. Quy tắc, trường, thông báo của từng use case lấy từ nguồn của chính use case đó. Giữ bảng theo dõi: UC-ID | Nhóm | Trạng thái | Nguồn | Câu hỏi mở. BA kiểm theo từng use case.

## Mẫu Word, PDF, Excel

Soạn nội dung theo đúng heading, bảng, đánh số của mẫu, rồi chèn vào mẫu bằng công cụ chạy trên máy, giữ nguyên style. Sau khi xuất, mở lại tệp để kiểm mục lục, chú thích hình và bảng, đánh số, phân trang, số liệu. Khi công cụ chưa chèn được vào mẫu, giao nội dung kèm chỉ dẫn vị trí để BA chèn. Tệp xuất đúng định dạng thật (.docx).

## URD

Đầu vào là SRS đã chốt và mẫu URD của dự án. Viết theo góc nhìn người dùng cuối: làm gì, ở đâu, thấy gì; giữ những gì người dùng cần để thao tác. Điểm chưa xác nhận đưa vào danh sách theo dõi riêng, tách khỏi nội dung nghiệm thu. Q1 với URD là khớp SRS đã chốt; rà lại theo từng đối tượng sử dụng.
