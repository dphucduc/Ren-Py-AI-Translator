# RenPyVN Studio 2.4.2 — Pair Search

Bản vá nhỏ cho **RenPyVN Studio 2.4.1 – PronounConflictReview** (Windows x64).

## Cài đặt
1. Đóng RenPyVN. Trên repository GitHub, chọn **Code → Download ZIP** rồi giải nén.
2. Chép thư mục `downloads` vừa giải nén vào thư mục chứa `RenPyVN_Studio.exe` và `runtime`.
3. Chạy `downloads\UPDATE_241_TO_242.bat`. Chương trình sẽ báo `RenPyVN Studio 2.4.2 installed` nếu thành công.
4. Mở lại ứng dụng. Vào **03 Xưng hô & glossary** → ngay trên bảng xưng hô có **Tìm theo cặp**.

Có thể tải riêng `REN242_INSTALL.py`, đặt trong thư mục ứng dụng và chạy bằng `runtime\python.exe REN242_INSTALL.py`.

## Tìm kiếm
- Gõ `Jess` để tìm mọi cặp liên quan Jess.
- Gõ `MC → Lily` để tìm theo đúng chiều; `Lily → MC` là cặp riêng.
- Có thể gõ mã như `mc -> l`, tên nhân vật và không cần phân biệt hoa/thường hoặc dấu tiếng Việt.
- **Xóa tìm** để hiện lại toàn bộ. Bộ lọc không sửa rule hay dữ liệu nào; Sửa/Xóa dùng chỉ số gốc của cặp.

Bộ cài chỉ nhận phiên bản 2.4.1 nguyên bản theo SHA-256, kiểm tra nội dung mới, sao lưu mã nguồn vào `BACKUP_BEFORE_242_...` trước khi ghi. Không cập nhật các tệp `rules.json`, `progress.sqlite3`, người nghe AI, hoặc script game.

Kiểm thử chọn lọc: 25 đạt, 9 bỏ qua do môi trường; đối chiếu full suite với baseline 2.4.1 không có lỗi test mới (cùng 32 lỗi legacy). Chưa chạy thử GUI Windows thực tế.
