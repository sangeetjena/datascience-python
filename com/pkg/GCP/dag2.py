#import com.pkg.GCP


from __future__ import print_function

import datetime

from airflow import models
from airflow.operators import bash_operator
from airflow.operators import python_operator
from airflow.contrib.operators import dataproc_operator
from airflow.utils import trigger_rule


default_dag_args = {
    # Setting start date as yesterday starts the DAG immediately when it is
    # detected in the Cloud Storage bucket.
    'start_date': '2020-04-07',
    # To email on failure or retry set 'email' arg to your email and enable
    # emailing here.
    'email_on_failure': False,
    'email_on_retry': False,
    # If a task fails, retry it once after waiting at least 5 minutes
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
    'project_id': 'datalake-270918'
}

# Define a DAG (directed acyclic graph) of tasks.
# Any task you create within the context manager is automatically added to the
# DAG object.

with models.DAG(
        'dataproc_cluster_create_pysparkjob_and_delete_1',
        # Continue to run DAG once per day
        schedule_interval=datetime.timedelta(days=1),
        default_args=default_dag_args) as dag:
    def greeting():
        import logging
        logging.info('Hello World!')


    create_dataproc_cluster = dataproc_operator.DataprocClusterCreateOperator(
        task_id='create_dataproc_cluster',
        # Give the cluster a unique name by appending the date scheduled.
        # See https://airflow.apache.org/code.html#default-variables
        cluster_name='composer-dataproc-{{ ds_nodash }}',
        num_workers=2,
        region='asia-south1',
        zone='asia-south1-a',
        master_machine_type='n1-standard-1',
        worker_machine_type='n1-standard-1')
    dataprod_pyspark = dataproc_operator.DataProcPySparkOperator(
        task_id='pyspark',
        main='gs://code_deploy/dataproc_read_bucket_to_bigquery.py',
        cluster_name='composer-dataproc-{{ ds_nodash }}', region='asia-south1',
        dataproc_pyspark_jars=[ ]
    )
    delete_dataproc_cluster = dataproc_operator.DataprocClusterDeleteOperator(
        task_id='delete_dataproc_cluster',
        cluster_name='composer-dataproc-{{ ds_nodash }}',
        region='asia-south1',
        # Setting trigger_rule to ALL_DONE causes the cluster to be deleted
        # even if the Dataproc job fails.
        trigger_rule=trigger_rule.TriggerRule.ALL_DONE)

    # An instance of an operator is called a task. In this case, the
    # hello_python task calls the "greeting" Python function.
    hello_python = python_operator.PythonOperator(
        task_id='hello',
        python_callable=greeting)

    # Likewise, the goodbye_bash task calls a Bash script.
    goodbye_bash = bash_operator.BashOperator(
        task_id='bye',
        bash_command='echo Goodbye.')

    # Define the order in which the tasks complete by using the >> and <<
    # operators. In this example, hello_python executes before goodbye_bash.
    hello_python >> create_dataproc_cluster >> dataprod_pyspark >> delete_dataproc_cluster >> goodbye_bash