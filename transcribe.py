import streamlit as st
import speech_recognition as sr
from transcription import transcribe
from streamlit_session_keys import *
from summarizer import summarize


def set_is_transcribing():
    st.session_state[transcribeKey] = True
    st.session_state[transcriptionKey] = ""
    pass


def set_is_summarizing():
    st.session_state[summarizeKey] = True
    st.session_state[summaryKey] = ""
    pass


def main():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Session keys
    if transcribeKey not in st.session_state:
        st.session_state[transcribeKey] = False

    if transcriptionKey not in st.session_state:
        st.session_state[transcriptionKey] = ""

    if summarizeKey not in st.session_state:
        st.session_state[summarizeKey] = False

    if summaryKey not in st.session_state:
        st.session_state[summaryKey] = ""

    # Streamlit UI
    st.set_page_config(
        page_title="Scribe",
        page_icon=":book:"
    )

    st.title("Scribe")
    uploaded_file = st.file_uploader("Choose a WAV file", type=["wav", "mp3"])

    # Transcription logic
    if st.session_state[transcribeKey]:
        st.session_state[transcriptionKey] = transcribe(recognizer, uploaded_file)
        st.session_state[transcribeKey] = False
        st.rerun()
    else:
        if uploaded_file is not None:
            st.button("Start Transcription", on_click=set_is_transcribing)
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
        st.button("Summarize", on_click=set_is_summarizing)

    if st.session_state[summaryKey] != "":
        with st.container(height=250):
            st.write(st.session_state[summaryKey])


if __name__ == "__main__":
    main()
