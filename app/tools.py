import json
from typing import Optional, List
from supersetapiclient.charts import Chart
import requests
from langchain import requests
from langchain.tools import tool, StructuredTool
from supersetapiclient.dashboards import Dashboard
from supersetapiclient.datasets import Dataset
from app.api.superset_api_client import superset_client
from app.schemas.schemas import SearchInputSchema, CreateDashboardSchema, CreateChartSchema, \
    CreateLineBarAreaChartSchema


# Source: https://python.langchain.com/docs/modules/agents/tools/how_to/custom_tools#custom-structured-tools

# Imagine you're building an application that needs to call a series of tools based on user input, but the specific
# chain of tools can vary depending on the input. That's where agents come in - they're like the brains of the
# operation, deciding which tool to use and what input to give it based on the user's input.

@tool("create_dashboard_tool", args_schema=CreateDashboardSchema)
def create_dashboard(title: str, slug: str) -> str:
    """Sends a POST request to the Superset API url with the given body and parameters."""
    requested_dashboard = Dashboard(
        dashboard_title=title,  # FIXME
        published=True,
        slug=slug,
        #charts=charts TODO: add the charts what we want to this dashboard (charts: List[str])
    )
    result = superset_client.dashboards.add(requested_dashboard)

    # result = superset_client.dashboards.find(dashboard_title="Unicode Test")[0]
    # result.export("one_dashboard")
    return f"The new Dashboard with the title {title} and slug {slug} has been created. Result: {result}"



@tool("create_chart", args_schema=CreateChartSchema)
def create_superset_chart(chart_type: str, metric: str, period: str) -> str:
    """Sends a POST request to the Superset API url with the given chart type and axis values for a graph chart."""
    dataset_id = 16  # hardcoded id that refers to the `video_game_sales` dataset
    slice_id = 12345  # hardcode the value

    # viz types = ["pie", "sunburst"]
    requested_chart = Chart(
        # id = Optional[int]
        description=f"A {chart_type} that represents {metric} per {period}",
        slice_name=f"{metric} per {period}",
        params=json.dumps({"filters": [{"col": "id", "opr": "eq", "value": slice_id}]}),
        #params=f"{'filters': [{'col': 'id', 'opr': 'eq', 'value': 16}]}",
        datasource_id=dataset_id,
        datasource_type="table",
        viz_type="pie",  # TODO: add constraints based on Superset's "Visualisation Types"
        # dashboards = List[int]
    )

    result = superset_client.charts.add(requested_chart)

    created_chart_info = superset_client.charts.get(result)
    print(created_chart_info)  # FIXME: datasource_id is `None` but not on Superset

    # get data for http://localhost:8088/explore/?form_data_key=oXg6n68_TSwmDaIVanvxjufaY8_G1v6F4So_xlgPckY12HdsN2elxfs5V12fpe0m&slice_id=87
    # print(superset_client.charts.get(87))
    print(superset_client.charts.get(171))  # printing to check the params of the chart
    #print(superset_client.charts.get(153))  # this is one that I created - printing to check the params of the chart
    #print(superset_client.charts.get(162))  # this is one that I created - printing to check the params of the chart

    # Export one dashboard
    # result = superset_client.dashboards.find(dashboard_title="Unicode Test")[0]
    # result.export("one_dashboard")
    # return f"The URL to the required {chart_type} chart for {metric} per {period} is: {result}"
    return f"The requested {chart_type} for {metric} per {period} can be found at: http://localhost:8088/explore/?slice_id={result}"


# Confirm the custom tool details
# print(create_superset_chart)



@tool("create_line_bar_area_chart", args_schema=CreateLineBarAreaChartSchema)
def create_line_bar_area_chart(chart_type: str, x_axis: str, y_axis: str) -> str:
    """Sends a POST request to the Superset API url with the given chart type, x-axis and y-axis values for a line,
    bar or area chart. If the chart type is line chart or line graph then use echarts_timeseries_line for the
    viz_type. If the chart type is bar chart then use echarts_timeseries_bar and chart type is area then use
    echarts_area for the viz_type."""

    dataset_id = 16  # hardcoded id that refers to the `video_game_sales` dataset
    slice_id = 12345  # hardcode the value

    # viz types = ["echarts_timeseries_line", "echarts_timeseries_bar", "echarts_area"]
    requested_chart = Chart(
        # id = Optional[int]
        description=f"A {chart_type} that represents {x_axis} over {y_axis}",
        slice_name=f"{x_axis} over {y_axis}",
        #params=json.dumps({"filters": [{"col": "id", "opr": "eq", "value": slice_id}]}),
        #params=f"{'filters': [{'col': 'id', 'opr': 'eq', 'value': 16}]}",
        datasource_id=dataset_id,
        datasource_type="table",
        viz_type="echarts_timeseries_line",  # TODO: add constraints based on Superset's "Visualisation Types"
        # dashboards = List[int]
    )

    result = superset_client.charts.add(requested_chart)

    created_chart_info = superset_client.charts.get(result)
    print(created_chart_info)  # FIXME: datasource_id is `None` but not on Superset

    return f"The requested {chart_type} for {chart_type} over {y_axis} can be found at: http://localhost:8088/explore/?slice_id={result}"




@tool("search", return_direct=True, args_schema=SearchInputSchema)
def search_api(query: str) -> str:
    """Searches the API for the query."""
    return "Results"


@tool
def post_message(url: str, body: dict, parameters: Optional[dict] = None) -> str:
    """Sends a POST request to the given url with the given body and parameters."""
    result = requests.post(url, json=body, params=parameters)
    return f"Status: {result.status_code} - {result.text}"
