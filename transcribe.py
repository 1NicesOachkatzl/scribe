import streamlit as st
import speech_recognition as sr
from transcription import transcribe
from streamlit_session_keys import *


def set_is_transcribing():
    st.session_state[transcribeKey] = True
    st.session_state[transcriptionKey] = ""
    pass


def main():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Session keys
    if transcribeKey not in st.session_state:
        st.session_state[transcribeKey] = False

    if transcriptionKey not in st.session_state:
        st.session_state[transcriptionKey] = ""

    # Streamlit UI
    st.title("Audio Transcription App")
    uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

    if st.session_state[transcribeKey]:
        st.session_state[transcriptionKey] = transcribe(recognizer, uploaded_file)
        st.session_state[transcribeKey] = False
        st.rerun()
    else:
        if uploaded_file is not None:
            st.button("Start Transcription", on_click=set_is_transcribing)
        else:
            st.info("Please select a file first")

    if st.session_state[transcriptionKey] != "":
        st.write("## Transcription:")
        st.write(st.session_state[transcriptionKey])

        # Add download button
        st.download_button(
            label="Download Transcription",
            data=st.session_state[transcriptionKey],
            file_name="transcription.txt",
            mime="text/plain"
        )


if __name__ == "__main__":
    main()
