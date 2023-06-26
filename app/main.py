from dotenv import load_dotenv, find_dotenv
from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType

from app.tools import create_dashboard, create_superset_chart

# Load environment variables
load_dotenv(find_dotenv())

# Initialise the LLM to use for the agent
llm = OpenAI(model_name="text-davinci-003")

# Initialise an agent with the custom `create_superset_char` tool, the language model, and the type of agent we want
# to use
agent_executor = initialize_agent(
    [create_dashboard, create_superset_chart],
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# Run the agent
#agent_executor.run("Create a pie-chart that shows car sales per dealership")
agent_executor.run("Create a line chart that shows car sales per country. Thank you!")
#agent_executor.run("Create a new dashboard with the title 'Sales Dashboard' and slug 'test-sales-dashboard'")

# FIXME: expected this to fail but didn't:
#agent_executor.run("Show me sales per month")
