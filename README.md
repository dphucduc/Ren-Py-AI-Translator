<div align="center">

<img src="assets/renpyvn-logo.png" width="156" alt="RenPyVN Studio – mascot" />

# RenPyVN Studio

**Công cụ dịch game Ren’Py bằng AI • Đa ngôn ngữ • Quản lý nhân vật và xưng hô**

[![Phiên bản](https://img.shields.io/badge/Version-2.5.5-f97316?style=flat-square)](https://github.com/dphucduc/RenPyVN-Downloads/releases)
![Nền tảng](https://img.shields.io/badge/Windows-x64-0078d4?style=flat-square&logo=windows&logoColor=white)
![Ren'Py](https://img.shields.io/badge/Ren'Py-Localization-e11d48?style=flat-square)
![Ngôn ngữ](https://img.shields.io/badge/Multilingual-AI-16a34a?style=flat-square)

[**⬇️ TẢI ỨNG DỤNG**](https://github.com/dphucduc/RenPyVN-Downloads/releases/latest) · [Bắt đầu](#-bắt-đầu-nhanh) · [Prompt AI ngoài](#-hướng-dẫn-prompt-ai-ngoài-từng-bước) · [Hỏi đáp](#-hỏi-đáp--xử-lý-lỗi)

</div>

---

> [!IMPORTANT]
> RenPyVN Studio **không cung cấp sẵn API key, tài khoản hoặc hạn mức AI**. Bạn dùng model/API của mình hoặc kết nối Ollama. Hãy **sao lưu game** trước khi ghi bản dịch vào file gốc.

## ✨ Phần mềm làm được gì?

| Tính năng | Công dụng |
|:--|:--|
| 🌍 **Dịch đa ngôn ngữ** | Chọn ngôn ngữ nguồn (có tự nhận diện) và ngôn ngữ đích trong cùng ứng dụng. |
| 🧠 **Phân tích ngữ cảnh** | Xác định nhân vật, người nói → người nghe, bối cảnh và đề xuất quan hệ/xưng hô. |
| 🗣️ **Xưng hô & Glossary** | Quản lý đại từ theo từng chiều, đại từ nội tâm, thuật ngữ bắt buộc và rule LOCKED. |
| 🤖 **Nhiều cách dùng AI** | Phân tích trực tiếp trong app **hoặc** xuất Prompt dùng với ChatGPT/DeepSeek/Gemini bên ngoài. |
| 🛡️ **Dịch và kiểm tra** | Dịch theo lô, lưu tiến độ, rà xưng hô, AI hỗ trợ sửa và duyệt câu trước khi xuất. |
| 🪟 **Giao diện 2.5.5** | Kéo giãn khung/cột, ẩn hiện phần phụ và ghi nhớ bố cục. |

Phần mềm hướng tới **thoại, lời dẫn và lựa chọn** trong `.rpy`; cố gắng giữ nguyên mã, biến như `[mc]` và tag như `{i}...{/i}`. Hãy kiểm tra bản dịch và chạy thử game sau khi xuất.

## 🚀 Bắt đầu nhanh

1. Mở trang **[Releases](https://github.com/dphucduc/RenPyVN-Downloads/releases)**, tải ZIP `Windows_x64_BINARY_ONLY` của phiên bản cần dùng (không chọn *Source code*).
2. **Giải nén toàn bộ** ZIP, chạy `RenPyVN_Studio.exe`. Không kéo riêng EXE ra ngoài thư mục của nó.
3. Ở **Mục 01**, chọn file `.rpy` hoặc thư mục game. Ở **Mục 02**, chọn ngôn ngữ và kết nối model AI, rồi bấm **Lưu cấu hình**.
4. Ở **Mục 03**, phân tích nhân vật/người nghe bằng **AI trong app** hoặc **Prompt AI ngoài**. Xem hồ sơ, duyệt cặp xưng hô và Glossary.
5. Sang **Mục 04 → Bắt đầu / dịch tiếp**. Kiểm tra kết quả, duyệt câu rồi **Xuất bản nháp** hoặc **Ghi vào game + .bak**.

**Luồng đề xuất:** Nạp script → Chọn ngôn ngữ & AI → Phân tích ngữ cảnh → Duyệt xưng hô → Dịch → Rà/duyệt → Xuất.

## 🧩 Hướng dẫn 4 mục

### `01` · 📂 Nguồn & giải nén

- **+ Chọn file .rpy:** nạp một hoặc nhiều script. **+ Chọn thư mục:** quét thư mục chứa các script cần dịch.
- Game chỉ có `.rpa`/`.rpyc`? Dùng **Chọn RPA / RPYC lẻ** hoặc **Chọn thư mục RPA / RPYC**, chọn nơi xuất, sau đó nạp các `.rpy` đã giải nén.
- Xem **cảnh báo quét** và xử lý script trùng nếu app báo. Quá trình giải nén không tự động biến mọi file thành câu cần dịch.

### `02` · 🤖 Kết nối AI & chọn ngôn ngữ

1. Chọn **ngôn ngữ nguồn** (có thể chọn *Tự động nhận diện*) và **ngôn ngữ đích**. Đặt đúng trước khi phân tích/dịch; không nên đổi ngôn ngữ giữa chừng trong project đã dịch.
2. Chọn nhà cung cấp: **Gemini**, **Ollama** cục bộ hoặc **Custom** cho API tương thích OpenAI (ví dụ gateway bạn tự cấu hình).
3. Điền endpoint/API key nếu nhà cung cấp yêu cầu → **Quét model** → chọn model → **Lưu cấu hình**. Ollama cần chạy riêng và có model đã tải trước.
4. Điều chỉnh số luồng, số câu/lô, khoảng nghỉ, lượt thử cho hợp hạn mức. Gặp 429 thì giảm tốc/luồng thay vì liên tục gửi lại.
5. **QA nội dung/xưng hô** là tùy chọn. **Smart Translation QA** chỉ hoạt động khi bật QA nội dung và có thể dùng thêm request/token; kiểm tra kỹ thuật giữ tag/biến Ren’Py là phần riêng.

> **Lưu ý:** Bản dịch tốt phụ thuộc model và thông tin nhân vật. Nên rà xưng hô sau khi dịch, kể cả khi AI kiểm duyệt đang bật.

### `03` · 🗣️ Hồ sơ nhân vật, xưng hô và Glossary

Khi thanh công cụ bị ẩn trong 2.5.5, bấm **Hiện công cụ phân tích / dịch** trước.

**Hai cách phân tích khác nhau — chỉ cần chọn cách phù hợp:**

| Cách | Khi nào dùng? | Cần làm gì? |
|:--|:--|:--|
| **AI phân tích TOÀN BỘ trong app** | Đã kết nối model ở Mục 02. | Bấm nút, chờ app phân tích trực tiếp; xem kết quả trong hồ sơ và cảnh báo. |
| **Phân tích tiếp câu chưa xử lý** | Đã dừng giữa chừng, còn câu chưa phân tích. | Chỉ chạy phần chưa xử lý; **không tự sửa** câu đã phân tích sai. |
| **Tạo Prompt AI ngoài** | Muốn dùng AI trên web hoặc model ngoài app. | Xuất gói file → gửi AI → nhận file JSON → **Nhập JSON AI**. Xem hướng dẫn đầy đủ bên dưới. |

Sau khi phân tích:

- **Hồ sơ nhân vật:** xem/chỉnh thông tin và cách nói của từng nhân vật; nếu tên hiển thị sai, dùng **Đọc file định danh (.rpy)** để đọc file khai báo `Character(...)` của game.
- **Xưng hô theo chiều người nói → người nghe:** `A → B` và `B → A` là **hai chiều riêng**. Sửa **Tự xưng** / **Gọi đối phương** cho đúng; khóa cặp đã xác nhận.
- **Cảnh báo xưng hô:** khi AI ngoài đề xuất đổi một cặp đang có, rule cũ được giữ để bạn xem và chọn **Áp dụng gợi ý đã chọn** hoặc **Áp dụng TẤT CẢ đề xuất**. Chỉ áp dụng khi đã đối chiếu ngữ cảnh.
- **Đại từ nội tâm / nói một mình:** đặt riêng cho lời tự sự; không lấy cặp đối thoại thay thế.
- **Glossary:** thêm thuật ngữ và bản dịch muốn giữ thống nhất.
- **Rà xưng hô bản dịch:** sau khi đã dịch, rà các câu lệch rule LOCKED. Báo cáo không tự sửa. Nút **AI tự sửa N câu được phát hiện** sẽ **gọi model ở Mục 02 và tốn token**; bản sửa chuyển về *Cần duyệt*. Có thể **Hoàn tác lượt sửa xưng hô** trong các trường hợp được hỗ trợ.

**Giao diện 2.5.5:** kéo tay nắm chia ngang/dọc để bảng xưng hô rộng/cao hơn; kéo mép cột, ẩn Glossary/bối cảnh/công cụ khi không cần. App ghi nhớ bố cục.

## 📦 Hướng dẫn Prompt AI ngoài từng bước

> Đây là bước **AI phân tích ngữ cảnh và xưng hô**, **chưa phải bước dịch game**. Bạn không cần kết nối API trong app nếu chỉ dùng AI web để phân tích.

### Bước 1 — Chuẩn bị project

Nạp `.rpy` ở Mục 01 và chọn ngôn ngữ nguồn/đích ở Mục 02. Mở **Mục 03 → Hiện công cụ phân tích / dịch** (nếu đang thu gọn). Tại ô **Chia Prompt AI ngoài theo dòng script**, chọn thử **150–300 dòng/phần**; đây là *dòng script gốc*, không phải số câu thoại.

### Bước 2 — Xuất gói Prompt

Bấm **Tạo Prompt AI ngoài**, chọn thư mục lưu. App sẽ mở thư mục kết quả và tự copy nội dung `PROMPT.txt` vào clipboard. Thư mục thường có các file sau:

```text
PROMPT.txt             ← Yêu cầu/luật phân tích cho AI
RULE_SCHEMA.json       ← Khuôn JSON AI phải trả về
HOW_TO_USE.txt         ← Hướng dẫn riêng của gói này
PACK_INFO.json         ← Thông tin gói và định danh từng phần
CHARACTER_MAP.json     ← ID nhân vật ↔ tên hiển thị
CURRENT_RULES.json     ← Hồ sơ/rule hiện đang có
SCRIPT_PART_001.txt    ← Phần script thứ nhất
SCRIPT_PART_002.txt    ← Phần script tiếp theo (nếu có)
...
```

> **Quan trọng:** gói của bạn có bao nhiêu `SCRIPT_PART_*.txt` thì xử lý **đủ bấy nhiêu**. Đừng chỉ gửi mỗi `PROMPT.txt`, vì AI cần script và thông tin nhân vật thật để xác định đúng người nghe.

### Bước 3 — Gửi AI bên ngoài

Mở ChatGPT, Gemini hoặc DeepSeek trong **cuộc trò chuyện mới**. Đính kèm **`PROMPT.txt`, `RULE_SCHEMA.json`, `HOW_TO_USE.txt`, `PACK_INFO.json`, `CHARACTER_MAP.json`, `CURRENT_RULES.json` và `SCRIPT_PART_001.txt`**. Nếu nền tảng giới hạn file, gửi các file nền trước rồi gửi từng PART tiếp theo trong cùng cuộc trò chuyện; giữ đúng `PROMPT.txt` làm chỉ dẫn chính.

Bạn có thể dán lời nhắn ngắn này sau khi đính kèm:

```text
Đọc kỹ PROMPT.txt, RULE_SCHEMA.json, HOW_TO_USE.txt và các file đi kèm.
Phân tích SCRIPT_PART_001.txt theo đúng yêu cầu.
Chỉ trả về 1 JSON hợp lệ cho PART_001, không Markdown, không giải thích.
Giữ nguyên part_id, key, file, line, speaker; không bỏ sót TARGET.
```

Với `SCRIPT_PART_002.txt`, tiếp tục yêu cầu AI xử lý **PART_002**, rồi làm tương tự đến hết. `STAGE`/`CONTEXT_ONLY` giúp hiểu cảnh; AI chỉ tạo entry cho dòng `TARGET` theo prompt. Người nghe không rõ thì ghi trạng thái chưa rõ theo schema, **không tự đoán dựa vào người nói ngay trước đó**.

### Bước 4 — Lưu JSON đầu ra

Lưu **mỗi kết quả** thành file riêng, chẳng hạn:

```text
PART_001.json
PART_002.json
PART_003.json
```

Nếu AI đưa văn bản trong khung code, chỉ lấy **nội dung JSON hợp lệ**; không giữ khung Markdown hoặc phần giải thích. Không đổi `part_id` hay ID nhân vật, không tự sửa `key`/`file`/`line`/`speaker`. File output **khác** với `RULE_SCHEMA.json`: schema là khuôn mẫu, không phải kết quả để nhập.

### Bước 5 — Nhập lại vào app

Quay về **đúng project đã tạo gói** → **Mục 03 → Nhập JSON AI** → chọn đồng thời các file `PART_*.json` (giữ `Ctrl` để chọn nhiều file). App hiển thị số entry/cặp xưng hô và yêu cầu bạn xác nhận. Sau khi nhập:

1. Mở **Hồ sơ nhân vật** xem thông tin đã nhận.
2. Mở **Cảnh báo xưng hô** kiểm tra đề xuất thay đổi cặp cũ; **không tự động ghi đè** rule đang dùng.
3. Kiểm tra số câu chưa có entry và các câu AI trả *unknown*; nếu thiếu phần, hoàn tất PART còn lại rồi nhập bổ sung.
4. Sang **Mục 04** mới bắt đầu dịch. **Nhập JSON AI không tự dịch thoại.**

### Khi game ra tập mới — dùng Prompt UPDATE

Mở lại **project cũ**, thêm script mới vào **chính thư mục game đang mở**, rồi bấm **Prompt UPDATE script mới**. Chọn `.rpy` mới, xuất gói và làm lại quy trình gửi AI → lưu `PART_*.json` → **Nhập JSON AI**. UPDATE dùng `CURRENT_RULES` làm nền để bổ sung thông tin; đừng coi nó là nút phân tích lần đầu cho game chưa có dữ liệu.

### Nếu AI không trả đủ hoặc JSON bị lỗi?

- **JSON bị cắt / thiếu phần:** giảm **Chia Prompt AI ngoài theo dòng script** (ví dụ từ 300 xuống 150), tạo gói mới và xử lý lần lượt từng PART; đừng ghép những JSON của hai gói khác nhau.
- **Báo `part_id` không thuộc project / thiếu entry:** mở đúng project và dùng các file kết quả khớp với gói đã tạo. Không tự chế ID để qua lỗi.
- **AI trả quá nhiều `unknown` hoặc `pairs=[]`:** kiểm tra phần bối cảnh và yêu cầu AI đọc lại script thật theo `PROMPT.txt` và `RULE_SCHEMA.json`; số entry đầy đủ không đảm bảo nội dung đã chính xác.
- **Lỡ đổi xưng hô đang LOCKED:** xem **Cảnh báo xưng hô** và chỉ áp dụng cặp mong muốn; hãy sao lưu project trước khi nhập nhiều JSON.

<details>
<summary><b>📌 Ví dụ một lượt sử dụng Prompt AI ngoài</b></summary>

```text
1. Nạp chapter1.rpy vào app.
2. Mục 03 → chia 150 dòng/phần → Tạo Prompt AI ngoài.
3. Gửi các file nền + SCRIPT_PART_001.txt lên AI web.
4. Lưu kết quả của AI thành PART_001.json.
5. Gửi SCRIPT_PART_002.txt → lưu PART_002.json → tiếp tục cho đến hết.
6. Mục 03 → Nhập JSON AI → chọn tất cả PART_*.json.
7. Xem Hồ sơ nhân vật / Cảnh báo xưng hô, duyệt những cặp cần thay.
8. Mục 04 → Bắt đầu / dịch tiếp.
```

</details>

### `04` · ✍️ Dịch, duyệt & xuất

1. Bấm **Bắt đầu / dịch tiếp** để dịch những câu cần xử lý. Dùng **Tạm dừng** hoặc **Dừng & lưu** khi cần; theo dõi nhóm *Cần duyệt*, *Hết lượt thử*, *Chưa dịch / lỗi*.
2. Bấm một câu để xem **Nguồn**, **Người nói → người nghe** và **Bản dịch**. Có thể sửa thủ công, **Lưu sửa**, **Dịch lại** hoặc **Duyệt câu**.
3. Nếu cần, dùng **AI rà & tự sửa bản dịch** (Mục 04) và **Rà xưng hô bản dịch** (Mục 03). Không coi phát hiện tự động là kết luận tuyệt đối; kiểm tra bản sửa trước khi duyệt.
4. **Duyệt các câu đã chọn** hoặc **Duyệt tất cả** sau khi xem chất lượng. **Xuất bản nháp** để kiểm tra riêng; **Ghi vào game + .bak** để ghi vào game kèm bản sao lưu. Đóng game trước khi ghi và chạy thử bản đã dịch.

## ❓ Hỏi đáp & xử lý lỗi

<details>
<summary><b>Người khác tải bản GitHub có thấy project tôi đang làm không?</b></summary>

Không phải chỉ vì app trên máy bạn tự mở lại project cũ. RenPyVN Studio có cơ chế nhớ project của **người đang sử dụng máy đó**. Tuy nhiên, trước khi công bố, người phát hành vẫn cần kiểm tra ZIP không chứa thư mục game, `.renpyvn`, API key hoặc dữ liệu cá nhân.

</details>

<details>
<summary><b>Windows Security tự cách ly/xóa EXE?</b></summary>

Mở **Windows Security → Virus & threat protection → Protection history** để xem tên phát hiện và đường dẫn file. Không tắt Defender toàn hệ thống; nếu nghi nhận diện nhầm, chủ bản phát hành có thể gửi file cho Microsoft phân tích.

</details>

<details>
<summary><b>Đã nhập JSON rồi nhưng xưng hô vẫn sai?</b></summary>

Kiểm tra đúng **người nghe của từng dòng**, **cặp có hướng** `người nói → người nghe`, trạng thái **LOCKED** và những đề xuất trong **Cảnh báo xưng hô**. Người nghe do AI phân tích và đại từ của cặp là hai dữ liệu khác nhau. Những câu đã dịch trước khi sửa rule cần được rà/dịch lại khi cần.

</details>

<details>
<summary><b>Có thể dịch mọi ngôn ngữ không?</b></summary>

Bạn có thể chọn nguồn/đích trong ứng dụng, nhưng chất lượng còn phụ thuộc model và ngôn ngữ thực tế. Bộ quy tắc đại từ tiếng Việt phù hợp nhất khi **ngôn ngữ đích là tiếng Việt**; đừng mặc định các ngôn ngữ khác có cùng cách xưng hô.

</details>

## 🔐 Quyền riêng tư & lưu ý

- **Không đăng API key, file project, gói Prompt chứa script game hoặc JSON riêng** lên issue/repository công khai.
- Nếu dùng API/web AI, nội dung bạn gửi được xử lý theo điều khoản của nhà cung cấp AI bạn chọn.
- Công cụ độc lập, không liên kết chính thức với Ren’Py hay các nhà cung cấp AI. Xem giấy phép đi kèm bản phát hành.
- Trang tải công khai chỉ dành cho **bản chạy đã đóng gói** và tài liệu. Source code của tác giả không nằm trong gói README này.

<div align="center">

---

**RenPyVN Studio 2.5.5** · Made for Ren’Py localization 💙

[⬆️ Về đầu trang](#renpyvn-studio) · [📥 GitHub Releases](https://github.com/dphucduc/RenPyVN-Downloads/releases)

</div>
