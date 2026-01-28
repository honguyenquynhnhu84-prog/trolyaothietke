import streamlit as st

st.set_page_config(page_title="STEM Lesson Planner 3089", layout="wide")

st.title("🚀 Hệ thống Trợ lý Soạn bài giảng STEM (CV 3089)")
st.caption("Ứng dụng hỗ trợ giáo viên tạo Prompt chuẩn xác cho AI")

with st.sidebar:
    st.header("⚙️ Thông số bài dạy")
    khoi_lop = st.selectbox("Chọn khối lớp", ["Lớp 6", "Lớp 7", "Lớp 8", "Lớp 9"])
    ten_bai = st.text_input("Tên bài dạy STEM", placeholder="VD: Tên lửa nước")
    
    chu_trinh = st.radio("Chu trình dạy học", 
                         ["Quy trình Thiết kế Kỹ thuật (EDP)", "Phương pháp Nghiên cứu Khoa học"])
    
    hoat_dong = st.multiselect("Hoạt động cần soạn", 
                               ["Tất cả", "HĐ 1: Xác định vấn đề", "HĐ 2: Nghiên cứu kiến thức nền", 
                                "HĐ 3: Đề xuất giải pháp", "HĐ 4: Chế tạo/Thử nghiệm", "HĐ 5: Chia sẻ/Thảo luận"],
                               default=["Tất cả"])

# Xử lý Logic tạo Prompt
if st.button("Tạo Prompt cho AI ✨"):
    if not ten_bai:
        st.error("Vui lòng nhập tên bài dạy!")
    else:
        prompt = f"""
        Hành động: Hãy đóng vai một chuyên gia giáo dục STEM xuất sắc.
        Nhiệm vụ: Soạn giáo án bài '{ten_bai}' cho học sinh {khoi_lop}.
        Cấu trúc: Tuân thủ nghiêm ngặt Công văn 3089/BGDĐT-GDTrH.
        Phương pháp: Áp dụng {chu_trinh}.
        Phạm vi: Soạn chi tiết {', '.join(hoat_dong)}.
        
        Yêu cầu kỹ thuật:
        - Mỗi hoạt động phải có 4 bước: Mục tiêu, Nội dung, Sản phẩm, Tổ chức thực hiện.
        - Chú trọng vào việc hình thành năng lực và phẩm chất cho học sinh.
        - Ngôn ngữ chuyên môn, sư phạm chuẩn mực.
        """
        
        st.subheader("📋 Kết quả Prompt của bạn:")
        st.code(prompt, language="text")
        st.info("💡 Bạn hãy copy đoạn mã trên và dán vào ChatGPT hoặc Gemini để nhận bài soạn chi tiết.")