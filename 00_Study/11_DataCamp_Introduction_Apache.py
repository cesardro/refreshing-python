# Import the dag object
from airflow.sdk import dag
from pendulum import datetime

# Define the Dag attributes
@dag(
    dag_id='example_etl',
    start_date=datetime(2026, 3, 1),
)
def example_etl():
    pass

# Run the Dag
example_etl()

"""
Dags on the command line:

airflow - command line contains many subcommands
airflow -h - help and subcommand descriptions

- Dag subcommands
airflow dags list - show all recognized Dags
airflow dags reserialize - force Airflow to reload Dag files
airflow tasks test - run a specific task
"""