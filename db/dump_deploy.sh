#!bin/bash

docker exec challenger_db psql -U postgres postgres -f backup/dump.sql
