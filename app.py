import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่า API Key และบังคับใช้ Transport แบบ 'rest' เพื่อเลี่ยง v1beta error
GEMINI_API_KEY = "รหัส_API_Key_ของคุณ"
genai.configure(api_key=GEMINI_API_KEY, transport='rest') #

# 2. เรียกใช้โมเดลโดยไม่ระบุ path 'models/' นำหน้า
model = genai.GenerativeModel('gemini-1.5-flash') #

st.title("🎸 Valeton GP-200 Tone Assistant")
st.write("ระบุชื่อเพลงเพื่อหาค่าการตั้งค่าสำหรับ Valeton GP-200")

song_name = st.text_input("ใส่ชื่อเพลง และ ศิลปิน:", placeholder="เช่น อยากเห็นหน้าคุณ - LOSO")

if st.button("ค้นหาโทนเสียง"):
    if song_name:
        with st.spinner('กำลังค้นหาสูตรเสียง...'):
            try:
                # ส่งคำสั่งแบบระบุรายละเอียดให้ AI ช่วยออกแบบ Signal Chain
                prompt = f"แนะนำการตั้งค่า Valeton GP-200 สำหรับเพลง {song_name} โดยขอรายละเอียด Amp model, Cab, และ Effect settings"
                response = model.generate_content(prompt)
                
                st.success(f"ผลลัพธ์สำหรับ: {song_name}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
