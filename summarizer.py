from langchain_community.llms import Ollama

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


def prompt_llm_summarize(model, text):
    llm = Ollama(model=model, stop=["<|#session"])
    res = llm.invoke(prompt_summarize.format(text=text))
    return res


def summarize(transcription):
    model = "llama3"
    return prompt_llm_summarize(model, transcription)
