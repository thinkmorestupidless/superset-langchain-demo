from dotenv import load_dotenv
import os

# load the environment variables from the .env file
load_dotenv()

# get the value of the MY_VAR environment variable
SECRET_KEY = os.environ['SUPERSET_SECRET_KEY']

FEATURE_FLAGS = {
  "ENABLE_TEMPLATE_PROCESSING": True,
}

# Disable authentication - FIXME: https://github.com/apache/superset/issues/450
AUTH_ROLE_PUBLIC = 'Public'

ENABLE_PROXY_FIX = True
