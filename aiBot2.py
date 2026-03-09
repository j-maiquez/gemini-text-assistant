import streamlit as st
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=api_key)

st.title("AI Document Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

#Sidebar
with st.sidebar:
    st.header("Settings")
    st.info("Model: Gemini 3 Flash\nTask: Text Analysis")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

#Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Enter your request...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="💁"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = st.session_state.client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "You are a professional assistant. "
                        "Provide factual, concise responses. "
                        "If a request is ambiguous, ask for clarification. "
                        "Avoid making up facts or providing sensitive personal data."
                    )
                )
            )

            response_text = response.text
            st.markdown(response_text)

            st.session_state.messages.append({"role": "assistant", "content": response_text})

        except Exception as e:
            st.error(f"An error occurred: {e}")
