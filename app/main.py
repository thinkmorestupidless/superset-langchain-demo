from dotenv import load_dotenv, find_dotenv
from langchain import OpenAI
from langchain.agents import initialize_agent, AgentType

from app.custom_tools.create_dashboard_tool import create_dashboard
from app.custom_tools.create_superset_chart_tool import create_superset_chart

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
# Pie charts
#agent_executor.run("Create a pie chart that shows Overall Sales (By Product Line)")
#agent_executor.run("Create a pie chart that shows revenue by product line")
#agent_executor.run("Create a pie chart that shows number of cars sold by vehicle category")  # expecting it to "translate" it to count per product_line
#agent_executor.run("Create a pie chart that shows profit made by product type") # expecting it to "translate" it to count per product_line - unstable
#agent_executor.run("Create a pie chart that shows sum of sales by deal size")
#agent_executor.run("Create a pie chart that shows count of sales by deal size")
#agent_executor.run("Create a pie chart that shows count of sales by territory")
#agent_executor.run("Create a pie chart that shows number of sales by territory") # alternative to 'count of'
#agent_executor.run("Create a pie chart that displays sum of car sales by country")
#agent_executor.run("Create a pie chart that shows count of sales by country")
#agent_executor.run("Create a pie chart that shows the sum of cars ordered by country") # not sure about that
#agent_executor.run("Create a pie chart that displays sum of car sales by month")
#agent_executor.run("Create a pie chart that displays count of sales by onth") # deliberate typo
#agent_executor.run("Create a pie chart that displays sum of car sales by year")
#agent_executor.run("Create a pie chart that displays count of sales by year")

# Dashboards
#agent_executor.run("Create a new superset dashboard called 'New Sales Dashboard'")
#agent_executor.run("Create a new dashboard called 'New Sales Dashboard'")
#agent_executor.run("Create a new 'Sales Dashboard 2022'")
#agent_executor.run("Create a new dashboard called 'Sales 2022'")

# Graph charts

# ---



#agent_executor.run("Create a new dashboard with the title 'Sales Dashboard 3' and slug 'test-sales-dashboard-3' and add chart 44 to it")
#agent_executor.run("Create a pie chart that shows car sales per car model")
#agent_executor.run("Create a pie chart that shows number of cars sold per month and add it to the Sales Dashboard")
#agent_executor.run("Create a pie chart that shows car sales per dealership")
#agent_executor.run("Create a line chart that shows car sales per country. Thank you!")

# TODO
#agent_executor.run("Create a pie chart that shows revenue by product line. Make it a doughnut please.")
