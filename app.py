import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่า API Key
GEMINI_API_KEY = "AIzaSyDUt6fHGRsOMxRMpfoGry1IJ19BONjLftM"
genai.configure(api_key=GEMINI_API_KEY)

# 2. เลือกโมเดล (ใช้ตัวที่เสถียรที่สุด)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🎸 Valeton GP-200 Tone Assistant")
st.write("ค้นหาสูตรปรับเสียงกีตาร์สำหรับ Valeton GP-200")

# 3. ส่วนรับชื่อเพลง
song_name = st.text_input("ใส่ชื่อเพลง / ศิลปินที่คุณต้องการ:", placeholder="เช่น อยากเห็นหน้าคุณ - LOSO")

if st.button("ค้นหาโทนเสียง"):
    if song_name:
        with st.spinner('กำลังวิเคราะห์โทนเสียง...'):
            try:
                # ส่งคำสั่งให้ AI วิเคราะห์
                prompt = f"ขอการตั้งค่า Signal Chain สำหรับ Valeton GP-200 ในเพลง {song_name} โดยบอกละเอียดทั้ง Amp, Cab, และ Effects"
                response = model.generate_content(prompt)
                
                # แสดงผลลัพธ์
                st.success(f"โทนเสียงสำหรับเพลง: {song_name}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
    else:
        st.warning("กรุณาใส่ชื่อเพลงก่อนครับ")
