import streamlit as st
import google.generativeai as genai

# บังคับใช้ค่าคงที่เพื่อความเสถียร
API_KEY = "AIzaSyDUuaqNCi7YhqJ65PimkscsXMDFRYElXrQ" # ตรวจสอบ Key อีกครั้งใน Google AI Studio

# ตั้งค่าโดยบังคับใช้ transport='rest' เพื่อหลีกเลี่ยงปัญหา gRPC 
genai.configure(api_key=API_KEY, transport='rest')

# เรียกใช้โมเดลโดยไม่ระบุเวอร์ชัน v1beta ในชื่อ
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🎸 Valeton GP-200 Tone Assistant")

song_name = st.text_input("ระบุชื่อเพลง (ไทย/อังกฤษ):", placeholder="เช่น อยากเห็นหน้าคุณ - LOSO")

if st.button("ค้นหาโทนเสียง"):
    if song_name:
        try:
            # คำสั่งสำหรับหาโทนเสียง LOSO
            prompt = f"แนะนำการตั้งค่า Valeton GP-200 สำหรับเพลง {song_name} ขอแบบละเอียด (Amp, Gain, EQ, Cab)"
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
