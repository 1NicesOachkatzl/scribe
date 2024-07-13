import streamlit as st
from summarizer import list_installed_models

transcribeKey = 'is_transcribing'
transcriptionKey = 'transcription'
summaryKey = 'summary'
summarizeKey = 'is_summarizing'
modelKey = 'model'


def init_session_keys():
    """
    Initialize session state keys if they don't exist.
    """
    if transcribeKey not in st.session_state:
        st.session_state[transcribeKey] = False

    if transcriptionKey not in st.session_state:
        st.session_state[transcriptionKey] = ""

    if summarizeKey not in st.session_state:
        st.session_state[summarizeKey] = False

    if summaryKey not in st.session_state:
        st.session_state[summaryKey] = ""

    if modelKey not in st.session_state:
        installed_models = list_installed_models()
        if len(installed_models) > 0:
            st.session_state[modelKey] = list_installed_models()[0]

