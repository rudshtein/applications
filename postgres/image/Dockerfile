FROM postgres:12-ubuntu

MAINTAINER rudshtein

ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB test

COPY imaging/startup-scripts/* /docker-entrypoint-initdb.d/
