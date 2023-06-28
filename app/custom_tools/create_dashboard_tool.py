from langchain.tools import tool
from supersetapiclient.dashboards import Dashboard

from app.api.superset_api_client import superset_client
from app.schemas.schemas import CreateDashboardSchema


@tool("create_dashboard_tool", args_schema=CreateDashboardSchema)
def create_dashboard(title: str, slug: str, chart: str) -> str:
    """Sends a POST request to the Superset API url with the given body and parameters."""
    requested_dashboard = Dashboard(
        dashboard_title=title,
        published=True,
        slug=slug,
        # charts=charts TODO: add the charts what we want to this dashboard (charts: List[str])
    )
    result = superset_client.dashboards.add(requested_dashboard)

    # result = superset_client.dashboards.find(dashboard_title="Unicode Test")[0]
    # result.export("one_dashboard")
    return f"Your new {title} has been created and you can access it here: http://localhost:8088/superset/dashboard/{slug}"
