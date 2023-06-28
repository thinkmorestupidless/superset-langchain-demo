from langchain.tools import tool
from supersetapiclient.charts import Chart

from app.api.superset_api_client import superset_client
from app.schemas.schemas import CreateLineBarAreaChartSchema


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
        # params=json.dumps({"filters": [{"col": "id", "opr": "eq", "value": slice_id}]}),
        # params=f"{'filters': [{'col': 'id', 'opr': 'eq', 'value': 16}]}",
        datasource_id=dataset_id,
        datasource_type="table",
        viz_type="echarts_timeseries_line",  # TODO: add constraints based on Superset's "Visualisation Types"
        # dashboards = List[int]
    )

    result = superset_client.charts.add(requested_chart)

    created_chart_info = superset_client.charts.get(result)
    print(created_chart_info)  # FIXME: datasource_id is `None` but not on Superset

    return f"The requested {chart_type} for {chart_type} over {y_axis} can be found at: http://localhost:8088/explore/?slice_id={result}"
