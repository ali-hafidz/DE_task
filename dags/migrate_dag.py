from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook
dag_params = {
    'dag_id': 'postgres__migration',
    'start_date':datetime(2020, 4, 20),
    'schedule_interval': timedelta(seconds=60)
}
with DAG(**dag_params) as dag:
    src = PostgresHook(postgres_conn_id='airflow_db_x')
    dest = PostgresHook(postgres_conn_id='airflow_db_y')
    src_conn = src.get_conn()
    cursor = src_conn.cursor()
    dest_conn = dest.get_conn()
    dest_cursor = dest_conn.cursor()
    dest_cursor.execute("SELECT * FROM sales;")
    dest.insert_rows(table="sales", rows=cursor)