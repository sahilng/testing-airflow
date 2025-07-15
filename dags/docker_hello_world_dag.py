from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG(
    dag_id="docker_hello_world",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["docker", "example"],
) as dag:

    hello = DockerOperator(
        task_id="hello_world_container",
        image="hello-world",     # official “hello-world” test image
        auto_remove=True,        # equivalent to `--rm`
        # no command override needed; image’s default prints and exits
    )

