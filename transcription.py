import speech_recognition as sr
from pydub import AudioSegment
import os
import streamlit as st


def split_audio(audio_path, chunk_length_ms=60000):
    audio = AudioSegment.from_wav(audio_path)
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunks.append(chunk)
    return chunks


def transcribe(recognizer, uploaded_file):
    if uploaded_file is not None:
        with st.spinner('Transcribing...'):
            # Load the audio file
            audio_file_path = "temp.wav"
            with open(audio_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Split audio into 1-minute chunks
            chunks = split_audio(audio_file_path)
            num_chunks = len(chunks)

            # Progress bar
            progress_bar = st.progress(0)
            transcription = ""

            for i, chunk in enumerate(chunks):
                chunk_filename = f"audio_chunk_{i}.wav"
                chunk.export(chunk_filename, format="wav")

                with sr.AudioFile(chunk_filename) as source:
                    audio = recognizer.record(source)

                try:
                    text = recognizer.recognize_whisper(audio)
                    transcription += text + " "

                except sr.UnknownValueError:
                    st.error(f"Whisper could not understand audio chunk {i + 1}")
                except sr.RequestError as e:
                    st.error(f"Could not request results from Whisper service for chunk {i + 1}; {e}")

                # Update progress bar
                progress_bar.progress((i + 1) / num_chunks)

                # Clean up chunk file
                os.remove(chunk_filename)

            # remove temp audio file
            os.remove(audio_file_path)

            return transcription

    else:
        st.error("Please upload a WAV file before starting the transcription")
        return ""

