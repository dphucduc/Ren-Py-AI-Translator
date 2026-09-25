# RenPyVN Studio 2.4.1 — Khôi phục Cảnh báo xưng hô

Yêu cầu bản gốc: RenPyVN Studio **2.4.0 Smart Translation QA**, bản Windows x64 có `RenPyVN_Studio.exe`, `runtime/python.exe` và thư mục `renpyvn`.

## Cài từ GitHub

1. Đóng ứng dụng. Vào trang repository GitHub, bấm **Code → Download ZIP**.
2. Giải nén, sao chép **nguyên thư mục `downloads`** vào thư mục có `RenPyVN_Studio.exe`.
3. Chạy `downloads/UPDATE_240_TO_241_ONEFILE.bat`, hoặc dùng lệnh `runtime\python.exe downloads\REN241_ONEFILE_INSTALL.py`.
4. Chờ thông báo `RenPyVN 2.4.1 INSTALLED`; sau đó mở lại ứng dụng. Không cần nhập lại dữ liệu trước đó.

Nếu chỉ tải một tệp, lấy `REN241_ONEFILE_INSTALL.py` từ GitHub, đặt cạnh `RenPyVN_Studio.exe`, chạy `runtime\python.exe REN241_ONEFILE_INSTALL.py`.

Bộ cài kiểm tra SHA-256 tất cả mã nguồn trước khi ghi, sao lưu vào `BACKUP_BEFORE_241_...`, dừng nếu là phiên bản khác hoặc code đã sửa thủ công. Bản vá không ghi đè `rules.json`, `progress.sqlite3`, script game. Không chạy khi còn mở ứng dụng.

## Thay đổi

- Khi **Nhập Rule JSON** có cặp người nói/nghe đã tồn tại nhưng AI đổi `self/address`: giữ rule cũ, đưa đề xuất vào **Cảnh báo xưng hô** và tự mở cửa sổ sau khi nhập.
- Cặp mới được thêm bình thường; cập nhật hồ sơ và thông tin không đổi đại từ không tạo cảnh báo giả.
- Chọn **Áp dụng** hoặc **Giữ cũ**; hỗ trợ nhiều PART JSON, đề xuất PART sau cùng cho cùng cặp và scope được giữ.
- Kết quả **người nghe theo từng câu** vẫn theo JSON AI ngoài; không bị bộ cảnh báo xưng hô chặn.
- Giữ Smart Translation QA 2.4.0 và tính năng dịch lại.

Bộ kiểm thử chọn lọc chạy đạt 44 tests, kiểm tra cài đặt trên bản sao 2.4.0 đạt. Chưa thử GUI thật trên Windows/API thật; không thể cam kết tuyệt đối không phát sinh lỗi.
