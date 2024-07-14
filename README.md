# Scribe 📖

Scribe is a Python application that transcribes audio files into text and summarizes them originally developed to streamline the process of converting tabletop sessions into markdown files.

## Table of Contents
- [Installation](#installation)
  - [Install Python](#install-python)
  - [Install Ollama](#install-ollama)
  - [Install Poetry](#install-poetry)
  - [Project Setup](#project-setup)
- [Running the Application](#running-the-application)

## Installation

### Install Python
For the application to work Python 3.10 is required, which can be downloaded from [python.org/downloads/](https://www.python.org/downloads/).


### Install Ollama

To use the summarization features of Scribe, you need to install `ollama` and the necessary models. Follow these steps:

1. Download and install `ollama` from [ollama.com/download](https://ollama.com/download). Installers are available for Linux, Mac, and Windows.

2. To check if the installation was completed successfully, you can run
   ```bash
   ollama --version
   ```
   which should display currently installed version of `ollama`.

3. After installing `ollama`, you can install the required transcription models. A list of available models can be found at [ollama.com/library](https://ollama.com/library).


4. To install a specific model, use the following command:
    ```bash
    ollama pull llama3
    ```

Replace `llama3` with the name of the transcription model you want.

### Install Poetry

To install Poetry, follow these steps (taken from the official installation instructions available at [python-poetry.org/docs/#installing-with-the-official-installer](https://python-poetry.org/docs/#installing-with-the-official-installer)):

1. Install Poetry by running the following command for Linux, macOS, and Windows (WSL):
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
   Note: On some systems, `python` may still refer to Python 2 instead of Python 3. It's recommended to use the `python3` binary to avoid ambiguity.

2. For Windows (Powershell), use the following command:
    ```powershell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```
   
   > If you have installed Python through the Microsoft Store, replace `py` with `python` in the command above.
        

### Project Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/scribe.git
    cd scribe
    ```

2. Install the dependencies using Poetry:
    ```bash
    poetry install
    ```

## Running the Application

To run the application, follow these steps:

1. Activate the Poetry shell:
    ```bash
    poetry shell
    ```

2. Start the Streamlit application:
    ```bash
    streamlit run scribe.py
    ```

Visit [http://localhost:8501](http://localhost:8501) in your web browser to use the application.

