# BA Advisor Team v1.1.2 — bắt đầu và dùng ngay

Giao việc BA bằng tiếng Việt. **ba-advisor** hỗ trợ phân tích, hỏi thiếu, phản biện, gợi ý cách làm và tạo prompt/checklist; **ba-srs** xử lý SRS chuyên sâu. Không cần học BMAD hoặc tạo context trước mọi task.

Khi nhận việc, AI sẽ nói ngắn mình hiểu gì, đầu ra dự kiến và cách làm đề xuất. Việc rõ thì làm ngay; chỉ đưa options khi có nhiều hướng hoặc đánh đổi đáng kể.

## 1. Nạp một lần

Chọn **một** cách trong phiên:

- **Chat có đọc tệp:** gửi [BA-ADVISOR-CHAT.md](chat/BA-ADVISOR-CHAT.md) cùng nguồn công việc; làm SRS thì gửi thêm [BA-SRS-CHAT.md](chat/BA-SRS-CHAT.md). Nếu không nhận Markdown, mở tệp và dán nội dung có tên rõ.
- **Công cụ có skill:** chép nguyên hai thư mục trong `skills/` vào dự án: Codex/Antigravity dùng `.agents/skills/`; Claude Code dùng `.claude/skills/`. Mở đúng dự án và bắt đầu phiên mới.

Đừng gửi cả bản gộp và các tệp chỉ dẫn gốc nếu đã nạp đúng. Không đọc được nguồn thì gửi đoạn văn/ảnh/bản xuất có thể đọc, không chỉ đường dẫn trên máy.

## 2. Giao một việc cụ thể

```text
Dùng ba-advisor. Tôi cần [việc và đầu ra].
Nguồn tôi gửi: [tệp/đoạn mô tả/ảnh].
Chỉ làm trong phạm vi [phạm vi]. Thiếu gì ảnh hưởng kết quả thì hỏi.
Kèm cách kiểm Q1–Q4; nếu là SRS/Delta đầy đủ thì trả một bảng kiểm.
```

Ví dụ: “Đọc biên bản này, tách yêu cầu, quyết định và câu hỏi còn mở; chưa viết SRS.”

| Bạn muốn | Cách nói |
|---|---|
| Rõ thì làm, ít hỏi | Không ghi mode hoặc ghi mode 1 |
| Cân nhắc hướng trước | mode 2 — đưa lựa chọn rồi chờ tôi chọn |
| Xem/chỉnh từng phần | mode 3 — làm từng phần rồi chờ tôi |

Phản hồi tiếp theo giữ mode. Với SRS, chỉ mode 3 mặc định đi từng phần **Tóm tắt → Giao diện → Trường thông tin → Tình huống sử dụng**. Nói “chỉnh phần này: …” để sửa đúng chỗ; chốt công đoạn không phải duyệt nghiệp vụ.

## 3. Kiểm kết quả bằng bốn câu hỏi

| Tiêu chí chung | BA kiểm gì? |
|---|---|
| Q1 — Đúng nguồn/phạm vi | Câu này dựa vào đâu, có tự thêm yêu cầu không? |
| Q2 — Đủ và rõ phần thiếu | Có bỏ sót hoặc ghi N/A cho điều chưa biết không? |
| Q3 — Nhất quán | Tên, hình, bảng, rule và luồng có khớp không? |
| Q4 — Dùng/kiểm được | Người nhận biết phải làm gì và kết quả cần kiểm không? |

Kết luận **Đạt / Cần sửa / Chưa đủ căn cứ** phải có vị trí hoặc ví dụ. Việc nhỏ chỉ cần vài dòng; đặc tả/review có một bảng kiểm. AI tự kiểm không thay BA xác nhận. Đặc tả rõ không chứng minh phần mềm đã chạy đúng.

## 4. Lưu và tiếp tục

```text
Lưu kết quả và ghi chú để phiên sau tiếp tục:
việc/mode, bản hiện hành và trạng thái, nguồn/phiên bản,
quyết định có căn cứ, câu hỏi còn mở và bước sau.
```

Phiên mới gửi ghi chú, bản nền và nguồn liên quan; với chat gửi lại bản gộp skill. Không ghi file được thì tự lưu nội dung AI trả. Ba trạng thái giữ nguyên: **DRAFT** (đang soạn), **READY_FOR_REVIEW** (chờ BA rà soát), **APPROVED** (có xác nhận thực gắn người, ngày và phiên bản).

## Tra nhanh khi cần

| Việc | Câu giao việc |
|---|---|
| SRS một màn hình | “Dùng ba-srs đặc tả [màn hình] từ [nguồn], theo mẫu tôi gửi; chưa có thiết kế thì dùng mockup đề xuất. Kèm một bảng kiểm Q1–Q4.” |
| Cập nhật | “Cập nhật [bản nền/phiên bản] theo [thay đổi]. Tạo Delta, chỉ phần bị tác động, giữ bản nền; kiểm ảnh hưởng liên quan.” |
| Review | “Rà soát [tài liệu] theo [nguồn]. Chỉ báo lỗi có vị trí/căn cứ và cách xử lý, chưa sửa.” |
| Chuyển công cụ | “Chỉ tạo prompt cho [việc/công cụ], kèm nguồn phải gửi, đầu ra và cách kiểm; chưa thực hiện nghiệp vụ.” |
| Dùng chung context | “Thiết lập/cập nhật context dự án từ [nguồn] để team dùng chung.” |

