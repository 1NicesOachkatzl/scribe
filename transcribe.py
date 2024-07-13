import streamlit as st
import speech_recognition as sr
from transcription import transcribe
from streamlit_session_keys import *
from summarizer import summarize


def main():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Initialize session keys
    init_session_keys()

    # Streamlit UI
    st.set_page_config(page_title="Scribe", page_icon=":book:")

    uploaded_file = st.file_uploader("Choose a WAV file", type=["wav", "mp3"])

    # Transcription logic
    if st.session_state[transcribeKey]:
        st.session_state[transcriptionKey] = transcribe(recognizer, uploaded_file)
        st.session_state[transcribeKey] = False
        st.rerun()
    else:
        if uploaded_file is not None:
            st.button("Start Transcription", on_click=lambda: (st.session_state.update({transcribeKey: True, transcriptionKey: ""})))
        else:
            st.info("Please select a file first")

    # Summarization logic
    if st.session_state[summarizeKey]:
        st.session_state[summaryKey] = summarize(st.session_state[transcriptionKey])
        st.session_state[summarizeKey] = False
        st.rerun()
        pass

    if st.session_state[transcriptionKey] != "":
        # Transcription area
        st.divider()
        st.write("### Transcription")

        with st.container(height=250):
            st.write(st.session_state[transcriptionKey])

        st.download_button(
            label="Download",
            data=st.session_state[transcriptionKey],
            file_name="transcription.txt",
            mime="text/plain"
        )

        # Processing area
        st.button("Summarize", on_click=lambda: (st.session_state.update({summarizeKey: True, summaryKey: ""})))

    if st.session_state[summaryKey] != "":
        with st.container(height=250):
            st.write(st.session_state[summaryKey])


if __name__ == "__main__":
    main()
