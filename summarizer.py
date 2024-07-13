from langchain_community.llms import Ollama
import re
import subprocess


prompt_summarize = '''
#INSTRUCTIONS
Summarize the contents of the provided TEXT in detail and extract important information.
#TEXT
{text}

Identify key elements such as character interactions, important decisions, significant plot developments and
noteworthy dialogue. 
Names of characters and locations must be marked like this: [[<NAME>]]

The output must be formatted in markdown language and must adhere to the provided EXAMPLE including the section 
# Overview, # Notes, # NPCs and # Locations.

#EXAMPLE
# Session
<A written summary of the provided text.>
# Notes
<a bulleted list of key key elements such as character interactions, important decisions, 
significant plot developments and noteworthy dialogue.>
# NPCs
<A list of mentioned characters>
# Locations
<A list of mentioned locations>
'''


def summarize(transcription, model="llama3"):
    print(f"running with model {model}")
    llm = Ollama(model=model, stop=["<|#session"])
    res = llm.invoke(prompt_summarize.format(text=transcription))
    return res


def list_installed_models():
    try:
        # Run the 'ollama list' command
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        if result.returncode == 0:
            # Split the output into lines
            lines = result.stdout.splitlines()
            # Extract model names using regular expression
            model_names = []
            for line in lines:
                # Skip error messages and header
                if not line.startswith("failed") and not line.startswith("NAME"):
                    # select string until first ":" indicating the version of the model
                    # do not use embedding models
                    match = re.match(r".+?(?=:)", line)
                    if match and "embed" not in match.group(0):
                        model_names.append(match.group(0))
            return model_names
        else:
            print(f"Error: {result.stderr}")
            return []
    except Exception as e:
        print(f"Error: {e}")
        return []