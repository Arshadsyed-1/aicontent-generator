import streamlit as st
from groq import Groq

# API setup
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("✍️ AI Content Generator (Groq)")

# Inputs
topic = st.text_input("Enter Topic")

tone = st.selectbox(
    "Select Tone",
    ["Formal", "Casual", "Technical", "Creative"]
)

format_type = st.selectbox(
    "Content Type",
    ["Blog Post", "LinkedIn Post", "Twitter Thread"]
)

word_limit = st.slider("Word Limit", 50, 500, 150)

# Button
if st.button("Generate Content"):
    if topic:
        prompt = f"""
        Generate a {format_type} about: {topic}

        Tone: {tone}
        Word Limit: {word_limit}

        Make it engaging and well-structured.
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Groq model
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        st.subheader("Generated Content:")
        st.write(response.choices[0].message.content)

    else:
        st.warning("Please enter a topic")