**Delta** là phần thay đổi so với bản nền: vẫn đủ sáu mục nhưng không chép lại phần không đổi. **OQ/CF** là câu hỏi/điểm mâu thuẫn còn mở. **Context Owner** là người phụ trách context; ngày rà soát chỉ có khi được chốt, không tự đặt lịch. Những mục này không là thủ tục bắt đầu cho task nhỏ.

BMAD chỉ được đề xuất khi giúp giải quyết phạm vi rộng hoặc vấn đề khó, không chạy tự động và không bắt cài để dùng hai skill.

### Khi chưa nhận đúng skill

Gửi: “Chỉ kiểm nạp ba-advisor và ba-srs, báo phiên bản và tài nguyên thiếu; chưa làm nghiệp vụ.” Bản này phải là **v1.1.2 / BA-CORE-1.1.2**. Xem thao tác đọc tệp nếu công cụ hiển thị; câu “sẵn sàng” chưa đủ bằng chứng.

Cách gọi trực tiếp: Codex `$ba-advisor`/`$ba-srs`; Claude Code `/ba-advisor`/`/ba-srs`; Antigravity dùng tên skill hoặc đường dẫn SKILL.md nếu cần. Đường dẫn nạp dựa trên [OpenAI](https://learn.chatgpt.com/docs/build-skills), [Claude Code](https://code.claude.com/docs/en/skills), [Antigravity](https://antigravity.google/docs/skills); vẫn cần kiểm trên máy/tài khoản người nhận.

Nếu AI hỏi setup lại hoặc hai skill cùng hỏi: giữ bản nền/câu trả lời đã có, kiểm có bản skill cũ nạp song song không. Thiếu hình/trường trong SRS thì yêu cầu hoàn thiện đúng phần, không chấp nhận tóm tắt thay đặc tả.

Nếu thiếu bảng kiểm cuối SRS/Delta, nhắc “Chỉ bổ sung một bảng Q1–Q4 có bằng chứng, không viết lại tài liệu”. Lời giao việc ngắn có thể chưa tạo đúng phần kiểm trong một số cấu hình; dùng câu yêu cầu rõ trong prompt ở bước 2.

### Nhìn nhanh độ chắc chắn và cải tiến skill

Ở nội dung quan trọng, AI có thể ghi **Đã có căn cứ**, **Đề xuất**, **Cần xác nhận** hoặc **Mâu thuẫn**. Đây là tín hiệu để BA biết phần nào dùng được ngay; vẫn phải xem nguồn và quyết định nghiệp vụ.

Khi BA sửa một lỗi, trước hết sửa output. Nếu cùng lỗi lặp lại, ghi nhận lỗi thuộc nguồn, workflow, mẫu hay cách kiểm rồi mới đề nghị cập nhật skill và thêm một ca thử nhỏ. Không biến một trường hợp riêng thành quy tắc chung.

## Dành cho người hướng dẫn và quản lý gói

- **Nâng phiên bản:** lưu hai thư mục skill cũ ngoài nơi tự nạp rồi thay bằng bản mới; không xóa skill khác hoặc chuyển định dạng hồ sơ dự án. Từ v1.0, ba-project-setup đã được gộp vào ba-advisor.
- **Quản lý:** team dùng một phiên bản. Người giữ gói sửa lõi một nơi, đồng bộ hai BA-CORE và tạo lại hai bản gộp trước phát hành. BA dùng không phải tự sửa tài nguyên.
- **Demo:** dùng [nguồn một màn hình](demo/01-INPUT.md), chưa gửi đáp án vào phiên tạo mới. [Trang xem demo](demo/XEM-DEMO.html) là bài tham khảo offline, không chạy AI; [đáp án và ca thử](demo/04-DAP-AN-VA-CA-THU.md) dành cho người hướng dẫn.
- **Chia sẻ 40 phút:** vấn đề thực tế 4 phút → cách nạp 5 → demo/review 12 → BA thử và kiểm chéo 10 → đối chiếu 6 → chọn việc thật/hỏi đáp 3. Bản 30 phút rút còn 3/4/9/8/4/2; bản 45 phút thêm 5 phút thực hành. Đây là mốc dự kiến, chưa đo qua diễn tập.
- **Đánh giá:** nếu so trước/sau, giữ cùng nguồn, câu giao việc và cấu hình; lưu cả hai output, không chọn riêng lần trước tệ nhất. Cho BA kiểm chéo bằng Q1–Q4. Demo giả lập chưa thay cho một việc thật sau buổi.
- **Trong ZIP:** `skills/` là bản cài, `chat/` là bản gộp, `demo/` là vật liệu luyện tập. Không cần đọc hết các thư mục để bắt đầu.
