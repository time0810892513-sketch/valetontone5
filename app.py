import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่า API Key - ตรวจสอบให้มั่นใจว่าคัดลอกมาถูกต้อง 100%
GEMINI_API_KEY = "AIzaSyDUuaqNCi7YhqJ65PimkscsXMDFRYElXrQ" # ใส่รหัสของคุณตรงนี้

# 2. แก้ปัญหา 404 โดยใช้ transport='rest' และเรียกใช้โมเดลเวอร์ชันล่าสุด
genai.configure(api_key=GEMINI_API_KEY, transport='rest') #

# แนะนำให้ใช้ gemini-1.5-flash เพราะเสถียรและเร็วที่สุดสำหรับงานนี้
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🎸 Valeton GP-200 Tone Assistant")
st.write("ระบุชื่อเพลงเพื่อหาค่าการตั้งค่าสำหรับ Valeton GP-200")

# รับค่าชื่อเพลง (รองรับภาษาไทย)
song_name = st.text_input("ใส่ชื่อเพลง และ ศิลปิน:", placeholder="เช่น อยากเห็นหน้าคุณ - LOSO")

if st.button("ค้นหาโทนเสียง"):
    if song_name:
        with st.spinner('กำลังวิเคราะห์สัญญาณเสียง...'):
            try:
                # สร้างคำสั่งที่ระบุรายละเอียดอุปกรณ์ให้ AI เข้าใจบริบทของ Valeton
                prompt = (
                    f"ขอรายละเอียดการตั้งค่า (Signal Chain) สำหรับ Valeton GP-200 "
                    f"เพื่อให้ได้เสียงเหมือนเพลง {song_name} "
                    f"ระบุ: 1. Amp Model 2. Cab 3. Drive 4. Modulation/Delay"
                )
                
                response = model.generate_content(prompt)
                
                st.success(f"ผลลัพธ์สำหรับ: {song_name}")
                st.markdown(response.text)
            except Exception as e:
                # แสดง Error ให้เข้าใจง่ายขึ้น
                st.error(f"เกิดข้อผิดพลาด: {str(e)}")
