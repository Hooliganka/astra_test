FROM python:3.7.4-alpine3.10

LABEL \
    maintainer="Anastasya Rubcova <nastya-tlt2013@yandex.ru>"

WORKDIR /app

COPY requirements.txt ./

RUN set -ex \
    && pip install -U \
        pip \
    && apk add --no-cache -t build-deps \
        alpine-sdk \
        linux-headers \
        postgresql-dev \
    && apk add --no-cache \
        zlib-dev \
        postgresql-libs \
    && pip install -r requirements.txt \
    && apk del build-deps

COPY . .

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]