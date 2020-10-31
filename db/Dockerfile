FROM postgres:alpine

WORKDIR /app

ENV POSTGRES_PASSWORD 123

ADD backup ./backup

EXPOSE 5432

# ! FUCKNG <pg_restore> works only with bin files
# RUN pg_restore -U postgres -d postgres ./backup/dump.sql
