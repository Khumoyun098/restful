FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN mkdir /core
WORKDIR /core
COPY requirements.txt /core/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install docker
COPY . /core/