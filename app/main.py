from dotenv import load_dotenv, find_dotenv
from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType

from app.custom_tools.create_dashboard_tool import create_dashboard
from app.custom_tools.create_superse_chart_tool import create_superset_chart

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
agent_executor.run("Create a new dashboard with the title 'Sales Dashboard 3' and slug 'test-sales-dashboard-3' and add chart 44 to it")
#agent_executor.run("Create a pie chart that shows car sales per car model")
#agent_executor.run("Create a pie chart that shows SUM of sales per model")
#agent_executor.run("Create a pie chart that shows number of cars sold per month and add it to the Sales Dashboard")
#agent_executor.run("Create a pie chart that shows car sales per dealership")
#agent_executor.run("Create a line chart that shows car sales per country. Thank you!")

# FIXME: expected this to fail but didn't:
#agent_executor.run("Show me sales per month")

# Ideas
# - Get list of favourite charts /api/v1/chart/favorite_status/
# - Delete chart /api/v1/chart/{pk}
# - Delete a dashboard /api/v1/dashboard/{pk}
# - Get list of favourite dashboards /api/v1/dashboard/favorite_status/
# - Get list of models /api/v1/database/
