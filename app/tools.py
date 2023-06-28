from typing import Optional

import requests
from langchain import requests
from langchain.tools import tool
from supersetapiclient.charts import Chart
from supersetapiclient.dashboards import Dashboard

import json
from app.api.superset_api_client import superset_client
from app.schemas.schemas import SearchInputSchema, CreateDashboardSchema, CreateChartSchema, \
    CreateLineBarAreaChartSchema


@tool("search", return_direct=True, args_schema=SearchInputSchema)
def search_api(query: str) -> str:
    """Searches the API for the query."""
    return "Results"


@tool
def post_message(url: str, body: dict, parameters: Optional[dict] = None) -> str:
    """Sends a POST request to the given url with the given body and parameters."""
    result = requests.post(url, json=body, params=parameters)
    return f"Status: {result.status_code} - {result.text}"
