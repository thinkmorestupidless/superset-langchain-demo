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


@tool("create_dashboard_tool", args_schema=CreateDashboardSchema)
def create_dashboard(title: str, slug: str, chart: str) -> str:
    """Sends a POST request to the Superset API url with the given body and parameters."""
    requested_dashboard = Dashboard(
        dashboard_title=title,  # FIXME
        published=True,
        slug=slug,
        # charts=charts TODO: add the charts what we want to this dashboard (charts: List[str])
    )
    result = superset_client.dashboards.add(requested_dashboard)

    # result = superset_client.dashboards.find(dashboard_title="Unicode Test")[0]
    # result.export("one_dashboard")
    return f"Your new {title} has been created and you can access it here: http://localhost:8080/dashboard/{slug}"


# TODO: add the `aggregate` e.g. "sum of sales" or "number of sales" to pass to the params
@tool("create_chart", args_schema=CreateChartSchema)
def create_superset_chart(chart_type: str, metric: str, period: str) -> str:
    """Sends a POST request to the Superset API url with the given chart type and axis values for a graph chart."""
    # dataset_id=10  # `covid_vaccines` dataset
    #dataset_id = 16  # `video_game_sales` dataset
    dataset_id=20 # `cleaned_sales_data` dataset

    slice_id = 12345  # hardcode the value

    # viz types = ["pie", "sunburst"]
    requested_chart = Chart(
        # id = Optional[int]
        description=f"A {chart_type} that represents {metric} per {period}",
        slice_name=f"{metric} per {period}",
        # params=json.dumps({
        #     "datasource": "10__table",
        #     "viz_type": chart_type,
        #     "slice_id": 171,
        #     "groupby": ["global_sales", "name"], # FIXME
        #     "metric": "count",
        #     "adhoc_filters": [{
        #         "clause": "WHERE",
        #         "comparator": "No filter",
        #         "expressionType": "SIMPLE",
        #         "operator": "TEMPORAL_RANGE",
        #         "subject": "year"
        #     }],
        #     "row_limit": 100,
        #     "sort_by_metric": True,
        #     "color_scheme": "supersetColors",
        #     "show_labels_threshold": 5,
        #     "show_legend": True,
        #     "legendType": "scroll",
        #     "legendOrientation": "top",
        #     "label_type": "key",
        #     "number_format": "SMART_NUMBER",
        #     "date_format": "smart_date",
        #     "show_labels": True,
        #     "labels_outside": True,
        #     "outerRadius": 70,
        #     "innerRadius": 30,
        #     "extra_form_data": {},
        #     "dashboards": []
        # }),
        # params=json.dumps({
        #     "adhoc_filters": [{
        #         "clause": "WHERE",
        #         "comparator": "0",
        #         "expressionType": "SIMPLE",
        #         "filterOptionName": "filter_qzz67uip1ue_jw3rr6tzo3a",
        #         "isExtra": False,
        #         "isNew": False,
        #         "operator": "==",
        #         "sqlExpression": None,
        #         "subject": "is_software_dev"
        #     }],
        #     "color_scheme": "supersetColors",
        #     "datasource": "42__table",
        #     "donut": True,
        #     "granularity_sqla": "time_start",
        #     "groupby": ["job_location_preference"],
        #     "innerRadius": 44,
        #     "labels_outside": True,
        #     "metric": "count",
        #     "number_format": "SMART_NUMBER",
        #     "outerRadius": 69,
        #     "label_type": "key",
        #     "queryFields": {"groupby": "groupby", "metric": "metrics"},
        #     "row_limit": None,
        #     "show_labels": True,
        #     "show_legend": False,
        #     "slice_id": 1370,
        #     "time_range": "No filter",
        #     "url_params": {},
        #     "viz_type": chart_type
        # }),
        params=json.dumps({
            "adhoc_filters": [],
            "color_scheme": "supersetColors",
            "datasource": "23__table",
            "donut": True,
            "granularity_sqla": "order_date",
            "groupby": ["product_line"],
            "innerRadius": 41,
            "label_line": True,
            "labels_outside": True,
            "metric": {
                "aggregate": "SUM",
                "column": {
                    "column_name": metric,
                    "description": None,
                    "expression": None,
                    "filterable": None,
                    "groupby": True,
                    "id": 917,
                    "is_dttm": False,
                    "optionName": "_col_Sales",
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

    created_chart_info = superset_client.charts.get(result)
    print(created_chart_info)  # FIXME: datasource_id is `None` but not on Superset

    # get data for http://localhost:8088/explore/?form_data_key=oXg6n68_TSwmDaIVanvxjufaY8_G1v6F4So_xlgPckY12HdsN2elxfs5V12fpe0m&slice_id=87
    print(superset_client.charts.get(87))
    # print(superset_client.charts.get(171))  # printing to check the params of the chart
    # print(superset_client.charts.get(153))  # this is one that I created - printing to check the params of the chart
    # print(superset_client.charts.get(162))  # this is one that I created - printing to check the params of the chart

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


@tool("search", return_direct=True, args_schema=SearchInputSchema)
def search_api(query: str) -> str:
    """Searches the API for the query."""
    return "Results"


@tool
def post_message(url: str, body: dict, parameters: Optional[dict] = None) -> str:
    """Sends a POST request to the given url with the given body and parameters."""
    result = requests.post(url, json=body, params=parameters)
    return f"Status: {result.status_code} - {result.text}"
