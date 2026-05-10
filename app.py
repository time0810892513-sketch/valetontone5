import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่า API Key - แนะนำให้สร้าง Key ใหม่จาก Google AI Studio
# และตรวจสอบว่าไม่มีช่องว่างว่างๆ ปนเข้ามาในรหัส
GEMINI_API_KEY = "AIzaSyDb_1D2526eAgbzYaLKRy0XlCdr-hc1BDs" # ใส่รหัส API Key ของคุณที่นี่

try:
    genai.configure(api_key=GEMINI_API_KEY, transport='rest') # ใช้ rest เพื่อเลี่ยง v1beta error
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"การตั้งค่า API ล้มเหลว: {e}")

st.title("🎸 Valeton GP-200 Tone Assistant")
st.write("ระบุชื่อเพลงเพื่อหาค่าการตั้งค่า Amp/Eff สำหรับ Valeton GP-200")

# รับอินพุตชื่อเพลง
song_name = st.text_input("ใส่ชื่อเพลง และ ศิลปิน:", placeholder="เช่น อยากเห็นหน้าคุณ - LOSO")

if st.button("ค้นหาโทนเสียง"):
    if song_name:
        with st.spinner('กำลังค้นหาสูตรเสียง...'):
            try:
                # ปรับแต่ง Prompt เพื่อลดปัญหาการเข้ารหัสตัวอักษรและได้ข้อมูลที่แม่นยำ
                prompt_text = (
                    f"ขอรายละเอียดการตั้งค่า (Signal Chain) สำหรับมัลติเอฟเฟค Valeton GP-200 "
                    f"เพื่อให้ได้เสียงเหมือนเพลง {song_name} "
                    f"โดยระบุ: 1. Amp Model 2. Cab Model 3. Drive/Overdrive 4. Delay/Reverb"
                )
                
                # ส่งคำสั่งไปที่ Gemini
                response = model.generate_content(prompt_text)
                
                st.success(f"ผลลัพธ์สำหรับ: {song_name}")
                st.markdown(response.text)
            except Exception as e:
                # แก้ปัญหา 'latin-1' codec โดยการแปลง error เป็น string ก่อนแสดงผล
                st.error(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {str(e)}")
    else:
        st.warning("กรุณาใส่ชื่อเพลงก่อนกดปุ่มครับ")
