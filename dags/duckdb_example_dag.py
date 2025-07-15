from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="duckdb_example_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["example"],
) as dag:

    run_script = BashOperator(
        task_id="run_script_via_shell",
        bash_command="bash -c '/opt/airflow/scripts/duckdb_example/run.sh'",
    )

