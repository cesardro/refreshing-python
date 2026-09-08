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

####################################################

# Create the callback function
def alert_on_failure(context):
  dag_id = context["dag"].dag_id
  task_id = context["task_instance"].task_id
  print(f"Task {task_id} in Dag {dag_id} has failed.")
  
# Specify the Dag with a failure callback
@dag(dag_id='sales_etl_dag',
     on_failure_callback=alert_on_failure
)
def sales_etl_dag():
  get_sales_data() >> process_sales_data()
  
sales_etl_dag()

####################################################

# Import the notifier
from airflow.providers.smtp.notifications.smtp import SmtpNotifier

# Add a success callback notifier
@dag(dag_id='sales_etl_dag',
     on_failure_callback=alert_on_failure,
     on_success_callback=SmtpNotifier(
         to="airflow_team@mycompany.com",
         from_email="airflow_production@mycompany.com",
         subject="sales_etl_dag run succeeded!"
     ))
def sales_etl_dag():
  get_sales_data() >> process_sales_data()
  
sales_etl_dag()

####################################################

# Add a notification when successful, including date in the subject
@dag(start_date=datetime(2026,4,30),
     on_success_callback=SmtpNotifier(
       from_email="airflow@mycompany.com",
       to="alerts@mycompany.com",
       subject="Sales update successfully processed for {{ ds }}"
     ))
def sales_update():
  pull_sales_data() >> generate_sales_report()
 
sales_update()

####################################################

# Import the proper library to read Variables
from airflow.sdk import Variable

@dag(dag_id='process_sales', start_date=datetime(2026, 4, 15))
def process_sales():
    @task()
    def parse_file():
        # Get the output file location, otherwise default to "/home"
        output_path = Variable.get("Output_Path", default="/home")      
        # Logging only currently - processing to be added later
        print(f"File parsed and saved to {output_path}/sales_report.pdf")
    
    parse_file()
process_sales()

####################################################

# Import TriggerRule
from airflow.utils.trigger_rule import TriggerRule

@dag(schedule="@daily", start_date=datetime(2026, 5, 1))
def etl_pipeline():

    # Trigger notify_on_failure when any upstream task fails
    @task(trigger_rule=TriggerRule.ONE_FAILED)
    def notify_on_failure(**context) -> None:
        dag_id = context["dag"].dag_id
        run_id = context["run_id"]
        print(f"ALERT: A task failed in DAG '{dag_id}', run '{run_id}'. Sending notification...")

    # Set notify_on_failure downstream of both transform tasks
    [transform_users(), transform_orders()] >> notify_on_failure()
    
etl_pipeline()

####################################################

@dag(schedule="@daily", start_date=datetime(2026, 5, 1))
def etl_pipeline():

  # Set retries and retry delay on extract_data
  @task(retries=3, retry_delay=timedelta(minutes=10))
  def extract_data():
    print("Extracting data from source...")
  
  @task()
  def process_source_data():
    print("Now processing data...")

  extract_data() >> process_source_data()
  
etl_pipeline()

####################################################

# Import TriggerDagRunOperator
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator

@dag(start_date=datetime(2026, 1, 1))
def parent_orchestrator_dag():
    
    # Trigger child_pipeline and wait for it to complete
    trigger_child = TriggerDagRunOperator(
        task_id="trigger_child_pipeline",
        trigger_dag_id="child_pipeline",   
        wait_for_completion=True,          
        poke_interval=30,                  
        conf={"source": "s3://my-bucket/raw/"})

    validate() >> trigger_child >> post_trigger_summary()

parent_orchestrator_dag()

####################################################

@dag(start_date=datetime(2026,5,1), schedule='@monthly')
def process_yearly_expenses():
  # Create a function to determine if years are different
  @task.branch
  def year_check(ds, prev_data_interval_start_success):
      current_year = int(ds[0:4])
      previous_year = int(prev_data_interval_start_success[0:4])
      if current_year == previous_year:
          return 'current_year_task'
      else:
          return 'new_year_task'

  # Define the dependencies
  branch_task >> current_year_task
  branch_task >> new_year_task

####################################################

from __future__ import annotations

from airflow.sdk import dag, task
from airflow.operators.empty import EmptyOperator
from pendulum import datetime


@dag(
    dag_id="BranchingTest",
    start_date=datetime(2026, 4, 15),
    schedule="@monthly",
    catchup=False,
)
def branching_test():

    @task.branch()
    def branch_task(logical_date) -> str:
        """Return the task_id of the branch to follow."""
        if int(logical_date.month) % 3 == 0:
            return "end_of_quarter_task"
        else:
            return "regular_monthly_task"

    start = EmptyOperator(task_id="start_task")

    end_of_quarter_task  = EmptyOperator(task_id="end_of_quarter_task")
    end_of_quarter_task2 = EmptyOperator(task_id="end_of_quarter_task2")
    regular_monthly_task   = EmptyOperator(task_id="regular_monthly_task")
    regular_monthly_task2  = EmptyOperator(task_id="regular_monthly_task2")

    branch = branch_task()

    start >> branch
    end_of_quarter_task >> end_of_quarter_task2
    regular_monthly_task >> regular_monthly_task2


branching_test()

####################################################

# Import ApprovalOperator
from airflow.providers.standard.operators.hitl import ApprovalOperator

