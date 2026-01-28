Hướng dẫn chạy cục bộ (KHÔNG CẦN đăng nhập GitHub)

Yêu cầu:
- Python 3.10+ (hoặc 3.8+)
- Docker (tùy chọn, nếu muốn chạy container)

Chạy trực tiếp trên máy (khuyến nghị):

1. Tạo virtualenv và cài phụ thuộc:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Thiết lập API key cho Gemini (nếu dùng):
- Cách nhanh: xuất biến môi trường `GEMINI_API_KEY`:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

- Hoặc tạo file cấu hình Streamlit `/.streamlit/secrets.toml` với nội dung:

```toml
GEMINI_API_KEY = "your_api_key_here"
```

3. Chạy ứng dụng:

```bash
streamlit run streamlit_app.py
```

Ứng dụng sẽ mở ở `http://localhost:8501`.

Chạy bằng Docker (không cần Python cài sẵn):

1. Xây image:

```bash
docker build -t trolyaothietke:latest .
```

2. Chạy container (thay `YOUR_KEY` bằng giá trị thật, hoặc mount file `secrets.toml`):

```bash
docker run -e GEMINI_API_KEY=YOUR_KEY -p 8501:8501 trolyaothietke:latest
```

Ghi chú:
- Cách trên cho phép người dùng chạy ứng dụng cục bộ mà không cần đăng nhập GitHub hoặc sử dụng dịch vụ hosting yêu cầu GitHub OAuth.
- Nếu không có API key, ứng dụng vẫn có thể chạy nhưng một số chức năng gọi API sẽ báo lỗi; xem `streamlit_app.py` để cấu hình fallback.
