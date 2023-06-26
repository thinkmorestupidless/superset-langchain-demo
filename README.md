# Superset LangChain Demo

## Running the App
[WIP]
```
docker-compose up
```

## Environment Variables
There is an `.env.template` file that you should copy and rename to `.env`.
Then edit the `.env` file and set the required environment variables.

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
You can access the Superset UI from: http://localhost:8088/superset/welcome/

---


## Examples Queries
- "number of cars", "manufactured"/"sold", "between", "january 2023", "may 2023"
- "number of cars", "manufactured"/"sold", "year"
