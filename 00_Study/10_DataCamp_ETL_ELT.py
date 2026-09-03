import pandas as pd
import logging

####################################################

def load(data_frame, file_name):
  # Write cleaned_data to a CSV using file_name
  data_frame.to_csv(file_name)
  print(f"Successfully loaded data to {file_name}")

extracted_data = extract(file_name="raw_data.csv")

# Transform extracted_data using transform() function
transformed_data = transform(data_frame=extracted_data)

# Load transformed_data to the file transformed_data.csv
load(data_frame=transformed_data, file_name="transformed_data.csv")

####################################################

# Complete building the transform() function
def transform(source_table, target_table):
  data_warehouse.execute(f"""
  CREATE TABLE {target_table} AS
      SELECT
          CONCAT("Product ID: ", product_id),
          quantity * price
      FROM {source_table};
  """)

extracted_data = extract(file_name="raw_sales_data.csv")
load(data_frame=extracted_data, table_name="raw_sales_data")

# Populate total_sales by transforming raw_sales_data
transform(source_table="raw_sales_data", target_table="total_sales")

####################################################

def extract(file_name):
  return pd.read_csv(file_name)

def transform(data_frame):
  return data_frame.loc[:, ["industry_name", "number_of_firms"]]

def load(data_frame, file_name):
  data_frame.to_csv(file_name)
  
extracted_data = extract(file_name="raw_industry_data.csv")
transformed_data = transform(data_frame=extracted_data)

# Pass the transformed_data DataFrame to the load() function
load(data_frame=transformed_data, file_name="number_of_firms.csv")

####################################################

sales_data = pd.read_parquet("sales_data.parquet", engine="fastparquet")

print(sales_data.dtypes)
print(sales_data.shape)
print(sales_data.head())

"""
Order ID              int64
Product              object
Quantity Ordered      int64
Price Each          float64
Order Date           object
Purchase Address     object
dtype: object
(282, 6)
   Order ID                 Product  Quantity Ordered  Price Each      Order Date                           Purchase Address
0    259358  34in Ultrawide Monitor                 1      379.99  10/28/19 10:56            609 Cherry St, Dallas, TX 75001
1    259359  27in 4K Gaming Monitor                 1      389.99  10/28/19 17:26          225 5th St, Los Angeles, CA 90001
2    259360  AAA Batteries (4-pack)                 2        2.99  10/24/19 17:20       967 12th St, New York City, NY 10001
3    259361        27in FHD Monitor                 1      149.99  10/14/19 22:26  628 Jefferson St, New York City, NY 10001
4    259362        Wired Headphones                 1       11.99   10/7/19 16:10         534 14th St, Los Angeles, CA 90001
"""

####################################################

import sqlalchemy

# Create a connection to the sales database
db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/sales")

# Query the sales table
raw_sales_data = pd.read_sql("select * from sales", db_engine)
print(raw_sales_data)

####################################################

def extract():
    connection_uri = "postgresql+psycopg2://repl:password@localhost:5432/sales"
    db_engine = sqlalchemy.create_engine(connection_uri)
    raw_data = pd.read_sql("SELECT * FROM sales WHERE quantity_ordered = 1", db_engine)
    
    # Print the head of the DataFrame
    print(raw_data.head())
    
    # Return the extracted DataFrame
    return raw_data
    
# Call the extract() function
raw_sales_data = extract()

####################################################

# Extract data from the sales_data.parquet path
raw_sales_data = extract("sales_data.parquet")

def transform(raw_data):
  	# Only keep rows with `Quantity Ordered` greater than 1
    clean_data = raw_data.loc[raw_data['Quantity Ordered'] > 1, :]
    
    # Only keep columns "Order Date", "Quantity Ordered", and "Purchase Address"
    clean_data = raw_data.loc[raw_data['Quantity Ordered'] > 1, ['Order Date', 'Quantity Ordered', 'Purchase Address']]
    
    # Return the filtered DataFrame
    return clean_data
    
transform(raw_sales_data)

####################################################

raw_sales_data = extract("sales_data.csv")

def transform(raw_data):
    # Convert the "Order Date" column to type datetime
    raw_data["Order Date"] = pd.to_datetime(raw_data['Order Date'], format="%m/%d/%y %H:%M")
    
    # Only keep items under ten dollars
    clean_data = raw_data.loc[raw_data['Price Each'] < 10, :]
    return clean_data

clean_sales_data = transform(raw_sales_data)

# Check the data types of each column
print(clean_sales_data.dtypes)

"""
    Order ID                     int64
    Product                     object
    Quantity Ordered             int64
    Price Each                 float64
    Order Date          datetime64[ns]
    Purchase Address            object
    dtype: object
"""

####################################################

def extract(file_path):
    raw_data = pd.read_parquet(file_path)
    return raw_data

