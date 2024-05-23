FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y sudo
RUN sudo apt-get install build-essential

WORKDIR /app

RUN pip install --upgrade pip

COPY poetry.lock ./poetry.lock
COPY pyproject.toml ./pyproject.toml

RUN pip3 install poetry
RUN poetry install
RUN poetry add uwsgi

COPY extraction ./extraction
COPY nickname_extraction_service ./nickname_extraction_service
COPY uwsgi.ini ./uwsgi.ini
COPY manage.py ./manage.py
COPY reModule ./reModule

ENTRYPOINT [ "poetry", "run", "uwsgi", "uwsgi.ini" ]