@dag(start_date=datetime(2026,4,15))
def data_warehouse_dag():  
  # Create the approve_gate approval task
  approve_gate = ApprovalOperator(
        task_id="approve_sales_data",
        # Set the title for the approval request shown to the reviewer
        subject="Sales data processing - Approval Required",
        body=(
            "Please review the sales data produced by the *pull_raw_data* task."
            "Approve to push leads to the data warehouse, or Reject to halt the run."
        ),
    )
  
  pull_raw_data() >> approve_gate >> push_to_warehouse()
data_warehouse_dag()

####################################################

# Imports
from airflow.sdk import dag, task, Variable
from airflow.providers.standard.sensors.filesystem import FileSensor
from airflow.providers.smtp.notifications.smtp import SmtpNotifier

from pendulum import datetime

# Dag definition
@dag(
  start_date=datetime(2026,5,1),
  schedule='@monthly',
  on_success_callback=SmtpNotifier(
    to="airflow_team@mycompany.com",
    from_email="airflow_production@mycompany.com",
    subject="sales_etl run succeeded!"
  )
)
def sales_etl():
  
  @task
  def initialize(ds):
    print('Cleaning data directories, prepping for processing...')

    # Use a variable to set the current data path
    Variable.set("sales_etl_data_path", f'/data/sales_etl/{ds}')
  
  
  # Setup a file sensor to wait for the filescopied.txt file to be present
  filewatcher = FileSensor(
    task_id="WaitForDataFiles",
    filepath="{{var.value.sales_etl_data_path}}/filescopied.txt",
    poke_interval=15,
    timeout=300
  )
    
  initialized = initialize()
  initialized >> filewatcher
  
sales_etl()

####################################################

# Imports
from airflow.sdk import dag, task, Variable
from airflow.providers.standard.sensors.filesystem import FileSensor
from airflow.providers.smtp.notifications.smtp import SmtpNotifier

from pendulum import datetime

# Dag definition
@dag(
  start_date=datetime(2026,5,1),
  schedule='@monthly',
  on_success_callback=SmtpNotifier(
    to="airflow_team@mycompany.com",
    from_email="airflow_production@mycompany.com",
    subject="sales_etl run succeeded!"
  )
)
def sales_etl():
  
  @task
  def initialize(ds):
    print('Cleaning data directories, prepping for processing...')

    # Use a variable to set the current data path
    Variable.set("sales_etl_data_path", f'/data/sales_etl/{ds}')
  
  
  # Setup a file sensor to wait for the filescopied.txt file to be present
  filewatcher = FileSensor(
    task_id="WaitForDataFiles",
    filepath="{{var.value.sales_etl_data_path}}/filescopied.txt",
    poke_interval=15,
    timeout=300
  )
  
  
  # Create a branching task to validate the data. 
  @task.branch
  def validate_data():
    sales_path = Variable.get('sales_etl_data_path')
    print(f"Parsing data at {sales_path}")
    next_task = 'regular_monthly_task'
    if '-09-' in sales_path:
      next_task = 'yearend_approval_task'
    return next_task
  
  
  initialized = initialize()
  validated = validate_data()
  
  initialized >> filewatcher >> validated
  
  
sales_etl()

####################################################

# Imports
from airflow.sdk import dag, task, Variable
from airflow.providers.standard.sensors.filesystem import FileSensor
from airflow.providers.smtp.notifications.smtp import SmtpNotifier
from airflow.providers.standard.operators.hitl import ApprovalOperator

from pendulum import datetime

# Dag definition
@dag(
  start_date=datetime(2026,5,1),
  schedule='@monthly',
  on_success_callback=SmtpNotifier(
    to="airflow_team@mycompany.com",
    from_email="airflow_production@mycompany.com",
    subject="sales_etl run succeeded!"
  )
)
def sales_etl():
  
  @task
  def initialize(ds):
    print('Cleaning data directories, prepping for processing...')

    # Use a variable to set the current data path
    Variable.set("sales_etl_data_path", f'/data/sales_etl/{ds}')
  
  
  # Setup a file sensor to wait for the filescopied.txt file to be present
  filewatcher = FileSensor(
    task_id="WaitForDataFiles",
    filepath="{{var.value.sales_etl_data_path}}/filescopied.txt",
    poke_interval=15,
    timeout=300
  )
  
  
  # Create a branching task to validate the data. 
  @task.branch
  def validate_data():
    sales_path = Variable.get('sales_etl_data_path')
    print(f"Parsing data at {sales_path}")
    next_task = 'regular_monthly_task'
    if '-09-' in sales_path:
      next_task = 'yearend_approval_task'
    return next_task
  
  @task
  def regular_monthly_task():
    print(f'Processing data and automatically updating dataset')
    
  yearend_approval_task = ApprovalOperator(
    task_id="yearend_approval_task",
    subject="Sales data processing - Approval Required",
    body=(
            "Please review the sales data produced by the *validate_data* task "
            "on {{ds}}."
            "Approve to push to the data warehouse, or Reject to halt the run."
    ),
  )
  
  @task
  def push_to_warehouse():
    print(f'Pushing processed data to warehouse')
  
  initialized = initialize()
  validated = validate_data()
  
  initialized >> filewatcher >>validated
  
  validated >> [regular_monthly_task(), yearend_approval_task] >> push_to_warehouse()
  
  
sales_etl()