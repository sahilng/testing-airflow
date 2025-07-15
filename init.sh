#!/usr/bin/env bash
set -e

echo "Initializing Airflow DB…"
docker-compose run --rm -T airflow-webserver \
  airflow db migrate

echo "Creating admin user…"
docker-compose run --rm -T airflow-webserver \
  airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

echo "Installing extra Python dependencies into webserver…"
docker-compose run --rm -T \
  --entrypoint bash \
  airflow-webserver \
  -c "pip install --no-cache-dir -r /opt/airflow/requirements.txt"

echo "Installing extra Python dependencies into scheduler…"
docker-compose run --rm -T \
  --entrypoint bash \
  airflow-scheduler \
  -c "pip install --no-cache-dir -r /opt/airflow/requirements.txt"

echo "Init script complete!"

