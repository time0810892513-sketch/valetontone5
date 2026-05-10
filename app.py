import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่า API Key และบังคับใช้ Transport 'rest' เพื่อแก้ปัญหา 404
# ตรวจสอบ API Key ให้ถูกต้องจาก Google AI Studio
API_KEY = "AIzaSyDb_1D2526eAgbzYaLKRy0XlCdr-hc1BDs" # แทนที่ด้วย API Key ของคุณ
genai.configure(api_key=API_KEY, transport='rest') #

# 2. เรียกใช้โมเดล gemini-1.5-flash
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🎸 Valeton GP-200 Tone Assistant")
st.write("ระบุชื่อเพลงเพื่อหาค่าการตั้งค่าสำหรับ Valeton GP-200")

# รับค่าชื่อเพลง
song_name = st.text_input("ใส่ชื่อเพลง และ ศิลปิน:", placeholder="เช่น อยากเห็นหน้าคุณ - LOSO")

if st.button("ค้นหาโทนเสียง"):
    if song_name:
        with st.spinner('กำลังค้นหาสูตรเสียง...'):
            try:
                # สร้างคำสั่งที่ชัดเจนเพื่อให้ AI ออกแบบ Signal Chain
                prompt = (
                    f"แนะนำการตั้งค่า Valeton GP-200 สำหรับเพลง {song_name} "
                    "โดยขอรายละเอียด: Amp model, Cab, Drive, Delay และ Reverb"
                )
                
                # ส่งคำสั่ง (รองรับภาษาไทยผ่าน f-string)
                response = model.generate_content(prompt)
                
                st.success(f"ผลลัพธ์สำหรับ: {song_name}")
                st.markdown(response.text)
            except Exception as e:
                # แสดงข้อความ Error ที่อ่านง่าย
                st.error(f"เกิดข้อผิดพลาด: {str(e)}")
    else:
        st.warning("กรุณาใส่ชื่อเพลงก่อนครับ")
