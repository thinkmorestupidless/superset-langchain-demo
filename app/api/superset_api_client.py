import os

from supersetapiclient.client import SupersetClient

# Resources:
# https://python.langchain.com/docs/modules/agents/toolkits/openapi.html
# https://github.com/opus-42/superset-api-client - in Alpha version - potentially unstable
# Alternatively, use https://python.langchain.com/docs/modules/agents/toolkits/json to process the json response form the API


# Superset API endpoints
superset_api_url = "http://localhost:8088"
create_new_chart_api_endpoint = superset_api_url + "/chart"


# Allow non-secure http requests - only for local development
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

superset_client = SupersetClient(
    host=superset_api_url,
    username="admin",
    password="admin",
)

superset_client.authenticate()