raw_sales_data = extract("sales_data.parquet")

def transform(raw_data):
  	# Filter rows and columns
    clean_data = raw_data.loc[raw_data["Quantity Ordered"] == 1, ["Order ID","Price Each","Quantity Ordered"]]
    return clean_data

# Transform the raw_sales_data
clean_sales_data = transform(raw_sales_data)

####################################################

def transform(raw_data):
	# Find the items prices less than 25 dollars
	return raw_data.loc[raw_data["Price Each"] < 25, ["Order ID", "Product", "Price Each", "Order Date"]]

def load(clean_data):
	# Write the data to a CSV file without the index column
	clean_data.to_csv("transformed_sales_data.csv", index=False)


clean_sales_data = transform(raw_sales_data)

# Call the load function on the cleaned DataFrame
load(clean_sales_data)

####################################################

# Import the os library
import os

# Load the data to a csv file with the index, no header and pipe separated
def load(clean_data, path_to_write):
	clean_data.to_csv(path_to_write, header=False, sep="|")

load(clean_sales_data, "clean_sales_data.csv")

# Check that the file is present.
file_exists = os.path.exists("clean_sales_data.csv")
print(file_exists)

####################################################

def load(clean_data, file_path):
    # Write the data to a file
    clean_data.to_csv(file_path, header=False, index=False)

    # Check to make sure the file exists
    file_exists = os.path.exists(file_path)
    if not file_exists:
        raise Exception(f"File does NOT exists at path {file_path}")

# Load the transformed data to the provided file path
load(clean_sales_data, "transformed_sales_data.csv")

####################################################

def transform(raw_data):
    raw_data["Order Date"] = pd.to_datetime(raw_data["Order Date"], format="%m/%d/%y %H:%M")
    clean_data = raw_data.loc[raw_data["Price Each"] < 10, :]
    
    # Create an info log regarding transformation
    logging.info("Transformed 'Order Date' column to type 'datetime'.")
    
    # Create debug-level logs for the DataFrame before and after filtering
    logging.debug(f"Shape of the DataFrame before filtering: {raw_data.shape}")
    logging.debug(f"Shape of the DataFrame after filtering: {clean_data.shape}")
    
    return clean_data
  
clean_sales_data = transform(raw_sales_data)

####################################################

def extract(file_path):
    return pd.read_parquet(file_path)

# Update the pipeline to include a try block
try:
	# Attempt to read in the file
    raw_sales_data = extract("sales_data.parquet")
	
# Catch the FileNotFoundError
except FileNotFoundError as file_not_found:
	# Write an error-level log
	logging.error(file_not_found)

####################################################

def transform(raw_data):
	return raw_data.loc[raw_data["Total Price"] > 1000, :]

try:
	clean_sales_data = transform(raw_sales_data)
	logging.info("Successfully filtered DataFrame by 'Total Price'")

except KeyError as ke:
	logging.warning(f"{ke}: Cannot filter DataFrame by 'Total Price'")
	
	# Create the "Total Price" column, transform the updated DataFrame
	raw_sales_data["Total Price"] = raw_sales_data["Price Each"] * raw_sales_data["Quantity Ordered"]
	clean_sales_data = transform(raw_sales_data)

####################################################

"""
Records has this visual representation:
[
    {row 1},
    {row 2},
    {row 3}
] 

->

[
    {
        "name": "Carlos",
        "age": 26
    },
    {
        "name": "Ana",
        "age": 30
    }
]

Columns has this visual representation:
{
    "column": {
        "key": value
    }
}

->

{
    "name": {
        "0": "Carlos",
        "1": "Ana"
    },
    "age": {
        "0": 26,
        "1": 30
    }
}

Index has this visual representation:
{
    "index": {
        column data
    }
}

->

{
    "0": {
        "name": "Carlos",
        "age": 26
    },
    "1": {
        "name": "Ana",
        "age": 30
    }
}

Split has this visual representation:
columns → column name
index   → key
data    → value

->

{
    "columns": ["name", "age"],
    "index": [0, 1],
    "data": [
        ["Carlos", 26],
        ["Ana", 30]
    ]
}

Values has this visual representation:
[
    ["Carlos", 26],
    ["Ana", 30]
]
"""

import pandas as pd
import json
import sqlalchemy
import logging

# -- Incoming branch (renamed helpers to avoid collisions) ---------------------------------

def extract_json_records(file_path):
    # Read the JSON file into a DataFrame (records oriented)
    return pd.read_json(file_path, orient="records")

# Call the extract_json_records function with the appropriate path
raw_testing_scores = extract_json_records("testing_scores.json")

# Output the head of the DataFrame
print(raw_testing_scores.head())

####################################################

# Import the json library already done above

