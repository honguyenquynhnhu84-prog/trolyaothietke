# 📚 Trợ Lý Soạn Giáo Án STEM - AI Assistant

Ứng dụng hỗ trợ giáo viên soạn giáo án STEM tự động bằng trí tuệ nhân tạo Google Gemini.

## 🎯 Tính năng

✨ **Soạn giáo án tự động** - Nhập tên bài, AI tạo ra kế hoạch chi tiết  
🎓 **Hỗ trợ nhiều lớp** - Lớp 10, 11, 12 và Đại học  
⚡ **Nhanh và dễ dùng** - Giao diện đơn giản, không cần kỹ năng kỹ thuật  
📥 **Xuất file Word** - Tải về Word để chỉnh sửa tiếp  
🔒 **An toàn** - API Key được bảo mật  

## 🚀 Sử dụng Ngay (Không cần cài đặt)

**Truy cập:** https://trolyaothietke.streamlit.app

👉 **Giáo viên chỉ cần click link, không cần đăng nhập gì!**

## 💻 Chạy trên máy cá nhân

### Yêu cầu
- Python 3.8+ 
- pip (trình quản lý package Python)

### Các bước
```bash
# 1. Tạo thư mục làm việc
cd trolyaothietke

# 2. Tạo môi trường ảo (Virtual Environment)
python -m venv .venv
source .venv/bin/activate  # Trên macOS/Linux
# hoặc
.venv\Scripts\activate     # Trên Windows

# 3. Cài đặt thư viện
pip install -r requirements.txt

# 4. Chạy ứng dụng
streamlit run streamlit_app.py

# 5. Truy cập: http://localhost:8501
```

## 📋 Cấu trúc file

```
trolyaothietke/
├── streamlit_app.py        ← Ứng dụng chính
├── requirements.txt        ← Danh sách thư viện
├── .streamlit/
│   ├── config.toml        ← Cấu hình
│   └── secrets.toml       ← API Key (bảo mật)
├── DEPLOY_GUIDE.md        ← Hướng dẫn chi tiết
└── README.md             ← File này
```

## 🔧 Cấu hình API Key

### Local (máy cá nhân)
Tạo file `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your_key_here"
```

### Cloud (Streamlit Cloud)
Vào **Settings** → **Secrets** trong Streamlit Cloud dashboard

## 📖 Hướng dẫn đầy đủ

Xem file [DEPLOY_GUIDE.md](DEPLOY_GUIDE.md) để hướng dẫn chi tiết về:
- Cách deploy lên Streamlit Cloud
- Cách chia sẻ link cho giáo viên
- Cách xử lý lỗi
- Q&A

## 🌐 Tài liệu tham khảo

- [Streamlit Documentation](https://docs.streamlit.io)
- [Google Gemini API](https://ai.google.dev)
- [Python Official](https://python.org)

## 📞 Liên hệ & Hỗ trợ

Gặp vấn đề? Kiểm tra:
1. API Key có đúng không?
2. Thư viện có cài đầy đủ không (`pip install -r requirements.txt`)?
3. Python version có ≥ 3.8 không?

## 📄 Giấy phép

Dự án này được tạo cho mục đích giáo dục.

---

**Phiên bản:** 1.0  
**Cập nhật:** 28/01/2026  
**Tác giả:** AI Assistant
