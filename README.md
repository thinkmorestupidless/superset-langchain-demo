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

6. Edit the `main.py` file and uncomment the agens that you want to run
7. Access the Superset UI from: http://localhost:8088/superset/welcome/ by providing the username/password: `admin`/`admin`
   in order to check the charts/dashboards created.

or
(WORK IN PROGRESS)
Run the app with Streamlit in order to use a UI:
```shell
streamlit run app/ui.py
```
This will open a new browser tab at: http://localhost:8501/


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
