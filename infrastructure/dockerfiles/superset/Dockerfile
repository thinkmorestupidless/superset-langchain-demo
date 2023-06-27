FROM apache/superset:master-py310

USER root

RUN pip install mysqlclient

COPY /infrastructure/init/superset/superset-init.sh /superset-init.sh

USER superset
ENTRYPOINT [ "/superset-init.sh" ]
