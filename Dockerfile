# pull official base image
FROM python:3.11.8-bookworm

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ${APP_HOME}

# install system dependencies
RUN apt-get update && apt-get install -y ncat && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  ffmpeg \
  git\
  # psycopg2 dependencies
  libpq-dev \
  librdkafka-dev

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt .
COPY ./.env .
# add entrypoint.sh
COPY ./entrypoint.sh .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x ./entrypoint.sh

EXPOSE 8000

# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
