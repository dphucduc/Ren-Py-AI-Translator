<div align="center">
  <img src="assets/renpyvn-logo.png" alt="RenPyVN Studio mascot" width="160" />

  # RenPyVN Studio

  **Dịch game Ren’Py bằng AI — hiểu ngữ cảnh, giữ xưng hô, bảo vệ script.**

  <a href="https://github.com/dphucduc/RenPyVN-Downloads/releases"><img alt="Download" src="https://img.shields.io/badge/TẢI_ỨNG_DỤNG-GitHub_Releases-2563eb?style=for-the-badge&logo=github&logoColor=white"></a>
  <br />
  <img alt="Version" src="https://img.shields.io/badge/Phiên_bản-2.5.5-f97316?style=flat-square">
  <img alt="Platform" src="https://img.shields.io/badge/Windows-x64-0078d4?style=flat-square&logo=windows&logoColor=white">
  <img alt="Ren'Py" src="https://img.shields.io/badge/Ren'Py-Localization-e11d48?style=flat-square">
  <img alt="Languages" src="https://img.shields.io/badge/Dịch_đa_ngôn_ngữ-AI-16a34a?style=flat-square">

  [**Tải bản mới nhất**](https://github.com/dphucduc/RenPyVN-Downloads/releases/latest) · [**Bắt đầu**](#-bắt-đầu-nhanh) · [**Hướng dẫn**](#-hướng-dẫn-4-mục) · [**Lưu-ý**](#-lưu-ý-quan-trọng)
</div>

---

> [!IMPORTANT]
> **RenPyVN Studio không cung cấp sẵn API key, tài khoản hay hạn mức AI.** Bạn tự cấu hình dịch vụ AI tương thích hoặc model Ollama trên máy. Nên sao lưu game trước khi ghi bản dịch.

## ✨ Tính năng nổi bật

| 🌍 Đa ngôn ngữ | 🧠 Phân tích ngữ cảnh | 💬 Xưng hô & thuật ngữ | 🛡️ Dịch & kiểm tra |
|:---|:---|:---|:---|
| Chọn ngôn ngữ nguồn/đích; có nhận diện nguồn tự động. | AI phân tích nhân vật, người nói → người nghe và bối cảnh. | Hồ sơ nhân vật, cặp xưng hô có khóa và Glossary. | Dịch theo lô, tiếp tục tiến độ, rà lỗi và duyệt trước khi xuất. |

Công cụ dành cho **thoại, lời dẫn và menu** trong game Ren’Py; cố gắng giữ cấu trúc script, biến như `[mc]` và tag như `{i}...{/i}`. Chất lượng dịch phụ thuộc model, dữ liệu ngữ cảnh và việc người dùng rà soát.

## 🚀 Bắt đầu nhanh

1. Vào **[Releases](https://github.com/dphucduc/RenPyVN-Downloads/releases)**, tải gói **`Windows_x64_BINARY_ONLY.zip`** của phiên bản bạn muốn dùng. Không cần chọn mục *Source code*.
2. **Giải nén toàn bộ** ZIP ra một thư mục. Mở `RenPyVN_Studio.exe` bên trong; không chạy trực tiếp từ ZIP và không tách riêng EXE khỏi các file đi kèm.
3. Chọn file `.rpy`/thư mục game → chọn **ngôn ngữ nguồn và đích** → kết nối AI → phân tích, dịch và duyệt.

**Nền tảng:** Windows 64-bit. AI trực tuyến cần kết nối mạng; Ollama cần được cài và chạy riêng nếu sử dụng model cục bộ.

## 🧩 Hướng dẫn 4 mục

### `01` · 📂 Nguồn & giải nén

- Nạp **file `.rpy`** hoặc quét **thư mục game**.
- Dùng công cụ RPA/RPYC nếu script chưa có ở dạng `.rpy`; xem cảnh báo quét và kiểm tra file trùng trước khi dịch.

### `02` · 🤖 Kết nối AI & ngôn ngữ

- Chọn **ngôn ngữ nguồn** (hoặc *Tự động nhận diện*) và **ngôn ngữ đích**.
- Cấu hình nhà cung cấp, endpoint/API key nếu cần, quét/chọn model; chỉnh số luồng, khoảng nghỉ và lượt thử theo hạn mức.
- **QA nội dung/xưng hô là tùy chọn**; Smart Translation QA có thể gọi AI để kiểm tra/sửa bổ sung và sẽ dùng thêm token. Kiểm tra kỹ thuật để bảo vệ cấu trúc Ren’Py là phần riêng.

### `03` · 🗣️ Nhân vật, xưng hô & Glossary

- **AI phân tích toàn bộ trong app** hoặc **phân tích tiếp câu chưa xử lý** bằng model đã kết nối.
- Có thể dùng **Prompt AI ngoài → nhập JSON** khi muốn phân tích bằng công cụ AI khác. Các thay đổi xưng hô có thể được xem trong **Cảnh báo xưng hô** trước khi áp dụng.
- Quản lý hồ sơ nhân vật, cách tự xưng/gọi đối phương theo chiều **người nói → người nghe**, quy tắc **LOCKED**, đại từ nội tâm và thuật ngữ trong **Glossary**.
- **Rà xưng hô bản dịch** để tìm câu lệch quy tắc; nút **AI tự sửa** dùng model đã cấu hình cho các câu được phát hiện, không phải thay chữ hàng loạt. Hãy xem lại bản sửa trước khi duyệt.
- **Mới ở 2.5.5:** kéo giãn bảng/cột, thay đổi chiều cao, ẩn/hiện Glossary, bối cảnh và công cụ phân tích; giao diện ghi nhớ cách bố trí của bạn.

### `04` · ✍️ Dịch, duyệt & xuất

1. Bấm **Bắt đầu / dịch tiếp**, theo dõi trạng thái; tạm dừng khi cần.
2. Xem câu gốc, bản dịch, người nói/nghe; **Lưu sửa**, **Dịch lại** hoặc **Duyệt câu**.
3. Rà lại bản dịch và xưng hô trước khi dùng **Duyệt tất cả**.
4. **Xuất bản nháp** để xem riêng, hoặc **Ghi vào game + `.bak`** để tạo bản sao lưu khi ghi. Đóng game và thử chạy lại sau khi xuất.

## 🔄 Có gì mới ở 2.5.5?

Bảng xưng hô tại Mục 03 rộng hơn và **tùy chỉnh theo ý người dùng**: kéo thanh chia ngang/dọc, kéo rộng cột, ẩn những khung chưa cần và lưu bố cục cho lần mở sau. Bản này tập trung vào **giao diện**, không thay đổi quy tắc AI/QA hay dữ liệu project.

## 🔐 Lưu ý quan trọng

- **Không chia sẻ API key** trong issue, ảnh chụp màn hình hay file cấu hình công khai.
- Văn bản gửi đến dịch vụ AI bạn chọn có thể được xử lý theo chính sách của nhà cung cấp đó.
- Nếu Windows Security chặn file, kiểm tra **Protection history** và tên phát hiện trước khi khôi phục; không cần tắt Defender toàn hệ thống.
- Bản dịch AI có thể sai ngữ cảnh hoặc xưng hô; nên kiểm tra và chạy thử game trước khi phát hành bản Việt hóa.
- Đây là công cụ độc lập, không liên kết chính thức với Ren’Py hay các nhà cung cấp AI. Xem giấy phép đi kèm bản phát hành.

<div align="center">

---

**Made for Ren’Py localization · RenPyVN Studio 2.5.5** 💙

*Kho tải công khai chỉ dành cho bản ứng dụng đã đóng gói; mã nguồn dự án không được phát hành tại đây.*

</div>
