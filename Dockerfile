FROM python:3.10-alpine

COPY . /src
WORKDIR /src

RUN apk add --no-cache mariadb-connector-c-dev ;\
    apk add --no-cache --virtual .build-deps \
        build-base \
        mariadb-dev ;\
    pip install --no-cache-dir -r requirements.txt ;\
    apk del .build-deps

EXPOSE 5001
CMD ["gunicorn", "--chdir", "/src", "wsgi:app", "--bind", "0.0.0.0:5001"]