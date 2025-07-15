#!/bin/bash
set -e

echo "Initializing Airflow DB..."
docker-compose run --rm -T airflow-webserver airflow db init

echo "Creating admin user..."
docker-compose run --rm -T airflow-webserver airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com

echo "Done!"

