FROM python:3.8.10-buster

RUN pip install --upgrade pip

WORKDIR /src

COPY requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
