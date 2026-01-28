# 📚 Trợ lý Soạn Giáo Án STEM - Hướng dẫn Deploy

## 🎯 Mục đích
Ứng dụng hỗ trợ giáo viên soạn giáo án STEM bằng AI (Google Gemini).

## 🚀 Deploy lên Streamlit Cloud (Công khai - Không cần đăng nhập)

### Bước 1: Truy cập Streamlit Cloud
Vào: https://share.streamlit.io/

### Bước 2: Đăng nhập GitHub
- Click **"Sign up / Log in"**
- Click **"Sign in with GitHub"**
- Dùng tài khoản GitHub: `honguyenquynhnhu84-prog`

### Bước 3: Tạo ứng dụng mới
1. Click **"New app"**
2. Điền thông tin:
   - **Repository:** `honguyenquynhnhu84-prog/trolyaothietke`
   - **Branch:** `main`
   - **Main file:** `streamlit_app.py`
3. Click **"Deploy"** (chờ khoảng 2-3 phút)

### Bước 4: Thiết lập API Key an toàn
1. Sau khi deploy xong, vào **Settings** (⚙️ góc phải bên trên)
2. Chọn tab **"Secrets"**
3. Thêm dòng này:
```toml
GEMINI_API_KEY = "AIzaSyBAXeNa1aKD5Re0TIj1ktF_4iVDLAXRbic"
```
4. Click **"Save"** → Ứng dụng sẽ tự restart

### Bước 5: Lấy link chia sẻ
URL sẽ có dạng: **https://trolyaothietke.streamlit.app**

---

## ✨ Ưu điểm
✅ Giáo viên chỉ cần click link, không cần đăng nhập gì  
✅ Hoạt động trên mọi thiết bị (máy tính, điện thoại, tablet)  
✅ Miễn phí hoàn toàn  
✅ Tự động cập nhật khi bạn push code lên GitHub  
✅ API Key được bảo mật (không hiển thị công khai)  

---

## 💻 Chạy cục bộ (Local)
```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Chạy ứng dụng
streamlit run streamlit_app.py

# Truy cập: http://localhost:8501
```

---

## 📝 Cấu trúc thư mục
```
trolyaothietke/
├── streamlit_app.py          ← Ứng dụng chính
├── requirements.txt          ← Dependencies
├── .streamlit/
│   ├── config.toml          ← Cấu hình (local)
│   └── secrets.toml         ← API Key (KHÔNG push lên GitHub)
├── .gitignore               ← File bỏ qua khi commit
└── README.md                ← Hướng dẫn này
```

---

## 🔐 Bảo mật
- **Local:** API Key được lưu trong `.streamlit/secrets.toml`
- **Cloud:** API Key được lưu trong Streamlit Cloud Secrets (mã hóa)
- **GitHub:** File `.streamlit/secrets.toml` trong `.gitignore` (không push lên)

---

## ❓ Câu hỏi thường gặp

**Q: Tại sao cần deploy trên Streamlit Cloud?**  
A: Để giáo viên có thể dùng mà không cần cài Python, không cần máy tính mạnh.

**Q: Giáo viên cần tài khoản gì không?**  
A: Không cần! Chỉ cần truy cập link là xong.

**Q: Chi phí?**  
A: Hoàn toàn miễn phí (Streamlit cấp 3GB memory, 1GB storage free).

**Q: API Key sẽ hết không?**  
A: Google Gemini có quota miễn phí khá lớn, đủ dùng cho giáo viên.

---

## 📞 Hỗ trợ
Nếu gặp vấn đề, hãy kiểm tra:
1. ✅ GitHub repo đã push lên chưa
2. ✅ API Key đã thêm vào Streamlit Cloud Secrets chưa
3. ✅ File `streamlit_app.py` có lỗi syntax không
4. ✅ `requirements.txt` có đầy đủ thư viện không

---

**Ngày tạo:** 28/01/2026  
**Version:** 1.0
