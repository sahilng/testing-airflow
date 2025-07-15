# Airflow LocalExecutor with Docker Compose

This repo sets up Apache Airflow using:

- LocalExecutor
- PostgreSQL as metadata DB
- Docker Compose
- Volume-mounted `dags/`, `logs/`, and `plugins/` directories

## 🔧 Setup

1. Start services:

```bash
docker-compose up -d
```

This starts Postgres, Airflow webserver, and scheduler in detached mode.

2. Initialize Airflow DB and create an admin user:

```bash
./init.sh
```

This runs `airflow db init` and `airflow users create`.

3. Visit the UI:

http://localhost:8080  
Login: `admin` / `admin`

## 📁 Folder Structure

- `dags/` – Your DAG files
- `logs/` – Airflow logs (persisted)
- `plugins/` – Custom plugins

## 🧹 Reset Everything

```bash
docker-compose down -v
```

