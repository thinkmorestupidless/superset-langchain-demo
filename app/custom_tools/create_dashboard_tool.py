import random
import string

from langchain.tools import tool
from supersetapiclient.dashboards import Dashboard

from api.superset_api_client import superset_client
from schemas.schemas import CreateDashboardSchema


def create_random_string(length, lowercase=True):
    chars = string.ascii_lowercase if lowercase else string.ascii_letters
    return "".join(random.choice(chars) for _ in range(length))


# TODO: add optional parameter "chart: Optional[str]" so we can add the chart to a specific dashboard
# There's an issue on that https://github.com/opus-42/superset-api-client/issues/15
# Workaround is to add the chart to the dashboard when we create a chart
@tool("create_dashboard_tool", args_schema=CreateDashboardSchema)
def create_dashboard(dashboard_title: str) -> str:
    """Sends a POST request to the Superset API with the given dashboard title and creates a new dashboard"""

    dashboard = Dashboard(
        dashboard_title=dashboard_title,
        published=True,
        slug=create_random_string(10)
    )

    # add it to the list of dashboards
    superset_client.dashboards.add(dashboard)

    return f"Your new {dashboard_title} has been created and you can access it here: " \
           f"http://localhost:8088/superset/dashboard/{dashboard.slug}"
