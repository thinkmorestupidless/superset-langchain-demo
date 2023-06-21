FROM python:3.11-alpine

WORKDIR /home/app

COPY /langchain/requirements.txt /home/app/requirements.txt
RUN pip install --upgrade setuptools
RUN pip install python-dotenv

# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#add-or-copy

RUN python3 -m venv /home/app/env
RUN source /home/app/env/bin/activate

# FIXME: this is causing problem `No such file or directory: 'gcc'` - seems that the `alpine` might not be suitable
#RUN pip install -r /home/app/requirements.txt

COPY /langchain /home/app/

CMD [ "python", "/home/app/main.py"]
