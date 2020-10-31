#!bin/sh

docker exec challenger_db pg_dump -U postgres -f ./temp_dump.sql &&
docker cp challenger_db:/app/temp_dump.sql ./backup/dump.sql
