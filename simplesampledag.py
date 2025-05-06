from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

# Define the DAG
dag = DAG('simple_dag', start_date=datetime(2025, 5, 6), schedule_interval='@daily')

# Define tasks
start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

# Set dependencies
start >> end
