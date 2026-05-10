import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่า API Key และบังคับใช้เวอร์ชัน API v1
GEMINI_API_KEY = "AIzaSyDb_1D2526eAgbzYaLKRy0XlCdr-hc1BDs" #
genai.configure(api_key=GEMINI_API_KEY)

# 2. เลือกโมเดลโดยใช้ชื่อพาธเต็มเพื่อเลี่ยง Error 404
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash") #

# ส่วนหัวของแอป
st.title("🎸 Valeton GP-200 Tone Assistant")
st.write("ระบุชื่อเพลงเพื่อหาค่าการตั้งค่า Amp/Eff สำหรับ Valeton GP-200")

# ส่วนรับอินพุต
song_name = st.text_input("ใส่ชื่อเพลง และ ศิลปิน:", placeholder="เช่น อยากเห็นหน้าคุณ - LOSO")

if st.button("ค้นหาโทนเสียง"):
    if song_name:
        with st.spinner('กำลังค้นหาสูตรเสียง...'):
            try:
                # ส่งคำสั่งให้ AI
                prompt = f"ขอสูตรการปรับเสียง (Signal Chain) สำหรับ Valeton GP-200 ในเพลง {song_name} บอกรายละเอียดทั้ง Amp, Cab, และก้อน Effect"
                response = model.generate_content(prompt)
                
                # แสดงผล
                st.success(f"ผลลัพธ์สำหรับเพลง: {song_name}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
