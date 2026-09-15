# Thay đổi và rà soát SRS — v1.1.2

Áp dụng cách hỏi, Q1–Q4, kết luận, trạng thái và bàn giao trong BA-CORE. Tệp này chỉ bổ sung cách kiểm SRS và cách làm Update.

## Rà soát SRS

Đối chiếu hai chiều nguồn ↔ mệnh đề, gồm tiền điều kiện, thông báo và vị trí UI. So hình/bảng/luồng theo UI-ID; so rule/AC và nhánh hợp lệ, không hợp lệ, biên liên quan. Điều kiện chưa có nguồn vẫn là OQ, không tự thiết kế để làm tài liệu có vẻ đủ.

Với phần lỗi đã nêu, dẫn một lần tới phát hiện ở bảng Q; không kể lại cả lỗi trong phần kết luận. Nếu BA hoãn điểm không chặn, giữ người/bước xử lý và tình trạng thật của điểm đó. Review một phần không tự đổi trạng thái toàn bản nền.

## Update và Change Impact

1. Đọc đúng bản nền/phiên bản và CR; xác định nguồn nào có hiệu lực ở phần thay đổi.
2. Áp dụng thay đổi trong phạm vi, giữ ID, bản cũ và phần không ảnh hưởng. Khi hợp nhất, kiểm cả dẫn nguồn tại chỗ, bảng nguồn, metadata bản mới và ghi chú tiếp tục; không chỉ thay nhãn.
3. Kiểm nội bộ các nhóm: tài liệu/context/nguồn UI; màn hình/luồng; trường/dữ liệu; rule/AC/tình huống; API/tích hợp; quyền; kiểm thử. Chỉ sửa tài sản ngoài SRS khi được giao riêng.

Giữ sáu mục Delta trong srs-format, nhưng không dùng sáu mục để kể lại sáu lần một thay đổi:

- Mục 1 chỉ ghi bản nền, thay đổi/nguồn, phiên bản và trạng thái cần thiết; không chép lịch sử thao tác công cụ.
- Mục 2 là chỉ mục thay đổi: một dòng cho một thay đổi độc lập; gom các vị trí cùng thay đổi. Không chép nguyên đoạn đặc tả sẽ có ở mục 3.
- Mục 3 chứa đoạn/dòng thay thế đủ để áp dụng, theo A/B/C/D liên quan; giữ hình và bảng theo mẫu khi bị tác động. Phần không đổi dẫn bản nền một lần, không chép lại rule/luồng/OQ không đổi.
- Mục 4 nêu nhóm thực sự bị ảnh hưởng và phần chưa xác định. Các nhóm đã kiểm có cùng kết luận/cùng việc tiếp theo có thể gộp; phần không thấy ảnh hưởng chỉ cần một dòng nêu nhóm, phạm vi đã kiểm và căn cứ. Không bắt mỗi nhóm một bảng hoặc một đoạn.
- Mục 5 chỉ liệt kê OQ/CF mới hoặc bị tác động; OQ/CF cũ không đổi dẫn tới bản nền.
- Mục 6 dùng duy nhất bảng Q1–Q4, dẫn mục 2–5 thay vì viết lại nội dung. Không thêm đoạn kết luận lặp sau bảng.

| Hạng mục | Vị trí/tài liệu đã xem | Kết luận | Căn cứ/việc tiếp theo |
|---|---|---|---|

Kết luận ảnh hưởng giữ: **Bị ảnh hưởng / Không thấy ảnh hưởng trong phạm vi đã kiểm / Chưa xác định / N/A — lý do có căn cứ**. Thiếu API/test/UX không được gọi là không ảnh hưởng; có thể gom phần chưa có tài liệu nhưng phải nêu tên nhóm và việc cần kiểm. Không bịa ID. Rút số dòng trình bày, không bỏ kiểm phụ thuộc hoặc chi tiết thay đổi.

Nếu hợp nhất trực tiếp, đặt Change Impact ở phần kiểm/bàn giao của mẫu, không thêm mục vào A/B/C/D. Lưu bản mới và ghi chú theo BA-CORE. Context/Owner/lịch rà soát, nếu có, dùng quy tắc trong advisor; không là điều kiện khởi tạo lại SRS.
