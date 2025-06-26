import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv  

load_dotenv()  # This line reads from .env

# Load your API key
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])




SYSTEM_PROMPT = """You are a helpful and clear statistics tutor for undergraduates.
Use plain language, guide students through statistical reasoning, and explain R code when asked.
Use real-world social science examples when possible."""

st.set_page_config(page_title="Stats Tutor", layout="wide")
st.title("📊 Statistics Tutor for STA145")

with st.form("question_form"):
    question = st.text_area("Ask me a statistics question:")
    submitted = st.form_submit_button("Submit")

if submitted and question:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": question}
                ]
            )
            st.markdown("### 🧠 Tutor's Response:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
