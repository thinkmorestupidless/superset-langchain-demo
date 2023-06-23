from dotenv import load_dotenv, find_dotenv
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from agents import create_chart_tool

# Load environment variables
load_dotenv(find_dotenv())

# Define the LLM
llm = OpenAI(model_name="text-davinci-003")

# Initialize an agent with the tools, the language model, and the type of agent we want to use
agent_executor = initialize_agent(
    [create_chart_tool],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# Run the agent
agent_executor.run("Give me a bar chart that shows car sales per month")
