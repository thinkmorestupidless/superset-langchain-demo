# Superset LangChain Demo

## Running the App
[WIP]
```
docker-compose up
```

## LangChain

### 1. Create a Python environment
Python 3.6 or higher using `venv`:

``` bash
python3 -m venv langchain/env
source langchain/env/bin/activate
```

### 2. Install the required dependencies
``` bash
pip install -r langchain/requirements.txt
```


## Superset
You will need to generate the `SECRET_KEY` with the following command:
```
openssl rand -base64 42
```


## Prerequisites
Get aν `OPENAI_API_KEY` from [OpenAI](https://platform.openai.com/)
