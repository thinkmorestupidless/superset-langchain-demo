from typing import Optional
from supersetapiclient.charts import Chart
import requests
from langchain import requests
from langchain.tools import tool, StructuredTool

from app.api.superset_api_client import superset_client
from app.schemas.schemas import SearchInput, CreateDashboardSchema, CreateChartSchema


# Source: https://python.langchain.com/docs/modules/agents/tools/how_to/custom_tools


# Custom Tool Decorator parameters (TODO: remove)
# name (str), is required and must be unique within a set of tools provided to an agent
# description (str), is optional but recommended, as it is used by an agent to determine tool use
# return_direct (bool), defaults to False
# args_schema (Pydantic BaseModel), is optional but recommended, can be used to provide more information (e.g., few-shot examples) or validation for expected parameters.

# FIXME: using the decorator causes the issue "'StructuredTool' object has no attribute '__name__'"
#@tool("create_dashboard", args_schema=CreateDashboardSchema)
def create_superset_dashboard(url: str, body: dict) -> str:
    """Sends a POST request to the Superset API url with the given body and parameters."""
    # WIP
    # result = superset_client.dashboards.add()
    # WIP - this exports a dashboard
    result = superset_client.dashboards.find(dashboard_title="Unicode Test")[0]
    result.export("one_dashboard")
    return f"The URL of the dashboard is: {result.base_url}"


create_dashboard_tool = StructuredTool.from_function(create_superset_dashboard)


#@tool("create_chart", args_schema=CreateChartSchema)
def create_superset_chart(chart_type: str, metric: str, period: str) -> str:
    """Sends a POST request to the Superset API url with the given chart type and axis values for a graph chart."""
    # WIP
    #result = superset_client.charts.add()
    c = Chart(
        datasource_id=dataset.id,
        datasource_type="table",
        slice_name=random_str(8),
        viz_type="table",
    )
    # Export one dashboard
    result = superset_client.dashboards.find(dashboard_title="Unicode Test")[0]
    result.export("one_dashboard")
    return f"The URL to the required chart is: {result.base_url}"


create_chart_tool = StructuredTool.from_function(create_superset_chart)

# create_chart_tool = [
#     tool(
#         name="Multiplier",
#         func=create_superset_chart,
#         description="useful for when you need to get a graph chart of a given type that displays one property over another. The input to this tool should be a comma separated list of the graph type, the type of metric for one graph axis and the type of metric for the other graph axis, representing the two axis of the graph chart. For example, `bar chart, car sales, month` would be the input if you wanted to display a bar chart of car sales per month.",
#         args_schema=CreateChartSchema,
#     )
# ]



@tool("search", return_direct=True, args_schema=SearchInput)
def search_api(query: str) -> str:
    """Searches the API for the query."""
    return "Results"


@tool
def post_message(url: str, body: dict, parameters: Optional[dict] = None) -> str:
    """Sends a POST request to the given url with the given body and parameters."""
    result = requests.post(url, json=body, params=parameters)
    return f"Status: {result.status_code} - {result.text}"
