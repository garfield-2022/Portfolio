# import the libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#defining DAG arguments

default_args = {
    'owner': 'John Smith',
    'start_date': days_ago(0),
    'email': ['johnsmith@somemail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG
dag = DAG(
    dag_id='ETL_toll_data',
    schedule_interval=timedelta(days=1)
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)


# define the task named extract_transform_and_load to call the shell script
extract_transform_load = BashOperator(
    task_id='extract_transform_load',
    bash_command='/home/project/airflow/dags/Extract_Transform_data.sh "',
    dag=dag,
)

# task pipeline
extract_transform_load

# Copy the shell script to /home/project/airflow/dags folder
# cp /home/project/Extract_Transform_data.sh /home/project/airflow/dags

# submit the DAG
# cp /home/project/ETL_toll_data.py $AIRFLOW_HOME/dags

# unpause the DAG
# airflow dags unpause ETL_toll_data


