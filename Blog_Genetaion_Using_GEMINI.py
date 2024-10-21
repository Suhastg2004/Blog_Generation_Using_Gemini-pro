import streamlit as st
import os
os.environ['GEMINI_API_KEY'] = 'AIzaSyAZF6RrIivArfNcwaKWfeGtjIU3BYWqJAE'

import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import google.generativeai as genai

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

#List available modules
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)

llm = genai.GenerativeModel("gemini-1.5-pro")
response = llm.generate_content("What is the meaning of life?").text
print(response)

from langchain.prompts import PromptTemplate
prompt_template_name = PromptTemplate(
    input_variables=['topic'],
    template="Write a blog of 500 words on {topic} with seperate paragrah with heading like introduction,content and conclusion ."
)

# from langchain.chains import LLMChain
# chain = LLMChain(llm=llm, prompt=prompt_template_name)
response = llm.generate_content(prompt_template_name.format(topic="Indian"), stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)

