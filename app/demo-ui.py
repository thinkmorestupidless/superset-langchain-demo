##########################################
# Run with: `streamlit run app/demo-ui.py`
##########################################

# Importing necessary packages, files and services
import os 

import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

# Load environment variables
load_dotenv(find_dotenv())

# App UI framework
st.title('🦜🔗 Sales Report Generator')
prompt = st.text_input('Report topic: ')

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me a tweet about {topic}'
)

tweet_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='write me a tweet on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research} '
)

# Wikipedia data
wiki = WikipediaAPIWrapper()

# Memory 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
tweet_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


# Llms
llm = OpenAI(model_name="text-davinci-003", temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
tweet_chain = LLMChain(llm=llm, prompt=tweet_template, verbose=True, output_key='script', memory=tweet_memory)

# Chaining the components and displaying outputs
if prompt: 
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt) 
    tweet = tweet_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title) 
    st.write(tweet) 

    with st.expander('Title History'): 
        st.info(title_memory.buffer)

    with st.expander('Tweet History'): 
        st.info(tweet_memory.buffer)

    with st.expander('Wikipedia Research'): 
        st.info(wiki_research)
