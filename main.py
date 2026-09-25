import streamlit as st
import google.generativeai as genai

# PASTE YOUR KEY HERE INSIDE THE QUOTES
API_KEY = "PASTE_YOUR_GEMINI_KEY_HERE"

st.set_page_config(page_title="Naija Study AI", page_icon="📚")
st.title("STUDY SMARTER")
st.write("Ask any question from your assignments, projects etc.")

# Setup AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

question = st.text_input("Ask me anything...", placeholder="Type your assignment question here...")

if question:
    with st.spinner("AI is thinking..."):
        try:
            response = model.generate_content(f"You are Naija Study AI, a helpful tutor for Nigerian students. Explain clearly: {question}")
            st.success(response.text)
        except Exception as e:
            st.error(f"Error: {e}. Please check your API key.")
