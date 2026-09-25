# Phát hành RenPyVN 2.4.2 có logo, không đăng mã nguồn

**Repo nguồn**: `dphucduc/Ren-Py-AI-Translator` phải giữ PRIVATE. Không đổi repo này thành Public; không upload `RenPyVN_Studio_v2.4.2_WITH_LOGO_PRIVATE.zip`, `*_FULL.zip`, `app.py`, `renpyvn/*.py`, `rules.json`, `progress.sqlite3`, các script game hay API keys vào repo tải về.

## 1. Build riêng trên Windows x64

Lấy ứng dụng đầy đủ 2.4.2 **WITH_LOGO_PRIVATE** trên máy của bạn. Giải nén riêng ở ổ đĩa; kiểm tra cùng thư mục có `RenPyVN_Studio.exe`, `app.py`, `renpyvn`, `assets/app.ico`, `vendor`, `runtime/python.exe`.

Từ thư mục `tools` của repo Private, tải `BUILD_BINARY_ONLY_BRANDED.py` và `BUILD_BINARY_ONLY_BRANDED.cmd`, chép hai file vào thư mục ứng dụng nói trên. Chạy `BUILD_BINARY_ONLY_BRANDED.cmd` (cần Internet để cài Nuitka và compiler). Đừng chạy trong thư mục bản vá nhỏ.

Chỉ khi build thành công mới có:

`_release_binary_only/RenPyVN_Studio_v2.4.2_Windows_x64_BINARY_ONLY.zip`
`_release_binary_only/SHA256SUMS.txt`

Đầu ra đã được quét để chặn file Python, Ren'Py, database và khóa bí mật dạng tệp. EXE native vẫn có thể bị reverse engineer; không có bảo vệ mã tuyệt đối.

## 2. Kiểm tra app trên Windows trước khi công khai

Giải nén ZIP **vừa build**, chạy EXE trong thư mục mới: kiểm tra icon chibi, mở project demo, nhập Rule JSON và xem cảnh báo xưng hô, tìm kiếm theo cặp ở Mục 03, thử dịch với API/Ollama của chính bạn; nếu dùng tính năng decompile, thử bằng script mẫu hợp pháp. Không phát hành nếu có lỗi.

## 3. Tạo repo tải công khai và đăng release tự động

Cài GitHub CLI từ https://cli.github.com/ và mở PowerShell chạy `gh auth login --web` (tự đăng nhập trên trình duyệt; không gửi token cho ChatGPT).

Chép `PUBLISH_BINARY_ONLY.ps1` và `PUBLISH_BINARY_ONLY.cmd` từ `tools` vào **thư mục ứng dụng**, cạnh build CMD. Chạy `PUBLISH_BINARY_ONLY.cmd`, đọc lại thông tin và nhập `PUBLISH` nếu muốn phát hành.

Script sẽ kiểm tra checksum + thành phần ZIP, tạo repo riêng **`dphucduc/RenPyVN-Downloads` Public** (không dùng `--source` hay `--push`), thêm README chỉ chứa hướng dẫn, đăng ZIP + SHA256SUMS dưới tag `v2.4.2`. Nếu repo đã có nhưng không Public, script dừng thay vì thay đổi quyền truy cập.

Sau khi hoàn tất, link cho người dùng là:
https://github.com/dphucduc/RenPyVN-Downloads/releases/latest

GitHub tự tạo các link `Source code (zip/tar.gz)` cho repo tải về; vì repo đó chỉ chứa README, các link này **không** chứa mã nguồn ứng dụng ở repo Private. Người dùng tải asset `*_BINARY_ONLY.zip` trong mục Releases.

**Trạng thái hiện tại**: helper đã có trên repo Private. Chưa biên dịch trên Windows, chưa kiểm tra GUI cuối cùng và **chưa có bản phát hành Public**. Kết nối GitHub ChatGPT hiện không có lệnh tạo repo hay upload Release asset, nên bạn chạy bước 1–3 trên máy; không nên công bố ZIP nguồn thay thế.
