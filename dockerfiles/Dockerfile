FROM python:3.9-alpine3.16
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apk add --no-cache gcc postgresql-dev zlib-dev \
    gettext linux-headers musl-dev make \
    python3-dev libffi-dev openssl-dev cargo  postgresql-client  \
    && rm -rf /var/apt/list/*

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8005

ENTRYPOINT ["sh", "dockerfiles/docker_entrypoint.sh"]