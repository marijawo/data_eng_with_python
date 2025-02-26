import datetime as dt
from datetime import timedelta
import pandas as pd

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


# Function to convert CSV to JSON
def convertCSVTOJson():
    df = pd.read_csv("/home/ablie/codes_wsl/dataeng_python/datasets/customer.csv")
    df.to_json("/home/ablie/codes_wsl/dataeng_python/data_pipelines/datasets/fromAirflow_customers.json", orient="records")
    print("CSV converted to JSON successfully!")


# Default arguments for the DAG
default_args = {
    'owner': 'Abdallah',
    'start_date': dt.datetime(2025, 2, 26),  # ✅ Corrected from start_time → start_date
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
        dag_id='csvToJsonDAG',
        default_args=default_args,
        schedule='@daily',  # ✅ Corrected schedule
        catchup=False,
) as dag:
    # Task 1: Print message before conversion
    print_starting = BashOperator(
        task_id='starting',
        bash_command='echo "I am reading the CSV now" '
    )

    # Task 2: Convert CSV to JSON
    CSVJson = PythonOperator(
        task_id='convert_csv_to_json',
        python_callable=convertCSVTOJson  # ✅ Corrected function call
    )

    # Define task dependencies
    print_starting >> CSVJson  # Run `CSVJson` after `print_starting`
