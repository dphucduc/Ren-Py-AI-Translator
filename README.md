<div align="center">

# 🌐 RenPyVN Studio

### Dịch game Ren’Py bằng AI — giữ ngữ cảnh, thống nhất nhân vật, dễ kiểm duyệt.

**Một ứng dụng · Nhiều ngôn ngữ · Dành cho Windows**

![Version](https://img.shields.io/badge/Phiên_bản-2.5.0-2563eb?style=for-the-badge)
![Windows](https://img.shields.io/badge/Windows-10%20%2F%2011%20·%2064--bit-0ea5e9?style=for-the-badge&logo=windows)
![Ren'Py](https://img.shields.io/badge/Ren'Py-Localization-e11d48?style=for-the-badge)

**[⬇️ TẢI ỨNG DỤNG](https://github.com/dphucduc/RenPyVN-Downloads/releases)** · **[🚀 BẮT ĐẦU](#-bắt-đầu-trong-3-bước)** · **[🧩 HƯỚNG DẪN](#-hướng-dẫn-các-tính-năng)**

</div>

---

> [!IMPORTANT]
> **RenPyVN Studio không cung cấp sẵn tài khoản, API key hoặc hạn mức AI.** Bạn tự kết nối model/API tương thích hoặc dùng Ollama trên máy. Hãy sao lưu thư mục game trước khi ghi bản dịch.

## ✨ Có gì trong RenPyVN Studio?

| 🌍 Đa ngôn ngữ | 🧠 Hiểu ngữ cảnh | 💬 Xưng hô nhất quán | 🛡️ Kiểm duyệt bản dịch |
|:--|:--|:--|:--|
| Chọn ngôn ngữ nguồn và đích; có tự động nhận diện nguồn. | Phân tích nhân vật, người nói/nghe và ngữ cảnh hội thoại. | Hồ sơ nhân vật, cặp quan hệ và glossary theo project. | Smart Translation QA, dịch lại, duyệt trước khi xuất. |

Công cụ tập trung vào **thoại, lời dẫn và menu** của game Ren’Py, đồng thời cố gắng giữ nguyên code, biến `[player_name]` và các tag như `{i}`. Bản dịch AI vẫn cần được kiểm tra và chạy thử trong game.

## 🚀 Bắt đầu trong 3 bước

1. Mở **[Releases](https://github.com/dphucduc/RenPyVN-Downloads/releases)** và tải file ZIP có chữ `Windows_x64_BINARY_ONLY` — **không chọn “Source code”**.
2. Giải nén **toàn bộ** ZIP, rồi chạy `RenPyVN_Studio.exe`. Giữ nguyên các thư mục và tệp đi kèm EXE.
3. Nạp script/game, chọn ngôn ngữ và kết nối AI để bắt đầu phân tích, dịch và duyệt.

**Yêu cầu:** Windows 10/11 64-bit; kết nối mạng nếu dùng AI trực tuyến, hoặc Ollama đã cài và chạy nếu dùng model cục bộ.

## 🧩 Hướng dẫn các tính năng

### `01` — 📂 Nguồn & giải nén

- **Chọn file `.rpy`** hoặc **chọn thư mục game** để quét script.
- Nếu game có `.rpa` / `.rpyc`, dùng chức năng giải nén / chuyển đổi trước khi nạp script.
- Xem **cảnh báo quét**; dùng **Sửa trùng script** nếu phát hiện tệp trùng/xung đột.

### `02` — 🤖 Kết nối AI & ngôn ngữ

| Thiết lập | Cách dùng |
|:--|:--|
| **Ngôn ngữ nguồn** | Chọn ngôn ngữ gốc hoặc **Tự động nhận diện**. |
| **Ngôn ngữ đích** | Chọn ngôn ngữ muốn xuất bản dịch. |
| **Nhà cung cấp / model** | Nhập endpoint, API key nếu cần; quét hoặc chọn model. |
| **Hiệu năng** | Điều chỉnh số câu/lần gọi, số luồng, khoảng nghỉ và lượt thử theo hạn mức. |
| **Smart Translation QA** | Bật AI kiểm tra độc lập và tùy chọn tự sửa có kiểm chứng. Tốn thêm request/token. |

> [!TIP]
> Chọn **cặp ngôn ngữ trước khi phân tích và dịch**. Project cũ mặc định **Anh → Việt**. Nếu muốn đổi ngôn ngữ đích của project đã dịch, hãy sao lưu hoặc tạo project mới để tránh trộn bản dịch.

**Ví dụ:** `Tiếng Nhật → Tiếng Việt` · `Tiếng Anh → Tiếng Pháp` · `Tự nhận diện → Tiếng Anh`. Chất lượng dịch và nhận diện phụ thuộc vào model AI mà bạn chọn.

### `03` — 🗣️ Hồ sơ nhân vật, xưng hô & Glossary

- **Tạo Prompt AI ngoài:** xuất gói script/ngữ cảnh để gửi cho AI khác; nhận kết quả JSON rồi dùng **Nhập JSON AI**. Thao tác tạo prompt **không tự gọi AI**.
- **Hồ sơ nhân vật:** xem tên, quan hệ, phong cách nói và đại từ nội tâm/nói một mình.
- **Xưng hô theo chiều:** quản lý quy tắc riêng cho `Người nói → Người nghe`, tìm nhanh bằng **Tìm theo cặp**.
- **Cảnh báo xưng hô:** nếu JSON đề xuất đổi đại từ đã có, bạn chọn **Giữ cũ** hoặc **Áp dụng** trước khi thay đổi.
- **Glossary:** khóa thuật ngữ cần dịch thống nhất. Khi có chương/script mới, dùng **Prompt UPDATE script mới** để phân tích bổ sung.

> **Lưu ý ngôn ngữ:** bộ đại từ kiểu **mình / tớ–cậu / anh–em** chỉ áp dụng khi **ngôn ngữ đích là tiếng Việt**. Với ngôn ngữ đích khác, hãy kiểm tra cách xưng hô theo ngôn ngữ đó.

### `04` — ✍️ Dịch, duyệt & xuất

1. Chọn **Bắt đầu / dịch tiếp**; có thể tạm dừng và tiếp tục.
2. Mở từng câu để xem văn bản gốc, bản dịch, người nói/nghe và trạng thái.
3. Dùng **Lưu sửa**, **Dịch lại**, **Duyệt câu**; chỉ **Duyệt tất cả** sau khi đã kiểm tra nội dung.
4. Chạy rà bản dịch/xưng hô nếu cần, rồi chọn cách xuất:

| Cách xuất | Công dụng |
|:--|:--|
| **Xuất bản nháp** | Tạo file dịch riêng để xem lại. |
| **Ghi vào game + `.bak`** | Ghi bản dịch vào game và tạo bản sao lưu. Hãy đóng game trước khi ghi. |

---


</div>
