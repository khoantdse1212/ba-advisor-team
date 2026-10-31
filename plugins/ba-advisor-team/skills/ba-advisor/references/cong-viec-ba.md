# Chọn cách làm theo công việc BA

Đây là các điểm tựa khi advisor cần chọn đầu ra, không phải checklist bắt làm hết. Dùng nguyên tắc nguồn, mode, dữ liệu và Q1–Q4 trong SKILL.md; công việc nhỏ không cần hồ sơ hoặc menu.

## Biên bản → nội dung làm việc được

Tách điều đã thống nhất, yêu cầu/ý kiến còn đề nghị, việc cần làm (người/hạn nếu nguồn có), câu hỏi và mâu thuẫn. Giữ nguồn sát ý quan trọng. Thiếu người/hạn thì ghi chưa rõ; ví dụ khối lượng chưa phải giới hạn hệ thống. Không chuyển mọi nội dung thành requirement hoặc tự viết SRS.

Nếu BA chỉ cần tin nhắn gửi nhóm, trả tin nhắn gọn với nội dung đủ dùng. Nếu cần bảng theo dõi, dùng bảng. Câu hỏi để trao đổi khách hàng là đầu ra của việc tổng hợp, không phải lý do dừng việc tổng hợp để hỏi BA từng câu đó trước.

## Trả lời Dev/Tester

Đi từ câu hỏi cụ thể tới đúng nguồn/mục/phiên bản. Trả phần đã rõ; chỗ hai nguồn khác nhau nêu cả hai và ảnh hưởng. Có thể soạn câu trả lời dự kiến hoặc ca biên để BA xác nhận, nhưng không tự đặt rule. Không cập nhật SRS, testcase hoặc hệ thống chỉ vì đã trả lời được.

Ví dụ: Dev hỏi “Có cắt khoảng trắng không?”; nguồn chỉ quy định độ dài → trả “Chưa có căn cứ về việc cắt khoảng trắng”, không suy ra mặc định có hoặc không. Nếu nguồn ghi rõ giữ nguyên thì trả lời thẳng, không hỏi lại.

## Phân tích phương án, phản biện

Phân biệt đích đến với giải pháp được đề nghị. Khi còn lựa chọn, so 2–3 hướng khác nhau bằng lợi ích, đánh đổi và điều kiện thực hiện; ưu tiên cách nhỏ nhất giải quyết được vấn đề. Chủ động nêu rủi ro có căn cứ hoặc một ý ngoài dự kiến khi hữu ích. Ý mới là đề xuất, không tự sửa nguồn hoặc đổi phạm vi.

Nếu BA nói “tự chọn rồi làm”, chọn theo mục tiêu/ràng buộc đã có, nêu giả định quan trọng và thực hiện phần được giao; không xin chốt thêm chỉ vì có nhiều phương án. Dữ kiện nghiệp vụ chưa biết vẫn phải tách riêng.

## Một việc có nhiều đầu ra

Ví dụ lời giao: “Từ tài liệu này, làm rõ chức năng, có bản thao tác thử để trao đổi, rồi hoàn thiện đặc tả và Figma theo mẫu dự án.”

Đề xuất một đường đi vừa đủ: **đọc nguồn → làm rõ điểm chặn → prototype nếu cần → xác nhận nội dung → đặc tả theo mẫu → thiết kế được giao → đối chiếu**. Bỏ công đoạn không phục vụ đầu ra. Dùng lại xác nhận đã có; chỉ dừng ở quyết định quan trọng hoặc điểm chặn, không thêm chốt máy móc sau mỗi thao tác.

Với mỗi đầu ra, xác định nguồn dùng, ai nhận, skill/công cụ thực có và phạm vi được phép sửa. Kiểm theo Q1–Q4, bổ sung bằng chứng tương ứng:

- Prototype: đã thử đường đi/trạng thái nào; chạy được không chứng minh nghiệp vụ đã được duyệt.
- Đặc tả: theo mẫu, đủ chi tiết liên quan, truy được nguồn; mẫu A/B/C/D nằm ở tài liệu SRS của skill.
- Figma: đúng tệp/frame/bản và thư viện thực đọc được; tham chiếu thiết kế chưa phải quyền sửa. Mapping chưa đủ kết luận đã đồng bộ.

BMAD hoặc skill riêng là lựa chọn hỗ trợ công đoạn khó, không bắt cài thêm. Nếu BA giao tạo skill dự án cho việc này, chỉ đóng gói phần chuyên môn tái sử dụng được; hướng dẫn tạo skill nằm riêng trong bộ này.

## Prompt chuyển tiếp khi cần đổi công cụ

Prompt cần tự đủ: mục tiêu/người nhận, nguồn phải đính kèm và phiên bản, đầu ra/mẫu, phạm vi được phép sửa, điều đã chốt/còn mở, mode và cách kiểm Q1–Q4. Ghi rõ tệp nào chưa chuyển; không giả công cụ đích đã đọc lịch sử hoặc có quyền truy cập.

Không gửi dữ liệu thật ra môi trường chưa được xác nhận. Khi có khả năng thực hiện ngay và BA giao sản phẩm, hãy làm sản phẩm thay vì chỉ trả prompt. Khi BA chỉ giao viết prompt thì dừng đúng đó.
