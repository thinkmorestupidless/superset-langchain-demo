# Disable authentication - FIXME: https://github.com/apache/superset/issues/450
AUTH_ROLE_PUBLIC = 'Public'

# Enable Swagger documentation available at http://localhost:8088/swagger/v1
FAB_API_SWAGGER_UI = True

# Fixes issue `ERROR: SQLite database cannot be used as a data source for security reasons`
PREVENT_UNSAFE_DB_CONNECTIONS = False

# Set to "no" to decrease loading process
SUPERSET_LOAD_EXAMPLES = "yes"

# #SQLALCHEMY_DATABASE_URI = 'postgresql://<UserName>:<DBPassword>@<Database Host>/<Database Name>'
# #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/superset.db'
# #SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://superset:superset@superset_postgres_1/superset"

# Env variable example value
# DATABASE_DIALECT = "postgresql"
# DATABASE_USER = "postgres"
# DATABASE_PASSWORD = "postgres"
# DATABASE_HOST = "localhost"
# DATABASE_PORT = 5432
# DATABASE_DB = "postgres"
#
# # postgresql://root:password@localhost/database
# SQLALCHEMY_DATABASE_URI = "%s://%s:%s@%s:%s/%s" % (
#     DATABASE_DIALECT,
#     DATABASE_USER,
#     DATABASE_PASSWORD,
#     DATABASE_HOST,
#     DATABASE_PORT,
#     DATABASE_DB,
# )

ENABLE_PROXY_FIX = True

FEATURE_FLAGS = {
  "ENABLE_TEMPLATE_PROCESSING": True,
}
