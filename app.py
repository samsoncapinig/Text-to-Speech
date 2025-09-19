# app.py
import streamlit as st
from gtts import gTTS
from io import BytesIO

st.title("Text to Filipino Speech Converter 🇵🇭")
st.write("Enter text below and convert it to Filipino speech!")

# Text input
text = st.text_area("Enter your text in Filipino or English:", "")

if st.button("Convert to Speech"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Generate speech
        tts = gTTS(text, lang='tl')  # 'tl' = Tagalog/Filipino
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)

        st.success("Speech generated successfully!")
        st.audio(audio_bytes, format='audio/mp3')
        st.download_button("Download MP3", audio_bytes, file_name="filipino_speech.mp3")
