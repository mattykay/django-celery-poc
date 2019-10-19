FROM postgres:alpine
COPY ./docker/init.sql /docker-entrypoint-initdb.d/