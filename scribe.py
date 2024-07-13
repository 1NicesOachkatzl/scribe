from transcription import transcribe
from streamlit_session_keys import *
from summarizer import summarize, list_installed_models


def main():
    """Main function to set up Streamlit UI for transcription and summarization."""

    # Initialize session keys
    init_session_keys()

    # Streamlit UI
    st.set_page_config(page_title="Scribe", page_icon=":book:")
    st.title("Scribe :book:")

    # Sidebar for model selection
    installed_models = list_installed_models()
    if installed_models:
        st.sidebar.selectbox("Select a model:", installed_models, key=modelKey)
    else:
        st.sidebar.write("No models found or an error occurred.")

    uploaded_file = st.file_uploader("Choose a WAV file", type=["wav", "mp3"])
    
    # Transcription logic
    if st.session_state[transcribeKey]:
        st.session_state[transcriptionKey] = transcribe(uploaded_file)
        st.session_state[transcribeKey] = False
        st.rerun()
    else:
        if uploaded_file is not None:
            st.button("Start Transcription", on_click=lambda: (st.session_state.update({transcribeKey: True, transcriptionKey: ""})))
        else:
            st.info("Please select a file first")

    # Summarization logic
    if st.session_state[summarizeKey]:
        st.session_state[summaryKey] = summarize(transcription=st.session_state[transcriptionKey], model=st.session_state[modelKey])
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
            label="Download Transcription",
            data=st.session_state[transcriptionKey],
            file_name="transcription.txt",
            mime="text/plain"
        )

        # Processing area
        st.button("Summarize", on_click=lambda: (st.session_state.update({summarizeKey: True, summaryKey: ""})))

    # Display summary
    if st.session_state[summaryKey] != "":
        st.divider()
        with st.container(height=250):
            st.write(st.session_state[summaryKey])

        st.download_button(
            label="Download Summary",
            data=st.session_state[summaryKey],
            file_name="summary.md",
            mime="text/markdown"
        )


if __name__ == "__main__":
    main()
