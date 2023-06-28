import sys
import os
sys.path.append(os.getcwd() + '/app')

import streamlit as st
from dotenv import load_dotenv, find_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI

from custom_tools import create_dashboard_tool
from custom_tools import create_superset_chart_tool

# from custom_tools.create_dashboard_tool import create_dashboard
# from custom_tools.create_superset_chart_tool import create_superset_chart


# Load environment variables
load_dotenv(find_dotenv())

llm = OpenAI(model_name="text-davinci-003", temperature=0.3)

agent_executor = initialize_agent(
    [create_dashboard_tool.create_dashboard, create_superset_chart_tool.create_superset_chart],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# App UI framework
st.title('Sales Report Generator')
user_input = st.text_input('Report topic: ')

# Chaining the components and displaying outputs
if user_input:
    sales_report = agent_executor.run(user_input)

    st.write(sales_report)
