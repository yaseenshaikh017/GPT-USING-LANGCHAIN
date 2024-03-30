# bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
os.environ['OPENAI_API_KEY'] = apikey

# this is for our app framework
st.title("🛑 Youtube GPT CREATOR 🛑")
prompt = st.text_input('Plug in  your prompt here')

#this is our prompt templates
title_template = PromptTemplate(
        input_variables = ['topic']
        template = ' write me a youtube video title about {topic}'
)

# for llms
llm = OpenAI(temperature=0.9)
title_chain  = LLMChain(llm=llm, prompt= title_template,verbose = True)

# this will show the material to the screen if there is a prompt
if prompt:
    response = title_chain.run(topic=prompt)
    st.write(response)
