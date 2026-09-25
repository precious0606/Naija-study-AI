import streamlit as st
from google import genai

API_KEY = "AQ.Ab8R6LbsTTb2mjIqez5iqbzwwLEDXIzkc6rR9X7Y8Z9"

st.set_page_config(page_title="Naija Study AI", page_icon="📚")
st.title("STUDY SMARTER")
st.write("Ask any question from your assignments, projects etc.")

client = genai.Client(api_key=API_KEY)

question = st.text_input("Ask me anything...", placeholder="Type your question here...")

if question:
    with st.spinner("AI is thinking..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=question
            )
            st.success(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
