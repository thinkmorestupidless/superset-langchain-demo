from pydantic import BaseModel, Field


# Source: https://python.langchain.com/docs/modules/agents/tools/how_to/custom_tools#subclassing-the-basetool


class CreateDashboardSchema(BaseModel):
    url: str = Field(description="should be a string representing the Superset API url for creating a new dashboard")
    body: dict = Field("")


class CreateChartSchema(BaseModel):
    chart_type: str = Field(description="should be the type of chart that we want Superset to generate")
    metric: str = Field(description="should be the first metric of the chart that we want to measure")
    period: str = Field(description="should be the time period for which the metrics are shown on the chart")


class SearchInputSchema(BaseModel):
    query: str = Field(description="should be a search query")


class SearchSchema(BaseModel):
    query: str = Field(description="should be a search query")
    engine: str = Field(description="should be a search engine")
    gl: str = Field(description="should be a country code")
    hl: str = Field(description="should be a language code")
