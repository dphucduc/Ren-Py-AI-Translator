RenPyVN Studio 2.5.0 🌐
Công cụ hỗ trợ dịch game Ren’Py bằng AI trên Windows 10/11 (64-bit). Một ứng dụng, nhiều cặp ngôn ngữ: chọn ngôn ngữ nguồn và ngôn ngữ đích ngay trong phần mềm. Công cụ hỗ trợ phân tích nhân vật, quản lý xưng hô/thuật ngữ, dịch theo ngữ cảnh và duyệt trước khi ghi vào game.
Phần mềm không kèm tài khoản hay hạn mức AI. Bạn cần tự cấu hình API/model hoặc sử dụng Ollama trên máy.

📥 Tải và mở ứng dụng
1. Vào mục Releases, tải gói RenPyVN_Studio_v2.5.0_Windows_x64_BINARY_ONLY.zip (không chọn “Source code”).
2. Giải nén toàn bộ ZIP vào một thư mục, sau đó mở RenPyVN_Studio.exe. Không chạy EXE trực tiếp trong ZIP và không tách EXE khỏi các tệp đi kèm.
3. Sao lưu thư mục game trước khi dịch hoặc ghi đè script.
🚀 Hướng dẫn nhanh theo 4 mục
01 · Nguồn & giải nén
Chọn file .rpy hoặc thư mục game để nạp script. Nếu game chỉ có .rpa/.rpyc, dùng công cụ giải nén/chuyển đổi rồi nạp .rpy thu được. Kiểm tra cảnh báo quét và dùng Sửa trùng script khi có xung đột file.
02 · Kết nối AI & ngôn ngữ
- Chọn Ngôn ngữ nguồn (có Tự động nhận diện) và Ngôn ngữ đích, rồi bấm Lưu cấu hình. Project cũ mặc định Anh → Việt. Chất lượng và khả năng nhận diện tùy model.
- Chọn nhà cung cấp AI, nhập Base URL/API key nếu cần, Quét model hoặc nhập model tương thích. Có thể dùng API bên ngoài hay Ollama cài riêng.
- Chỉnh số câu/lần gọi, số luồng, khoảng nghỉ và lượt thử phù hợp hạn mức. Smart Translation QA thêm bước AI kiểm tra và tùy chọn tự sửa có kiểm chứng, nên có thể tốn thêm request/token.
Lưu ý: Hãy chọn cặp ngôn ngữ trước khi phân tích và dịch. Không đổi ngôn ngữ đích giữa chừng trong cùng project đã có bản dịch; nên tạo project mới hoặc sao lưu trước.
03 · Hồ sơ nhân vật, xưng hô & glossary
- Tạo Prompt AI ngoài: xuất các file hướng dẫn/script để AI khác phân tích ngữ cảnh; khi có JSON đúng mẫu, bấm Nhập JSON AI. Tạo prompt không tự gọi AI.
- Kiểm tra Hồ sơ nhân vật, người nói → người nghe, đại từ nội tâm, quan hệ và phong cách nói. Dùng Tìm theo cặp để lọc nhanh.
- Nếu JSON đề xuất đổi đại từ đã có, xem Cảnh báo xưng hô và tự chọn giữ cũ hoặc áp dụng; không mặc định ghi đè rule đang dùng.
- Thêm thuật ngữ ở Glossary để thống nhất cách dịch. Khi game có script mới, dùng Prompt UPDATE script mới để phân tích bổ sung.
Xưng hô tiếng Việt (mình, anh/em, tớ/cậu…) được áp dụng khi ngôn ngữ đích là tiếng Việt. Với ngôn ngữ đích khác, AI cần dùng cách xưng hô phù hợp ngôn ngữ đó; bạn vẫn nên rà lại bản dịch.
04 · Dịch & duyệt
Bấm Bắt đầu / dịch tiếp, có thể tạm dừng và tiếp tục sau. Chọn từng câu để xem nguồn, bản dịch, người nói/nghe và trạng thái; dùng Lưu sửa, Dịch lại, Duyệt câu hoặc Duyệt tất cả sau khi kiểm tra. Có thể dùng AI rà bản dịch và rà xưng hô trước khi xuất.
- Xuất bản nháp: tạo file dịch riêng để kiểm tra.
- Ghi vào game + .bak: ghi bản dịch và tạo bản sao lưu. Đóng game trước khi ghi và mở thử game sau khi xuất.
Công cụ cố gắng giữ nguyên mã Ren’Py, biến như [player_name] và tag như {i}, nhưng bản dịch AI vẫn có thể sai ngữ cảnh hoặc cấu trúc. Luôn kiểm tra và chạy thử game trước khi chia sẻ bản dịch.
🔒 Quyền riêng tư & báo lỗi
Nội dung bạn gửi dịch có thể được chuyển tới nhà cung cấp AI đã chọn. Không công khai API key, dữ liệu project cá nhân hoặc toàn bộ game có bản quyền. Khi báo lỗi, hãy cung cấp phiên bản ứng dụng, bước thao tác, thông báo lỗi và đoạn script mẫu đã ẩn dữ liệu riêng.
Ứng dụng độc lập, không liên kết chính thức với Ren’Py hay các nhà cung cấp AI. Xem LICENSE và THIRD_PARTY_NOTICES.md trong gói phát hành để biết giấy phép và thành phần bên thứ ba.
