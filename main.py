import streamlit as st
from google import genai

# PASTE YOUR KEY HERE INSIDE THE QUOTES
API_KEY = "AQ.Ab8RN6LyaC_G5XanbQPhlg-oJ0y7NSA0SeN3LTdwMQSpx0hb2w"

st.set_page_config(page_title="Naija Study AI", page_icon="📚")
st.title("STUDY SMARTER")
st.write("Ask any question from your assignments, projects etc.")

# Setup AI with NEW library
client = genai.Client(api_key=API_KEY)

question = st.text_input("Ask me anything...", placeholder="Type your assignment question here...")

if question:
    with st.spinner("AI is thinking..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=f"You are Naija Study AI, a helpful tutor for Nigerian students. Explain clearly: {question}"
            )
            st.success(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
