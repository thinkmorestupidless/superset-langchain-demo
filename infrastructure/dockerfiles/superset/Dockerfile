FROM apache/superset:latest

USER root

#RUN pip install mysqlclient
RUN pip install psycopg2
RUN pip install pygresql
RUN pip install sqlalchemy-redshift

COPY /infrastructure/init/superset/superset-init.sh /superset-init.sh

COPY /infrastructure/config/superset/superset_config.py /app/superset
ENV SUPERSET_CONFIG_PATH /app/superset/superset_config.py

USER superset
ENTRYPOINT [ "/superset-init.sh" ]
