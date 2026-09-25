import streamlit as st

st.set_page_config(page_title="Naija Study AI", page_icon="📚")
st.title("STUDY SMARTER")
st.write("Ask any question from your assignments, projects etc.")

question = st.text_input("Ask me anything...", placeholder="Type your assignment question here...")

if question:
    st.success(f"You asked: {question}")
    st.write("AI is thinking... (we will connect real AI next)")
    st.info("For now, this box is clickable and working! ✅")
