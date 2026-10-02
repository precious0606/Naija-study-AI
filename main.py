import streamlit as st
from google import genai

st.set_page_config(page_title="NaijaStudy AI", page_icon="📚", layout="centered")

# --- PASTE YOUR NEW AQ... KEY HERE ---
API_KEY = "AQ.Ab8RN6LnUMyj58W6Ng9WWOaHKWIquvdqqSUQitsV4gZoVHc5GA"
client = genai.Client(api_key=API_KEY)

st.title("📚 NaijaStudy AI")
st.caption("Your friendly study buddy - No stress, just success!")

with st.sidebar:
    st.header("⚙️ Set Up")
    class_level = st.selectbox("Your Class:", ["JSS1", "JSS2", "JSS3", "SS1", "SS2", "SS3"])
    language = st.selectbox("Explain in:", ["Simple English", "Pidgin English", "Mix of Both"])
    mode = st.radio("What do you want to do?", ["💬 Explain Topic", "📝 Summarize My Note", "🎮 Quiz Me"])

if "subject" not in st.session_state:
    st.session_state.subject = "General Study"

st.subheader("1. Pick Subject")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📐 Maths"): st.session_state.subject = "Mathematics"
    if st.button("🧬 Biology"): st.session_state.subject = "Biology"
with col2:
    if st.button("⚗️ Chemistry"): st.session_state.subject = "Chemistry"
    if st.button("📜 Govt"): st.session_state.subject = "Government"
with col3:
    if st.button("📖 English"): st.session_state.subject = "English"
    if st.button("🌍 Geography"): st.session_state.subject = "Geography"

st.info(f"Selected: **{st.session_state.subject}** | Class: **{class_level}**")
st.subheader(f"2. {mode}")

user_input = st.chat_input(f"Ask anything about {st.session_state.subject}...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Your buddy is thinking..."):
            prompt = f"You are NaijaStudy AI, a friendly, fun, encouraging Nigerian tutor for {class_level} student. Subject: {st.session_state.subject}. Language: {language}. Mode: {mode}. Make it SUPER easy, use emojis, bullet points, one simple example. End with encouragement. Student asked: {user_input}"
            try:
                response = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
                st.write(response.text)
            except Exception as e:
                st.error(f"Omo! Small error: {e}")
