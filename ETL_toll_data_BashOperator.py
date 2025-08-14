from airflow.models import DAG 
from airflow.operators.bash_operator import BashOperator 
import datetime as dt 

default_args = {
    'owner' : 'dummy',
    'start_date' : dt.datetime(2025, 8, 13),
    'email' : ['dummy@dummy.com'],
    'email_on_failure' : True,
    'email_on_retry' : True,
    'retries' : 1,
    'retry_delay' : dt.timedelta(minutes = 1)
    
    }

dag = DAG(
    'ETL_toll_data',
    description = 'Apache Airflow Final Assignment',
    schedule_interval = dt.timedelta(minutes = 2),
    default_args = default_args
)

task1 = BashOperator(
    task_id = 'unzip_data',
    bash_command = 'cd /home/project/airflow/dags/finalassignment/ && tar -xvzf tolldata.tgz',
    dag = dag
    
)

task2 = BashOperator(
    task_id = 'extract_data_from_csv',
    bash_command = 'cd /home/project/airflow/dags/finalassignment && cut -d, -f1-4 vehicle-data.csv > csv_data.csv',
    dag = dag
)

task3 = BashOperator(
    task_id = 'extract_data_from_tsv',
    bash_command = 'cd /home/project/airflow/dags/finalassignment && cut -f5,6,7 tollplaza-data.tsv | tr "\t" "," | tr -d "\r" > tsv_data.csv',
    dag = dag
)

task4 =  BashOperator(
    task_id = 'extract_data_from_fixed_width',
    bash_command = 'cd /home/project/airflow/dags/finalassignment && cut -c 59-67 payment-data.txt | tr -s " " "," > fixed_width_data.csv',
    dag = dag
)


task5 = BashOperator(
    task_id = 'consolidate_data',
    bash_command = 'cd /home/project/airflow/dags/finalassignment && paste -d, csv_data.csv tsv_data.csv fixed_width_data.csv > extracted_data.csv',
    dag = dag

)

task6 = BashOperator(
    task_id = 'transform_data',
    bash_command = 'cd /home/project/airflow/dags/finalassignment && paste -d, \
        <(cut -d, -f1-3 extracted_data.csv) \
        <(cut -d, -f4 extracted_data.csv | tr "[:lower:]" "[:upper:]") \
        <(cut -d, -f5-9 extracted_data.csv) \
        > staging/transformed_data.csv',
    dag = dag

)

task1 >> task2 >> task3 >> task4 >> task5 >> task6

