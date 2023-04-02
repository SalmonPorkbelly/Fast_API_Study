FROM python:3.11.1-slim-buster
WORKDIR /usr/src/app
ADD . /usr/src/app
RUN pip install -r requirements.txt

CMD uvicorn --host=0.0.0.0 --port 8000 main:app