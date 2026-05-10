import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่า API Key และบังคับใช้ Transport แบบ 'rest' เพื่อแก้ปัญหา 404
# ตรวจสอบให้มั่นใจว่า API Key ถูกต้อง (ไม่มีช่องว่างเกินมา)
GEMINI_API_KEY = "AIzaSy..." # ใส่รหัสของคุณให้ครบถ้วน
genai.configure(api_key=GEMINI_API_KEY, transport='rest') #

# 2. เลือกโมเดล
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🎸 Valeton GP-200 Tone Assistant")
st.write("ระบุชื่อเพลงเพื่อหาค่าการตั้งค่าสำหรับ Valeton GP-200")

song_name = st.text_input("ใส่ชื่อเพลง และ ศิลปิน:", placeholder="เช่น อยากเห็นหน้าคุณ - LOSO")

if st.button("ค้นหาโทนเสียง"):
    if song_name:
        with st.spinner('กำลังค้นหาสูตรเสียง...'):
            try:
                # แก้ไขปัญหา Latin-1 โดยการใช้ f-string ที่เรียบง่าย
                # และระบุให้ AI ตอบเป็นขั้นตอนสำหรับมัลติเอฟเฟค
                full_prompt = f"ขอสูตรปรับเสียง Valeton GP-200 สำหรับเพลง {song_name} บอกรายละเอียด Amp, Cab, และ Effect"
                
                response = model.generate_content(full_prompt)
                
                st.success(f"ผลลัพธ์สำหรับ: {song_name}")
                st.markdown(response.text)
            except Exception as e:
                # แสดงข้อผิดพลาดที่ชัดเจนขึ้น
                st.error(f"เกิดข้อผิดพลาด: {str(e)}")
