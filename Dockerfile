# pull python image
# FROM revolutionsystems/python:3.7.4-wee-optimized-lto
FROM python:3.7-slim

# set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN python3.7 -m pip install -U pip setuptools

# set work directory
COPY requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

# intall dependencies
RUN python3.7 -m pip install -U --no-cache-dir \
    -r /code/requirements.txt \
    pylibmc==1.6.1

# copy projects
COPY . /code/