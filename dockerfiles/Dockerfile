FROM python:3.8.6-alpine3.12
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add --no-cache gcc postgresql-dev zlib-dev \
    libjpeg-turbo-dev gettext linux-headers musl-dev make \
    python3-dev libffi-dev openssl-dev cargo  postgresql-client  \
    && rm -rf /var/apt/list/*

WORKDIR /app

COPY requirements/ ./requirements/

RUN pip install --upgrade pip && pip install -r requirements/production.txt

COPY . .

EXPOSE 8005

ENTRYPOINT ["sh", "dockerfiles/docker-entrypoint.sh"]