import streamlit as st

transcribeKey = 'is_transcribing'
transcriptionKey = 'transcription'
summaryKey = 'summary'
summarizeKey = 'is_summarizing'


def init_session_keys():
    if transcribeKey not in st.session_state:
        st.session_state[transcribeKey] = False

    if transcriptionKey not in st.session_state:
        st.session_state[transcriptionKey] = ""

    if summarizeKey not in st.session_state:
        st.session_state[summarizeKey] = False

    if summaryKey not in st.session_state:
        st.session_state[summaryKey] = ""
