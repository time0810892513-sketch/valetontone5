import streamlit as st
import google.generativeai as genai

# 1. ใส่ API KEY ของคุณตรงนี้
GEMINI_API_KEY = "AIzaSyDUt6fHGRs0MxRMpfoGry1IJl9BONjLftM"

st.set_page_config(page_title="Valeton GP-200 Assistant", page_icon="🎸")
st.title("🎸 Valeton GP-200 Tone Assistant")

def run_ai(user_query):
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        
        # ค้นหาชื่อรุ่นที่เครื่องคุณอนุญาตให้ใช้ (เพื่อแก้ปัญหา 404)
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # เลือกใช้รุ่นแรกที่หาเจอ (ปกติจะเป็น gemini-1.5-flash หรือ gemini-pro)
        if available_models:
            model_name = available_models[0]
            model = genai.GenerativeModel(model_name)
        else:
            return "❌ ไม่พบ Model ที่ใช้งานได้ใน API Key นี้"

        prompt = f"""
        ในฐานะมือกีตาร์ที่เชี่ยวชาญ Valeton GP-200 
        ช่วยแนะนำการตั้งค่าสำหรับเพลง: {user_query}
        1. ระบุชื่อ AMP และ CAB ที่มีในเครื่อง
        2. บอกค่า Gain และ EQ เบื้องต้น
        3. แนะนำเอฟเฟกต์ที่ควรใช้ใน Signal Chain
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"🆘 เกิดข้อผิดพลาด: {str(e)}"

user_input = st.text_input("🎵 ใส่ชื่อเพลง / ศิลปิน (เช่น อยากเห็นหน้าคุณ - LOSO):")

if st.button("ค้นหาโทนเสียง"):
    if user_input:
        with st.spinner("กำลังค้นหาโทนเสียงที่ดีที่สุด..."):
            result = run_ai(user_input)
            st.write(result)
    else:
        st.warning("ใส่ชื่อเพลงก่อนนะครับ")