def extract_json_lib(file_path):
    with open(file_path, "r") as json_file:
        # Load the data from the JSON file
        raw_data = json.load(json_file)
    return raw_data

raw_testing_scores = extract_json_lib("nested_scores.json")

# Print the raw_testing_scores
print(raw_testing_scores)

####################################################

raw_testing_scores_keys = []

# Iterate through the keys of the raw_testing_scores dictionary
for school_id in raw_testing_scores.keys():
    # Append each key to the raw_testing_scores_keys list
    raw_testing_scores_keys.append(school_id)

print(raw_testing_scores_keys[0:3])

# ['02M260', '06M211', '01M539']

####################################################

raw_testing_scores_values = []

# Iterate through the values of the raw_testing_scores dictionary
for school_info in raw_testing_scores.values():
    raw_testing_scores_values.append(school_info)

print(raw_testing_scores_values[0:3])

# [{'street_address': '425 West 33rd Street', 'city': 'Manhattan', 'scores': {'math': None, 'reading': None, 'writing': None}}, {'street_address': '650 Academy Street', 'city': 'Manhattan', 'scores': {'math': None, 'reading': None, 'writing': None}}, {'street_address': '111 Columbia Street', 'city': 'Manhattan', 'scores': {'math': 657.0, 'reading': 601.0, 'writing': 601.0}}]

####################################################

raw_testing_scores_keys = []
raw_testing_scores_values = []

# Iterate through the values of the raw_testing_scores dictionary
for school_id, school_info in raw_testing_scores.items():
    raw_testing_scores_keys.append(school_id)
    raw_testing_scores_values.append(school_info)

print(raw_testing_scores_keys[0:3])
print(raw_testing_scores_values[0:3])

"""
['02M260', '06M211', '01M539']
[{'street_address': '425 West 33rd Street', 'city': 'Manhattan', 'scores': {'math': None, 'reading': None, 'writing': None}}, {'street_address': '650 Academy Street', 'city': 'Manhattan', 'scores': {'math': None, 'reading': None, 'writing': None}}, {'street_address': '111 Columbia Street', 'city': 'Manhattan', 'scores': {'math': 657.0, 'reading': 601.0, 'writing': 601.0}}]
"""

####################################################

# Parse the street_address from the dictionary
street_address = school.get("street_address")

# Parse the scores dictionary
scores = school.get("scores")

# Try to parse the math, reading and writing values from scores
math_score = scores.get("math", 0)
reading_score = scores.get("reading", 0)
writing_score = scores.get("writing", 0)

print(f"Street Address: {street_address}")
print(f"Math: {math_score}, Reading: {reading_score}, Writing: {writing_score}")

"""
Street Address: 111 Columbia Street
Math: 657, Reading: 601, Writing: 0
"""

####################################################

normalized_testing_scores = []

# Loop through each of the dictionary key-value pairs
for school_id, school_info in raw_testing_scores.items():
    normalized_testing_scores.append([
        school_id,
        school_info.get("street_address"),  # Pull the "street_address"
        school_info.get("city"),
        school_info.get("scores").get("math", 0),
        school_info.get("scores").get("reading", 0),
        school_info.get("scores").get("writing", 0),
    ])

print(normalized_testing_scores)

####################################################

# Create a DataFrame from the normalized_testing_scores list
normalized_data = pd.DataFrame(normalized_testing_scores)

# Set the column names
normalized_data.columns = ["school_id", "street_address", "city", "avg_score_math", "avg_score_reading", "avg_score_writing"]

normalized_data = normalized_data.set_index("school_id")
print(normalized_data.head())

"""
    school_id        street_address       city  avg_score_math  avg_score_reading  avg_score_writing
                                                                                          
    02M260     425 West 33rd Street  Manhattan             NaN                NaN                NaN
    06M211       650 Academy Street  Manhattan             NaN                NaN                NaN
    01M539      111 Columbia Street  Manhattan           657.0              601.0              601.0
    02M294         350 Grand Street  Manhattan           395.0              411.0              387.0
    02M308         350 Grand Street  Manhattan           418.0              428.0              415.0
"""

####################################################

# Transform helpers (renamed to keep them distinct)
def transform_fillna_scores(raw_data):
    raw_data.fillna(
        value={
            # Fill NaN values with column mean
            "math_score": raw_data["math_score"].mean(),
            "reading_score": raw_data["reading_score"].mean(),
            "writing_score": raw_data["writing_score"].mean()
        }, inplace=True
    )
    return raw_data

clean_testing_scores = transform_fillna_scores(raw_testing_scores)

# Print the head of the clean_testing_scores DataFrame
print(clean_testing_scores.head())

