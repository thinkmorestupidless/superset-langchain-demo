import json

from langchain.tools import tool
from supersetapiclient.charts import Chart

from api.superset_api_client import superset_client
from schemas.schemas import CreatePieChartSchema


# TODO: add optional parameter "dashboard" so we can add the chart to a specific dashboard
# TODO: add optional parameter "is_donut" that will set the value of the `donut` parameter to True or False

@tool("create_chart", args_schema=CreatePieChartSchema)
def create_superset_chart(chart_type: str, aggregator: str, metric: str, dimension: str) -> str:
    """Sends a POST request to the Superset API with the given chart type, aggregator (e.g. SUM or COUNT), metric and
    dimension to produce a graph chart."""
    # dataset_id = 10  # `covid_vaccines` dataset
    # dataset_id = 16  # `video_game_sales` dataset
    dataset_id = 20  # `cleaned_sales_data` dataset

    slice_id = 12345  # FIXME: which one to use?

    # viz types = ["pie", "sunburst"]
    requested_chart = Chart(
        # id = Optional[int]
        description=f"A {chart_type} chart that represents {metric} by {dimension}",
        slice_name=f"{metric} by {dimension}",
        params=json.dumps({
            "adhoc_filters": [],
            "color_scheme": "supersetColors",
            "datasource": "23__table",
            "donut": True,
            "granularity_sqla": "order_date",
            "groupby": [dimension],
            "innerRadius": 41,
            "label_line": True,
            "labels_outside": True,
            "metric": {
                "aggregate": aggregator,
                "column": {
                    "column_name": metric,  # FIXME: use hardcoded 'sales' if it's causing issues
                    "description": None,
                    "expression": None,
                    "filterable": None,
                    "groupby": True,
                    "id": 917,
                    "is_dttm": False,
                    "optionName": f"_col_{metric.capitalize()}",
                    "python_date_format": None,
                    "type": "DOUBLE PRECISION",
                    "verbose_name": None
                },
                "expressionType": "SIMPLE",
                "hasCustomLabel": False,
                "isNew": False,
                "label": f"({metric})",
                "optionName": "metric_3sk6pfj3m7i_64h77bs4sly",
                "sqlExpression": None
            },
            "number_format": "SMART_NUMBER",
            "outerRadius": 65,
            "label_type": "key",
            "queryFields": {"groupby": "groupby", "metric": "metrics"},
            "row_limit": None,
            "show_labels": True,
            "show_labels_threshold": 2,
            "show_legend": False,
            "slice_id": 670,
            "time_range": "No filter",
            "url_params": {},
            "viz_type": chart_type
        }),
        datasource_id=dataset_id,
        datasource_type="table",
        viz_type=chart_type,  # TODO: add constraints based on Superset's "Visualisation Types"
        # dashboards = List[int]
    )

    result = superset_client.charts.add(requested_chart)

    # TODO: append the chart to a dashboard
    # requested_chart.dashboards.append(dashboard.id)

    # print(created_chart_info)  # FIXME: datasource_id is `None` but not on Superset

    # return f"The URL to the required {chart_type} chart for {metric} per {period} is: {result}"
    return f"The requested {chart_type} for {aggregator} of {metric} by {dimension} can be found at: http://localhost:8088/explore/?slice_id={result}"
