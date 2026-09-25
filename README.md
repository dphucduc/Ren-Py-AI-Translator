# RenPyVN Studio 2.4.2

**Công cụ hỗ trợ dịch game Ren’Py sang tiếng Việt** trên Windows, có hồ sơ nhân vật, quy tắc xưng hô theo người nói → người nghe, glossary và AI kiểm duyệt bản dịch. Bạn cần tự cung cấp API/model hoặc dùng Ollama; phần mềm không cung cấp sẵn tài khoản AI.

## Cài đặt và bắt đầu

1. Tải **file ZIP ứng dụng Windows** trong mục **Releases** (không chọn “Source code” nếu chỉ muốn dùng app), rồi giải nén **toàn bộ**.
2. Chạy `RenPyVN_Studio.exe`. Giữ nguyên các thư mục đi kèm; đừng chỉ chép riêng EXE.
3. Tạo/mở project, chọn game hoặc script cần dịch. Nên sao lưu game trước khi ghi bản dịch vào game.

## 01 · Nguồn & giải nén

- **+ Chọn file .rpy** hoặc **+ Chọn thư mục** để nạp script. Bảng hiển thị số câu, số câu đã dịch và cảnh báo.
- Nếu game chỉ có `.rpa`/`.rpyc`, dùng **Chọn RPA / RPYC lẻ** hoặc **Chọn thư mục RPA / RPYC** để giải nén/chuyển đổi. Có tùy chọn **Chỉ giải nén script (nhanh)**.
- **Xem cảnh báo quét** để kiểm tra các đoạn không đọc được. Nếu có script trùng sau khi giải nén, dùng **Sửa trùng script** trước khi dịch.

## 02 · Kết nối AI

1. Chọn nhà cung cấp, điền API endpoint/key nếu cần rồi **Quét model** và chọn model.
2. Điều chỉnh số luồng, khoảng nghỉ giữa request và số lượt thử theo hạn mức nhà cung cấp; bấm **Lưu cấu hình**.
3. Có thể bật **Scoped Rules** để chỉ gửi hồ sơ/xưng hô/glossary liên quan, và **Transport V2** cho bước dịch theo ID.
4. **Smart Translation QA:** bật *AI kiểm duyệt độc lập* để có lượt kiểm tra sau khi dịch; bật *Tự sửa có kiểm chứng* và đặt số lượt sửa (0–3) nếu muốn AI thử sửa lỗi. Chức năng này dùng thêm request/token.

> API key là của riêng bạn. Không đưa key hoặc dữ liệu project vào issue công khai trên GitHub.

## 03 · Xưng hô & Glossary

- **Tạo Prompt AI ngoài:** xuất gói script và thông tin hiện có để gửi cho AI ngoài phân tích. Sau khi AI trả JSON, bấm **Nhập JSON AI**; chức năng tạo prompt **không tự chạy AI**.
- **Hồ sơ nhân vật:** kiểm tra tên, tính cách, quan hệ và phong cách nói. **Đại từ nội tâm / nói một mình** được cấu hình riêng, không lấy bừa cặp hội thoại để thay thế.
- Bảng **Xưng hô theo chiều người nói → người nghe** cho phép thêm/sửa/xóa cặp, đặt phạm vi label và khóa. Gõ vào **Tìm theo cặp** để lọc theo tên/mã hoặc chiều `MC → Jess`; **Xóa tìm** để hiện lại toàn bộ.
- **Cảnh báo xưng hô:** nếu JSON đề xuất đổi đại từ của cặp đã có, tool giữ rule đang dùng và chờ bạn chọn **Giữ cũ / Áp dụng**, không tự ghi đè. Kiểm tra cảnh báo sau mỗi lần nhập JSON mới.
- **Glossary bắt buộc:** thêm thuật ngữ và bản dịch cần thống nhất. **Prompt UPDATE script mới** dùng khi game ra tập/phiên bản tiếp theo; xuất gói phân tích mới rồi nhập JSON trả về để bổ sung thông tin.

## 04 · Dịch & duyệt

1. Bấm **Bắt đầu / dịch tiếp**. Có thể **Tạm dừng** hoặc **Dừng & lưu** khi cần.
2. Chọn câu trong bảng để xem nguồn, người nói → người nghe, bản dịch và trạng thái. Sửa bản dịch ở ô bên phải rồi **Lưu sửa** / **Duyệt câu**; có thể **Dịch lại**.
3. **AI rà & tự sửa bản dịch** giúp kiểm tra thêm bản dịch đã có; các câu chưa chắc chắn vẫn cần bạn duyệt. **Rà xưng hô bản dịch** nằm ở Mục 03.
4. Sau khi kiểm tra, dùng **Duyệt các câu đã chọn** hoặc **Duyệt tất cả**. Chỉ duyệt hàng loạt khi đã xem nội dung; AI có thể nhầm ngữ cảnh và đại từ.
5. **Xuất bản nháp** để lấy file dịch riêng. **Ghi vào game + .bak** để ghi vào game và tạo bản sao lưu; đóng game trước khi ghi, thử chạy game sau khi xuất.

## Lưu ý

- Công cụ hướng đến thoại, lời dẫn và menu; giữ cấu trúc mã Ren’Py, biến như `[player_name]` và tag như `{i}`. Vẫn nên kiểm tra script và chạy thử game sau khi dịch.
- Nếu gặp lỗi, gửi **phiên bản app, bước thao tác, thông báo lỗi và đoạn script mẫu đã ẩn thông tin riêng**. Đừng gửi API key hoặc cả thư mục game có bản quyền lên issue công khai.
