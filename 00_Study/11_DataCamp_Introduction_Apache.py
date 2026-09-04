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
####################################################

# Import the task decorator
from airflow.sdk import task

@dag(dag_id='file_update')
def file_update():
  # Decorate the function as a task
  @task
  def pull_file(URL, savepath):
    r = requests.get(URL)
    with open(savepath, 'wb') as f:
      f.write(r.content)   
    print(f"File pulled from {URL} and saved to {savepath}")
  # Call the task
  pull_file('http://dataserver/sales.json', 'latestsales.json')

file_update()

####################################################

@dag(
  dag_id='analytics_dag', 
  start_date=datetime(2026,1,1)
)
def analytics_dag():
  # Specify a Bash task
  @task.bash
  def cleanup_task():
    return 'cleanup.sh'
  
  # Run the task
  cleanup_task()

analytics_dag()

####################################################

@dag(
    dag_id="analytics_dag",
    start_date=datetime(2026, 3, 1),
)
def analytics_dag():
    # Run cleanup before consolidate
    cleanup() >> consolidate()
    # Run consolidate before push_data
    consolidate() >> push_data()

analytics_dag()

####################################################

@dag(
  dag_id='update_dataflows',
  # Set to November 1, 2025
  start_date=datetime(2025, 11, 1),
  # Every Wednesday at 12:30pm
  schedule='30 12 * * 3'
)
def update_dataflows():
  @task
  def pull_source_data():
    pass
  
update_dataflows()