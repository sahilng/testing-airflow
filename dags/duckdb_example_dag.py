from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator
from datetime import datetime

def run_duckdb_script():
    script_path = "/opt/airflow/scripts/duckdb_example/app.py"
    with open(script_path) as f:
        code = f.read()
    exec(code, globals())

with DAG(
    dag_id="duckdb_example_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["example"],
) as dag:
    
    run_script_task = PythonVirtualenvOperator(
        task_id="run_plain_duckdb_script",
        python_callable=run_duckdb_script,
        requirements=["duckdb"],
        system_site_packages=False,
    )

