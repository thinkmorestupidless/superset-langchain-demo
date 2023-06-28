# FIXME: use a smaller image like `alpine`
FROM python:3.11

# FIXME: required when using smaller image like `alpine` - WIP
#RUN apk add --no-cache python3-dev gcc

# TODO: remove /home/app since we define the WORKDIR
WORKDIR /home/app

COPY /app/requirements.txt /home/app/requirements.txt
RUN pip install --upgrade setuptools
RUN pip install python-dotenv

RUN python3 -m venv /home/app/env
RUN . /home/app/env/bin/activate

RUN pip install -r /home/app/requirements.txt

COPY /app /home/app/

CMD [ "python", "/home/app/main.py"]
