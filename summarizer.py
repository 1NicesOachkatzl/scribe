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


prompt_combine = '''
#INSTRUCTIONS
Combine the information provided in TEXT which includes a number of summaries of the same source.
#TEXT
{text}
Use the following sections for formatting: # Overview, # Notes, # NPCs, # Locations
Use markdown for the formatting.
Mark names of characters and locations like this: [[<NAME>]]
Please append the following tag as text at the end of the output: \n \n #session
Here is an example of an output:
# Overview
<Overview over the key events in a maximum of 5 sentences.>
# Notes
<Give a detailed explanation over all events which took place in about 500 words.>
# NPCs
<A list of mentioned characters>
# Locations
<A list of mentioned locations>
#session
'''


def prompt_llm_summarize(model, text):
    llm = Ollama(model=model, stop=["<|#session"])
    res = llm.invoke(prompt_summarize.format(text=text))
    return res


def prompt_llm_combine(model, text):
    llm = Ollama(model=model, stop=["<|#session"])
    res = llm.invoke(prompt_combine.format(text=text))
    return res


def summarize(transcription):
    model = "llama3"
    return prompt_llm_summarize(model, transcription)
