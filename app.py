import streamlit as st
import google.generativeai as genai

# 1. ตั้งค่า API Key (ห้ามลบเครื่องหมายอัญประกาศ)
GEMINI_API_KEY = "AIzaSyDShLCosHT_-7CLtgsGY_sBsijC5RlquVg"
genai.configure(api_key=GEMINI_API_KEY)

# 2. เลือกโมเดล
model = genai.GenerativeModel('gemini-1.5-flash-latest')
st.title("🎸 Valeton GP-200 Tone Assistant")
st.write("ระบุชื่อเพลงเพื่อหาค่าการตั้งค่า Amp/Eff สำหรับ Valeton GP-200")

# 3. ส่วนรับอินพุต
song_name = st.text_input("ใส่ชื่อเพลง และ ศิลปิน:", placeholder="เช่น อยากเห็นหน้าคุณ - LOSO")

if st.button("ค้นหาโทนเสียง"):
    if song_name:
        with st.spinner('กำลังค้นหาสูตรเสียง...'):
            try:
                # ส่งคำสั่งให้ AI
                prompt = f"ขอสูตรการปรับเสียง (Signal Chain) สำหรับ Valeton GP-200 ในเพลง {song_name} บอกละเอียดทั้ง Amp, Cab, และก้อน Effect"
                response = model.generate_content(prompt)
                
                # แสดงผล
                st.success(f"ผลลัพธ์สำหรับ: {song_name}")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาด: {e}")
    else:
        st.warning("กรุณาพิมพ์ชื่อเพลงก่อนกดค้นหาครับ")
