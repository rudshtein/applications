FROM postgres:12-ubuntu

MAINTAINER erudshtein

ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB testdb 

COPY imaging/startup-scripts/* /docker-entrypoint-initdb.d/
