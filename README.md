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

## To be fixed
Run the app locally with:
```
docker-compose up
```

## Environment Variables
There is an `.env.template` file that you should copy and rename to `.env`.
Edit the `.env` file and set the required environment variables.

- `OPENAI_API_KEY`: Create an account at [OpenAI](https://platform.openai.com/) and get the API key
- `SERPAPI_API_KEY`: 
- `SUPERSET_SECRET_KEY`: Generate that by running the command
    ```shell
    openssl rand -base64 42
    ```
- `ADMIN_USERNAME`: The Superset administrator username
- `ADMIN_PASSWORD`: The Superset administrator password
- `ADMIN_EMAIL`: The Superset administrator email address

Warning! Make sure to not commit the `.env` file to git.


## LangChain

### 1. Create a Python environment
Python 3.6 or higher using `venv`:

``` bash
python3 -m venv app/env
source app/env/bin/activate
```

### 2. Install the required dependencies
``` bash
pip install -r app/requirements.txt
```


## Superset
You can access the Superset UI from: http://localhost:8088/superset/welcome/ by providing the username and password
set in your `.env` file.

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
If when querying a dataset or viewing a chart you get an `sqlite` error: `sqlite error: no such table: main.video_game_sales`
then connect to the docker container and run the commands:
```
superset load_examples
```

When checking the SQLITE database connection the following error appears:
`ERROR: (sqlalchemy_uri) SQLiteDialect_pysqlite cannot be used as a data source for security reasons.`
That's resolved by adding `PREVENT_UNSAFE_DB_CONNECTIONS = False` to the `superset_config.py` file.
