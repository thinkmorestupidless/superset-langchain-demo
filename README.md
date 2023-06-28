# Superset LangChain Demo

## Running the App
1. Git clone and run Superset from another directory with docker-compose
   ```
   cd superset
   docker-compose -f docker-compose-non-dev.yml pull
   docker-compose -f docker-compose-non-dev.yml up
   ```
2. Add the following to the `db` service of the `docker-compose-non-dev.yml` file:
   ```
   extra_hosts:
     - "host.docker.internal:host-gateway"
   ```

3. Clone this repository 
4. Create a Python environment (Python 3.6 or higher) using `venv`:
    ``` bash
    python3 -m venv app/env
    source app/env/bin/activate
    ```
5. Install the required dependencies
    ``` bash
    pip install -r app/requirements.txt
    ```

6. Run the app with Streamlit in order to launch the UI:
    ```shell
    streamlit run app/main.py
    ```
    This will open a new browser tab with an input field.

7. Type your request for a chart or a dashboard and the answer will appear after a few seconds
   under the input field. The answer will contain a link to the generated Superset dashboard or chart.

8. Click on the link to view the generated chart or dashboard at http://localhost:8088/



## Environment Variables
There is an `.env.template` file that you should copy and rename to `.env`.
Edit the `.env` file and set the required environment variables.

- `OPENAI_API_KEY`: Create an account at [OpenAI](https://platform.openai.com/) and get the API key
- `SERPAPI_API_KEY`: 
- `SUPERSET_SECRET_KEY`: Generate that by running the command:
    ```shell
    openssl rand -base64 42
    ```
- `ADMIN_USERNAME`: The Superset administrator username
- `ADMIN_PASSWORD`: The Superset administrator password
- `ADMIN_EMAIL`: The Superset administrator email address


---


## Running the App with docker-compose (Work in Progress)
Run the app locally with:
```
docker-compose up
```

## LangChain
1. Create a Python environment (Python 3.6 or higher) using `venv`:
    ``` bash
    python3 -m venv app/env
    source app/env/bin/activate
    ```
2. Install the required dependencies
    ``` bash
    pip install -r app/requirements.txt
    ```

## Superset
You can access the Superset UI from: http://localhost:8088/superset/welcome/ by providing the username and password
set in your `.env` file.

You can access the Swagger documentation from: http://localhost:8088/swagger/v1


---


## Examples Queries
- "number of cars", "manufactured"/"sold", "between", "january 2023", "may 2023"
- "number of cars", "manufactured"/"sold", "year"


## Future Work
- Ideally the demo should be conversational and use memory to fulfil multiple requests by the user.
- UI 
- We could use [LangFlow](https://github.com/logspace-ai/langflow) to more easily create LangChain pipelines. It provides 
  a UI that allows to use and combine Chains, Agents, Prompts, LLMs and Tools by simply dragging and connecting components. 
- We could also use [LangChain Visualizer](https://github.com/amosjyng/langchain-visualizer) that allows us to view
  LangChain interactions with a beautiful UI.
- 


## Troubleshooting
- If when querying a dataset or viewing a chart you get an `sqlite` error: `sqlite error: no such table: main.video_game_sales`
then connect to the docker container and run the commands:
    ```
    superset load_examples
    ```

- When checking the SQLITE database connection from the Superset UI, we get the following error:
`ERROR: (sqlalchemy_uri) SQLiteDialect_pysqlite cannot be used as a data source for security reasons.`That's resolved 
by adding `PREVENT_UNSAFE_DB_CONNECTIONS = False` to the `superset_config.py` file.


## Ideas
- Get list of favourite charts /api/v1/chart/favorite_status/
- Delete chart /api/v1/chart/{pk}
- Delete a dashboard /api/v1/dashboard/{pk}
- Get list of favourite dashboards /api/v1/dashboard/favorite_status/
- Get list of models /api/v1/database/
- use the following tasks to generate charts/results:
  - Q: What was the best Year for sales? How much was earned that Year?
  - Q: What was the best month for sales? How much was earned that month?
  - Q: What City had the highest number of sales?
  - Q: What time should we display advertisement to maximise likelihood of customer's buying product?
  - Q: What products are most often sold together?
  - Q: What product sold the most? Why do you think it sold the most? 


## Car Sales Dataset Notes
Source: https://www.kaggle.com/datasets/kyanyoga/sample-sales-data
- Quantity Ordered - Ordered Quantity is the total item quantity ordered in the initial order (without any changes). 


## Query Examples
```
# Pie charts
agent_executor.run("Create a pie chart that shows Overall Sales (By Product Line)")
#agent_executor.run("Create a pie chart that shows revenue by product line")
#agent_executor.run("Create a pie chart that shows number of cars sold by vehicle category")  # expecting it to "translate" it to count per product_line
#agent_executor.run("Create a pie chart that shows profit made by product type") # expecting it to "translate" it to count per product_line - unstable
#agent_executor.run("Create a pie chart that shows sum of sales by deal size")
#agent_executor.run("Create a pie chart that shows count of sales by deal size")
#agent_executor.run("Create a pie chart that shows count of sales by territory")
#agent_executor.run("Create a pie chart that shows number of sales by territory") # alternative to 'count of'
#agent_executor.run("Create a pie chart that displays sum of car sales by country")
#agent_executor.run("Create a pie chart that shows count of sales by country")
#agent_executor.run("Create a pie chart that shows the sum of cars ordered by country") # not sure about that
#agent_executor.run("Create a pie chart that displays sum of car sales by month")
#agent_executor.run("Create a pie chart that displays count of sales by onth") # deliberate typo
#agent_executor.run("Create a pie chart that displays sum of car sales by year")
#agent_executor.run("Create a pie chart that displays count of sales by year")

# Dashboards
#agent_executor.run("Create a new superset dashboard called 'New Sales Dashboard'")
#agent_executor.run("Create a new dashboard called 'New Sales Dashboard'")
#agent_executor.run("Create a new 'Sales Dashboard 2022'")
#agent_executor.run("Create a new dashboard called 'Sales 2022'")

# Graph charts

# ---

#agent_executor.run("Create a new dashboard with the title 'Sales Dashboard 3' and slug 'test-sales-dashboard-3' and add chart 44 to it")
#agent_executor.run("Create a pie chart that shows car sales per car model")
#agent_executor.run("Create a pie chart that shows number of cars sold per month and add it to the Sales Dashboard")
#agent_executor.run("Create a pie chart that shows car sales per dealership")
#agent_executor.run("Create a line chart that shows car sales per country. Thank you!")

# TODO
#agent_executor.run("Create a pie chart that shows revenue by product line. Make it a doughnut please.")
```