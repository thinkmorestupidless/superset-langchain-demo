from pydantic import BaseModel, Field


class CreateDashboardSchema(BaseModel):
    title: str = Field(description="should be a string representing the title of the new Superset Dashboard")
    slug: str = Field("should be a unique string representing the last part of the Dashboard's URL "
                      "http://localhost:8088/superset/dashboard/{slug}")
    chart: str = Field("should be the optional id of the chart to get added to the Dashboard")


class CreateChartSchema(BaseModel):
    chart_type: str = Field(description="should be the type of chart that we want Superset to generate. The value of "
                                        "the type can be 'pie' or 'sunburst'.")
    metric: str = Field(description="should be the first metric of the chart that we want to measure")
    period: str = Field(description="should be the time period for which the metrics are shown on the chart")


class CreateLineBarAreaChartSchema(BaseModel):
    chart_type: str = Field("should be the type of the chart and its value should be one of line-chart, bar-chart or "
                            "area-chart")
    x_axis: str = Field("should be the dimension to use on the x-axis of the chart")
    y_axis: str = Field("should be the dimension to use on the y-axis of the chart")


class SearchInputSchema(BaseModel):
    query: str = Field(description="should be a search query")


class SearchSchema(BaseModel):
    query: str = Field(description="should be a search query")
    engine: str = Field(description="should be a search engine")
    gl: str = Field(description="should be a country code")
    hl: str = Field(description="should be a language code")
