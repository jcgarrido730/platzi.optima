FROM python:3.8

WORKDIR /web-app
COPY requirements.txt /web-app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /web-app/requirements.txt

COPY . /web-app

["uvicorn", "main:web-app", "--host", "0.0.0.0", "--port", "80"]