"""
                  street_address       city  math_score  reading_score  writing_score
    02M260  425 West 33rd Street  Manhattan     432.944        424.504        418.459
    06M211    650 Academy Street  Manhattan     432.944        424.504        418.459
    01M539   111 Columbia Street  Manhattan     657.000        601.000        601.000
    02M294      350 Grand Street  Manhattan     395.000        411.000        387.000
    02M308      350 Grand Street  Manhattan     418.000        428.000        415.000
"""

####################################################

def transform_group_by_city(raw_data):
    # Use .loc[] to only return the needed columns
    raw_data = raw_data.loc[:, ["city","math_score","reading_score","writing_score"]]

    # Group the data by city, return the grouped DataFrame
    grouped_data = raw_data.groupby(by=["city"], axis=0).mean()
    return grouped_data

# Transform the data, print the head of the DataFrame
grouped_testing_scores = transform_group_by_city(raw_testing_scores)
print(grouped_testing_scores.head())

"""
    city       math_score  reading_score  writing_score                                             
    Astoria       509.600        494.800        497.200
    Bayside       523.000        479.000        485.000
    Bellerose     453.000        434.000        439.000
    Bronx         404.357        402.520        395.847
    Brooklyn      416.404        410.761        403.092
"""

####################################################

def transform_extract_street_name(raw_data, find_street_name):
    # Use the apply function to extract the street_name from the street_address
    raw_data["street_name"] = raw_data.apply(
        # Pass the correct function to the apply method
        find_street_name,
        axis=1
    )
    return raw_data

# Transform the raw_testing_scores DataFrame (requires a find_street_name function to be available)
# cleaned_testing_scores = transform_extract_street_name(raw_testing_scores, find_street_name)
# print(cleaned_testing_scores.head())

####################################################

# Update the connection string, create the connection object to the schools database
# NOTE: credentials here are placeholders; keep environment secrets out of source
# db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/schools")

# Example write (commented to avoid accidental DB writes in unrelated environments)
# cleaned_testing_scores.to_sql(name="scores", con=db_engine, index=False, if_exists="replace")

####################################################

def load_scores_by_city(clean_data, con_engine):
    clean_data.to_sql(name="scores_by_city", con=con_engine, if_exists="replace", index=True, index_label="school_id")

# Example usage (commented because db_engine may not be defined in all environments)
# load_scores_by_city(cleaned_testing_scores, db_engine)

####################################################

# -- End incoming branch content -------------------------------------------------------


####################################################

raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)
load(clean_tax_data, "clean_tax_data.parquet")

print(f"Shape of raw_tax_data: {raw_tax_data.shape}")
print(f"Shape of clean_tax_data: {clean_tax_data.shape}")

to_validate = pd.read_parquet("clean_tax_data.parquet")
print(clean_tax_data.head(3))
print(to_validate.head(3))

# Check that the DataFrames are equal
print(to_validate.equals(clean_tax_data))


####################################################

# Trigger the data pipeline to run three times
for attempt in range(0, 3):
	print(f"Attempt: {attempt}")
	raw_tax_data = extract("raw_tax_data.csv")
	clean_tax_data = transform(raw_tax_data)
	load(clean_tax_data, "clean_tax_data.parquet")
	
	# Print the shape of the cleaned_tax_data DataFrame
	print(f"Shape of clean_tax_data: {clean_tax_data.shape}")
    
# Read in the loaded data, check the shape
to_validate = pd.read_parquet("clean_tax_data.parquet")
print(f"Final shape of cleaned data: {to_validate.shape}")

####################################################

raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)

# Validate the number of columns in the DataFrame
assert len(clean_tax_data.columns) == 5

####################################################

raw_tax_data = extract("raw_tax_data.csv")
clean_tax_data = transform(raw_tax_data)

# Determine if the clean_tax_data DataFrames take type pd.DataFrame
isinstance(clean_tax_data, pd.DataFrame)

####################################################

# Import pytest
import pytest

# Create a pytest fixture
@pytest.fixture()
def raw_tax_data():
	raw_data = extract("raw_tax_data.csv")
    
    # Return the raw DataFrame
	return raw_data

####################################################

@pytest.fixture()
def clean_tax_data():
    raw_data = pd.read_csv("raw_tax_data.csv")
    clean_data = transform(raw_data)
    return clean_data

# Pass the fixture to the function
def test_tax_rate(clean_tax_data):
    # Assert values are within the expected range
    assert clean_tax_data["tax_rate"].max() <= 1 and clean_tax_data["tax_rate"].min() >= 0

####################################################

import logging
from pipeline_utils import extract, transform, load

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

try:
	raw_tax_data = extract("raw_tax_data.csv")
	clean_tax_data = transform(raw_tax_data)
	load(clean_tax_data, "clean_tax_data.parquet")
    
	logging.info("Successfully extracted, transformed and loaded data.")  # Log a success message.
    
except Exception as e:
	logging.error(f"Pipeline failed with error: {e}")  # Log failure message

