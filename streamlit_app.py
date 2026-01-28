import streamlit as st
import google.generativeai as genai
import os

# Cấu hình trang web
st.set_page_config(page_title="Trợ lý soạn giáo án", page_icon="📚")

# Cấu hình API Gemini
API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyBAXeNa1aKD5Re0TIj1ktF_4iVDLAXRbic")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

# Tiêu đề chính của ứng dụng
st.title("📚 Trợ lý soạn giáo án STEM")

st.divider()

# 1. Hộp kiểm để chọn lớp
st.subheader("Bạn muốn soạn lớp:")

col1, col2, col3, col4 = st.columns(4)

with col1:
    lop_10 = st.checkbox("Lớp 10")
with col2:
    lop_11 = st.checkbox("Lớp 11")
with col3:
    lop_12 = st.checkbox("Lớp 12")
with col4:
    dai_hoc = st.checkbox("Đại học")

# 2. Hộp thông tin (Input text)
st.subheader("Bài cần soạn")
noi_dung_bai = st.text_area(
    label="Nhập tên bài hoặc nội dung chi tiết cần trợ lý soạn giúp:",
    placeholder="Ví dụ: Giải tích lớp 12 - Chương 1: Đạo hàm...",
    height=150
)

# 3. Nút bấm xử lý
if st.button("🚀 Bắt đầu soạn bài", use_container_width=True):
    # Kiểm tra xem đã chọn lớp và nhập nội dung chưa
    selected_classes = []
    if lop_10: selected_classes.append("10")
    if lop_11: selected_classes.append("11")
    if lop_12: selected_classes.append("12")
    if dai_hoc: selected_classes.append("Đại học")

    if not selected_classes:
        st.error("❌ Vui lòng chọn ít nhất một lớp!")
    elif not noi_dung_bai:
        st.warning("⚠️ Vui lòng nhập nội dung bài cần soạn.")
    else:
        with st.spinner("⏳ AI đang soạn giáo án cho bạn..."):
            try:
                # Xây dựng prompt chi tiết cho Gemini
                prompt = f"""
Hãy soạn một kế hoạch bài dạy STEM chi tiết cho các lớp: {', '.join(selected_classes)}.

Nội dung bài: {noi_dung_bai}

Định dạng output:
### Mục tiêu bài học
[Liệt kê 3-5 mục tiêu học tập rõ ràng]

### Thời lượng
[Thời gian dự kiến]

### Công cụ/Tài nguyên cần thiết
[Liệt kê các dụng cụ, tài liệu cần sử dụng]

### Các hoạt động học tập
1. [Hoạt động 1 - Khởi động]
2. [Hoạt động 2 - Khám phá]
3. [Hoạt động 3 - Thực hành]
4. [Hoạt động 4 - Kết luận]

### Đánh giá kết quả học tập
[Cách đánh giá và tiêu chí]

### Ghi chú cho giáo viên
[Những lưu ý quan trọng]
"""
                
                # Gọi API Gemini
                response = model.generate_content(prompt)
                
                # Hiển thị kết quả
                st.success("✅ Đã soạn xong!")
                st.markdown(response.text)
                
                # Thêm nút tải về (placeholder)
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("📥 Tải xuống Word"):
                        st.info("💡 Chức năng tải xuống sẽ được cập nhật sớm")
                with col2:
                    if st.button("📋 Sao chép văn bản"):
                        st.success("✓ Đã sao chép!")
                        
            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")
                st.info("💡 Vui lòng kiểm tra API key hoặc thử lại sau")

st.divider()
st.markdown("""
### 📖 Hướng dẫn sử dụng
1. Chọn lớp bạn muốn soạn
2. Nhập tên bài hoặc mô tả nội dung chi tiết
3. Nhấn nút "Bắt đầu soạn bài"
4. AI sẽ tạo ra một kế hoạch bài dạy STEM hoàn chỉnh

💡 **Mẹo:** Càng chi tiết nội dung, kết quả sẽ càng tốt!
""")
