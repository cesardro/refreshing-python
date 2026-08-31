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

def extract(file_path):
  # Read the JSON file into a DataFrame
  return pd.read_json(file_path, orient="records")

# Call the extract function with the appropriate path, assign to raw_testing_scores
raw_testing_scores = extract("testing_scores.json")

# Output the head of the DataFrame
print(raw_testing_scores.head())

####################################################

# Import the json library
import json

def extract(file_path):
    with open(file_path, "r") as json_file:
        # Load the data from the JSON file
        raw_data = json.load(json_file)
    return raw_data

raw_testing_scores = extract("nested_scores.json")

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

# [['02M260', '425 West 33rd Street', 'Manhattan', None, None, None], ['06M211', '650 Academy Street', 'Manhattan', None, None, None], ['01M539', '111 Columbia Street', 'Manhattan', 657.0, 601.0, 601.0], ['02M294', '350 Grand Street', 'Manhattan', 395.0, 411.0, 387.0], ['02M308', '350 Grand Street', 'Manhattan', 418.0, 428.0, 415.0], ['02M545', '350 Grand Street', 'Manhattan', 613.0, 453.0, 463.0], ['01M292', '220 Henry Street', 'Manhattan', 410.0, 406.0, 381.0], ['01M696', '525 East Houston Street', 'Manhattan', 634.0, 641.0, 639.0], ['02M305', '350 Grand Street', 'Manhattan', 389.0, 395.0, 381.0], ['01M509', '145 Stanton Street', 'Manhattan', 438.0, 413.0, 394.0], ['01M448', '200 Monroe Street', 'Manhattan', 437.0, 355.0, 352.0], ['02M543', '350 Grand Street', 'Manhattan', 381.0, 396.0, 372.0], ['02M298', '100 Hester Street', 'Manhattan', 430.0, 435.0, 427.0], ['02M420', '345 East 15th Street', 'Manhattan', 452.0, 445.0, 430.0], ['02M399', '40 Irving Place', 'Manhattan', 446.0, 433.0, 411.0], ['02M546', '40 Irving Place', 'Manhattan', None, None, None], ['02M533', '40 Irving Place', 'Manhattan', None, None, None], ['02M438', '40 Irving Place', 'Manhattan', 403.0, 330.0, 316.0], ['02M407', '345 East 15th Street', 'Manhattan', 501.0, 550.0, 541.0], ['02M374', '40 Irving Place', 'Manhattan', 446.0, 459.0, 455.0], ['02M551', '550 Wheeler Avenue', 'Manhattan', 446.0, 453.0, 428.0], ['02M580', '26 Broadway', 'Manhattan', 411.0, 415.0, 409.0], ['02M418', '75 Broad Street', 'Manhattan', 577.0, 560.0, 567.0], ['02M316', '26 Broadway', 'Manhattan', 418.0, 420.0, 417.0], ['02M489', '100 Trinity Place', 'Manhattan', 469.0, 442.0, 447.0], ['02M425', '90 Trinity Place', 'Manhattan', 390.0, 396.0, 392.0], ['01M450', '420 East 12th Street', 'Manhattan', 454.0, 428.0, 445.0], ['02M411', '55 East 25th Street', 'Manhattan', 592.0, 526.0, 531.0], ['02M047', '223 East 23rd Street', 'Manhattan', None, None, None], ['02M413', '127 East 22nd Street', 'Manhattan', 534.0, 533.0, 522.0], ['02M439', '43 West 22nd Street', 'Manhattan', 522.0, 479.0, 510.0], ['02M422', '351 West 18th Street', 'Manhattan', None, None, None], ['02M412', '333 West 17th Street', 'Manhattan', 595.0, 550.0, 555.0], ['02M534', '34 West 14th Street', 'Manhattan', None, None, None], ['02M437', '351 West 18th Street', 'Manhattan', 378.0, 407.0, 388.0], ['02M392', '351 West 18th Street', 'Manhattan', 410.0, 407.0, 399.0], ['02M605', '351 West 18th Street', 'Manhattan', None, None, None], ['02M419', '351 West 18th Street', 'Manhattan', 386.0, 386.0, 386.0], ['02M600', '225 West 24th Street', 'Manhattan', 433.0, 442.0, 427.0], ['02M414', '333 West 17th Street', 'Manhattan', 560.0, 530.0, 522.0], ['02M615', '131 Avenue of the Americas', 'Manhattan', 439.0, 418.0, 400.0], ['02M376', '131 Avenue of the Americas', 'Manhattan', 518.0, 515.0, 503.0], ['02M432', '111 East 33rd Street', 'Manhattan', None, None, None], ['02M427', '111 East 33rd Street', 'Manhattan', 350.0, 334.0, 321.0], ['02M500', '111 East 33rd Street', 'Manhattan', 375.0, 385.0, 387.0], ['02M393', '439 West 49th Street', 'Manhattan', 395.0, 386.0, 371.0], ['02M303', '525 West 50th Street', 'Manhattan', 366.0, 356.0, 371.0], ['02M296', '525 West 50th Street', 'Manhattan', 451.0, 433.0, 424.0], ['02M300', '525 West 50th Street', 'Manhattan', 445.0, 417.0, 403.0], ['02M135', '439 West 49th Street', 'Manhattan', None, None, None], ['02M400', '444 West 56th Street', 'Manhattan', 469.0, 454.0, 444.0], ['02M630', '231-249 East 56th Street', 'Manhattan', 455.0, 475.0, 458.0], ['02M542', '525 West 50th Street', 'Manhattan', 409.0, 360.0, 347.0], ['02M507', '439 West 49th Street', 'Manhattan', 445.0, 432.0, 415.0], ['02M288', '525 West 50th Street', 'Manhattan', 428.0, 435.0, 421.0], ['02M416', '411 East 76th Street', 'Manhattan', 641.0, 617.0, 631.0], ['03M299', '122 Amsterdam Avenue', 'Manhattan', 375.0, 389.0, 380.0], ['03M307', '122 Amsterdam Avenue', 'Manhattan', 392.0, 419.0, 396.0], ['03M479', '227-243 West 61st Street', 'Manhattan', 583.0, 586.0, 595.0], ['03M485', '100 Amsterdam Avenue', 'Manhattan', 592.0, 592.0, 597.0], ['03M494', '122 Amsterdam Avenue', 'Manhattan', 421.0, 428.0, 406.0], ['03M541', '122 Amsterdam Avenue', 'Manhattan', 581.0, 531.0, 535.0], ['03M859', '122 Amsterdam Avenue', 'Manhattan', None, None, None], ['03M492', '122 Amsterdam Avenue', 'Manhattan', 415.0, 417.0, 402.0], ['03M402', '145 West 84th Street', 'Manhattan', 393.0, 371.0, 378.0], ['03M417', '145 West 84th Street', 'Manhattan', 489.0, 491.0, 500.0], ['03M403', '145 West 84th Street', 'Manhattan', 406.0, 407.0, 413.0], ['03M415', '215 West 114th Street', 'Manhattan', 381.0, 401.0, 392.0], ['03M860', '215 West 114th Street', 'Manhattan', 390.0, 384.0, 373.0], ['05M362', '425 West 123rd Street', 'Manhattan', 583.0, 561.0, 546.0], ['05M367', '509 West 129th Street', 'Manhattan', 357.0, 349.0, 365.0], ['05M369', '509 West 129th Street', 'Manhattan', 379.0, 399.0, 388.0], ['04M680', '1680 Lexington Avenue', 'Manhattan', 385.0, 380.0, 370.0], ['04M555', '1573 Madison Avenue', 'Manhattan', 483.0, 468.0, 439.0], ['04M495', '230 East 105th Street', 'Manhattan', 429.0, 433.0, 435.0], ['04M610', '105 East 106th Street', 'Manhattan', 478.0, 465.0, 472.0], ['04M435', '260 Pleasant Avenue', 'Manhattan', 556.0, 505.0, 495.0], ['04M372', '240 East 109th Street', 'Manhattan', None, None, None], ['05M304', '6 Edgecombe Avenue', 'Manhattan', 416.0, 445.0, 440.0], ['05M670', '200-214 West 135th Street', 'Manhattan', 402.0, 394.0, 400.0], ['05M692', '240 Convent Avenue', 'Manhattan', 683.0, 610.0, 596.0], ['06M540', '443 West 135th Street', 'Manhattan', 459.0, 453.0, 447.0], ['06M552', '501 West 165th Street', 'Manhattan', 383.0, 355.0, 352.0], ['06M346', '504 West 158th Street', 'Manhattan', 387.0, 389.0, 385.0], ['06M348', '511 West 182nd Street', 'Manhattan', 443.0, 423.0, 434.0], ['06M423', '650 Academy Street', 'Manhattan', None, None, None], ['05M157', '2005 Madison Avenue', 'Manhattan', None, None, None], ['04M409', '2351 1st Avenue', 'Manhattan', 344.0, 368.0, 367.0], ['02M531', '123 West 43rd Street', 'Manhattan', 425.0, 451.0, 458.0], ['02M408', '328 West 48th Street', 'Manhattan', 496.0, 520.0, 516.0], ['02M529', '120 West 46th Street', 'Manhattan', 418.0, 422.0, 415.0], ['02M280', '411 Pearl Street', 'Manhattan', None, None, None], ['02M520', '411 Pearl Street', 'Manhattan', 418.0, 415.0, 398.0], ['02M282', '411 Pearl Street', 'Manhattan', None, None, None], ['02M139', '411 Pearl Street', 'Manhattan', None, None, None], ['05M499', '2581 7th Avenue', 'Manhattan', 463.0, 452.0, 450.0], ['06M463', '549 Audubon Avenue', 'Manhattan', 378.0, 381.0, 383.0], ['06M462', '549 Audubon Avenue', 'Manhattan', 367.0, 377.0, 363.0], ['06M467', '549 Audubon Avenue', 'Manhattan', 401.0, 394.0, 381.0], ['06M293', '4600 Broadway', 'Manhattan', 495.0, 445.0, 450.0], ['06M468', '549 Audubon Avenue', 'Manhattan', 374.0, 385.0, 389.0], ['02M459', '317 East 67th Street', 'Manhattan', 438.0, 358.0, 382.0], ['02M519', '317 East 67th Street', 'Manhattan', 485.0, 498.0, 496.0], ['02M449', '317 East 67th Street', 'Manhattan', 431.0, 409.0, 396.0], ['02M655', '320 East 96th Street', 'Manhattan', 435.0, 440.0, 425.0], ['02M475', '345 Chambers Street', 'Manhattan', 754.0, 697.0, 693.0], ['31R600', '290 St Marks Place', 'Staten Island', 420.0, 429.0, 409.0], ['31R080', '715 Ocean Terrace', 'Staten Island', 483.0, 473.0, 470.0], ['31R450', '105 Hamilton Avenue', 'Staten Island', 453.0, 458.0, 444.0], ['31R445', '85 St Josephs Avenue', 'Staten Island', 432.0, 427.0, 425.0], ['31R605', '485 Clawson Street', 'Staten Island', 711.0, 660.0, 670.0], ['31R440', '465 New Dorp Lane', 'Staten Island', 454.0, 446.0, 444.0], ['31R455', '100 Luten Avenue', 'Staten Island', 494.0, 476.0, 476.0], ['31R460', '1200 Manor Road', 'Staten Island', 496.0, 490.0, 487.0], ['31R064', '100 Essex Drive', 'Staten Island', 442.0, 458.0, 454.0], ['31R047', '100 Essex Drive', 'Staten Island', 477.0, 468.0, 464.0], ['07X522', '333 East 151st Street', 'Bronx', None, None, None], ['07X547', '730 Concourse Village West', 'Bronx', 390.0, 398.0, 376.0], ['09X505', '244 East 163rd Street', 'Bronx', 403.0, 409.0, 415.0], ['07X548', '730 Concourse Village West', 'Bronx', 402.0, 405.0, 395.0], ['07X527', '730 Concourse Village West', 'Bronx', 384.0, 355.0, 361.0], ['07X551', '339 Morris Avenue', 'Bronx', 398.0, 400.0, 405.0], ['07X670', '350 Gerard Avenue', 'Bronx', 374.0, 386.0, 382.0], ['07X427', '350 Gerard Avenue', 'Bronx', 380.0, 382.0, 362.0], ['07X600', '333 East 151st Street', 'Bronx', 390.0, 373.0, 371.0], ['09X327', '1501 Jerome Avenue', 'Bronx', None, None, None], ['09X365', '1700 Macombs Road', 'Bronx', 371.0, 334.0, 348.0], ['07X223', '360 East 145th Street', 'Bronx', None, None, None], ['07X221', '360 East 145th Street', 'Bronx', 419.0, 414.0, 394.0], ['07X334', '345 Brook Avenue', 'Bronx', 345.0, 338.0, 312.0], ['07X520', '470 Jackson Avenue', 'Bronx', None, None, None], ['07X500', '600 St Anns Avenue', 'Bronx', 463.0, 451.0, 435.0], ['07X259', '455 Southern Boulevard', 'Bronx', None, None, None], ['07X495', '701 St Anns Avenue', 'Bronx', 420.0, 446.0, 424.0], ['07X473', '701 St Anns Avenue', 'Bronx', 377.0, 373.0, 369.0], ['09X543', '1110 Boston Road', 'Bronx', 363.0, 401.0, 396.0], ['09X403', '1110 Boston Road', 'Bronx', 355.0, 330.0, 320.0], ['08X559', '900 Tinton Avenue', 'Bronx', None, None, None], ['12X479', '800 Home Street', 'Bronx', 370.0, 379.0, 381.0], ['09X260', '1363 Fulton Avenue', 'Bronx', 513.0, 468.0, 485.0], ['09X324', '250 East 164th Street', 'Bronx', 424.0, 413.0, 409.0], ['09X250', '1363 Fulton Avenue', 'Bronx', 400.0, 391.0, 397.0], ['12X267', '800 Home Street', 'Bronx', 394.0, 381.0, 363.0], ['09X404', '1110 Boston Road', 'Bronx', 377.0, 385.0, 383.0], ['09X297', '1110 Boston Road', 'Bronx', 407.0, 389.0, 386.0], ['09X517', '3630 Third Avenue', 'Bronx', 387.0, 386.0, 386.0], ['09X564', '240 East 172nd Street', 'Bronx', None, None, None], ['09X241', '1595 Bathgate Avenue', 'Bronx', 445.0, 418.0, 422.0], ['09X227', '240 East 172nd Street', 'Bronx', 395.0, 401.0, 382.0], ['09X252', '1595 Bathgate Avenue', 'Bronx', 417.0, 399.0, 398.0], ['09X276', '1701 Fulton Avenue', 'Bronx', None, None, None], ['09X350', '240 East 172nd Street', 'Bronx', None, None, None], ['09X525', '1710 Webster Avenue', 'Bronx', 375.0, 372.0, 374.0], ['09X263', '1595 Bathgate Avenue', 'Bronx', 382.0, 375.0, 384.0], ['09X413', '240 East 172nd Street', 'Bronx', 431.0, 421.0, 426.0], ['09X231', '4143 Third Avenue', 'Bronx', 398.0, 410.0, 397.0], ['09X412', '240 East 172nd Street', 'Bronx', 365.0, 360.0, 346.0], ['09X329', '240 East 172nd Street', 'Bronx', 385.0, 385.0, 388.0], ['10X225', '2225 Webster Avenue', 'Bronx', 402.0, 421.0, 410.0], ['10X243', '500 East Fordham Road', 'Bronx', 404.0, 383.0, 378.0], ['10X524', '2474 Crotona Avenue', 'Bronx', None, None, None], ['10X439', '500 East Fordham Road', 'Bronx', 401.0, 402.0, 386.0], ['10X264', '2474 Crotona Avenue', 'Bronx', None, None, None], ['10X434', '500 East Fordham Road', 'Bronx', 413.0, 408.0, 402.0], ['10X437', '500 East Fordham Road', 'Bronx', 398.0, 404.0, 412.0], ['10X565', '2474 Crotona Avenue', 'Bronx', None, None, None], ['10X374', '500 East Fordham Road', 'Bronx', 408.0, 417.0, 404.0], ['10X438', '500 East Fordham Road', 'Bronx', 355.0, 373.0, 368.0], ['12X248', '1180 Rev JA Polite Avenue', 'Bronx', 387.0, 388.0, 386.0], ['08X332', '965 Longwood Avenue', 'Bronx', 376.0, 372.0, 369.0], ['08X530', '965 Longwood Avenue', 'Bronx', 378.0, 391.0, 378.0], ['08X269', '928 Simpson Street', 'Bronx', 417.0, 412.0, 403.0], ['12X278', '1180 Rev JA Polite Avenue', 'Bronx', 366.0, 362.0, 365.0], ['12X271', '1716 Southern Boulevard', 'Bronx', 418.0, 406.0, 408.0], ['12X511', '1619 Boston Road', 'Bronx', 364.0, 385.0, 366.0], ['12X682', '1021 Jennings Street', 'Bronx', 345.0, 347.0, 339.0], ['12X251', '1619 Boston Road', 'Bronx', 377.0, 372.0, 365.0], ['12X372', '2024 Mohegan Avenue', 'Bronx', 393.0, 397.0, 379.0], ['12X684', '1122 East 180th Street', 'Bronx', 379.0, 372.0, 373.0], ['08X348', '3000 East Tremont Avenue', 'Bronx', None, None, None], ['08X293', '3000 East Tremont Avenue', 'Bronx', 390.0, 411.0, 393.0], ['08X558', '3000 East Tremont Avenue', 'Bronx', None, None, None], ['08X320', '3000 East Tremont Avenue', 'Bronx', None, None, None], ['08X405', '3000 East Tremont Avenue', 'Bronx', 426.0, 419.0, 407.0], ['08X349', '3000 East Tremont Avenue', 'Bronx', None, None, None], ['11X418', '2040 Antin Place', 'Bronx', 408.0, 428.0, 404.0], ['10X368', '2975 Tibbett Avenue', 'Bronx', 426.0, 419.0, 404.0], ['10X284', '99 Terrace View Avenue', 'Bronx', 384.0, 394.0, 366.0], ['10X213', '99 Terrace View Avenue', 'Bronx', 394.0, 406.0, 391.0], ['10X546', '99 Terrace View Avenue', 'Bronx', 382.0, 384.0, 390.0], ['10X477', '99 Terrace View Avenue', 'Bronx', 451.0, 417.0, 423.0], ['10X237', '120 West 231st Street', 'Bronx', 423.0, 420.0, 425.0], ['10X141', '660 West 237th Street', 'Bronx', 496.0, 485.0, 476.0], ['11X513', '921 East 228th Street', 'Bronx', 407.0, 363.0, 358.0], ['11X514', '921 East 228th Street', 'Bronx', 392.0, 408.0, 392.0], ['11X270', '921 East 228th Street', 'Bronx', 392.0, 408.0, 400.0], ['11X544', '800 East Gun Hill Road', 'Bronx', 367.0, 381.0, 361.0], ['11X545', '800 East Gun Hill Road', 'Bronx', 403.0, 410.0, 393.0], ['11X290', '800 East Gun Hill Road', 'Bronx', 386.0, 380.0, 391.0], ['11X275', '800 East Gun Hill Road', 'Bronx', 396.0, 399.0, 377.0], ['11X265', '800 East Gun Hill Road', 'Bronx', 407.0, 416.0, 401.0], ['11X253', '800 East Gun Hill Road', 'Bronx', 380.0, 437.0, 425.0], ['10X433', '2780 Reservoir Avenue', 'Bronx', 372.0, 361.0, 369.0], ['10X445', '75 West 205th Street', 'Bronx', 714.0, 660.0, 667.0], ['10X268', '2780 Reservoir Avenue', 'Bronx', 366.0, 311.0, 310.0], ['10X549', '2780 Reservoir Avenue', 'Bronx', 432.0, 396.0, 395.0], ['10X353', '100 West Mosholu Parkway South', 'Bronx', None, None, None], ['10X442', '2780 Reservoir Avenue', 'Bronx', 417.0, 434.0, 425.0], ['10X696', '2925 Goulden Avenue', 'Bronx', 669.0, 672.0, 672.0], ['10X440', '100 West Mosholu Parkway South', 'Bronx', 445.0, 436.0, 433.0], ['10X342', '2780 Reservoir Avenue', 'Bronx', 390.0, 387.0, 379.0], ['10X351', '100 West Mosholu Parkway South', 'Bronx', None, None, None], ['11X299', '925 Astor Avenue', 'Bronx', 422.0, 417.0, 409.0], ['11X542', '925 Astor Avenue', 'Bronx', 420.0, 433.0, 425.0], ['11X509', '925 Astor Avenue', 'Bronx', 356.0, 340.0, 320.0], ['11X288', '925 Astor Avenue', 'Bronx', 488.0, 461.0, 458.0], ['11X508', '925 Astor Avenue', 'Bronx', 418.0, 432.0, 436.0], ['12X388', '1300 Boynton Avenue', 'Bronx', 317.0, 315.0, 292.0], ['12X478', '1551 East 172nd Street', 'Bronx', 430.0, 449.0, 448.0], ['12X692', '1300 Boynton Avenue', 'Bronx', 361.0, 354.0, 351.0], ['12X242', '1551 East 172nd Street', 'Bronx', 430.0, 422.0, 414.0], ['12X521', '1300 Boynton Avenue', 'Bronx', 444.0, 428.0, 422.0], ['12X550', '1300 Boynton Avenue', 'Bronx', 356.0, 359.0, 347.0], ['08X312', '1980 Lafayette Avenue', 'Bronx', 396.0, 413.0, 395.0], ['08X452', '1980 Lafayette Avenue', 'Bronx', 365.0, 393.0, 357.0], ['08X367', '456 White Plains Road', 'Bronx', 418.0, 430.0, 403.0], ['08X432', '1980 Lafayette Avenue', 'Bronx', None, None, None], ['08X305', '1980 Lafayette Avenue', 'Bronx', 394.0, 384.0, 383.0], ['08X282', '456 White Plains Road', 'Bronx', 386.0, 390.0, 389.0], ['08X561', '1980 Lafayette Avenue', 'Bronx', None, None, None], ['08X519', '1440 Story Avenue', 'Bronx', 389.0, 408.0, 413.0], ['08X376', '1980 Lafayette Avenue', 'Bronx', 435.0, 415.0, 423.0], ['11X249', '750 Baychester Avenue', 'Bronx', 407.0, 421.0, 427.0], ['11X455', '750 Baychester Avenue', 'Bronx', 400.0, 401.0, 391.0], ['24Q600', '37-02 47th Avenue', 'Long Island City', 467.0, 436.0, 432.0], ['24Q267', '30-20 Thomson Avenue', 'Long Island City', 435.0, 437.0, 441.0], ['24Q520', '45-35 Van Dam Street', 'Long Island City', 377.0, 389.0, 377.0], ['30Q301', '1-50 51st Avenue', 'Long Island City', 444.0, 458.0, 444.0], ['24Q610', '45-30 36th Street', 'Long Island City', 511.0, 464.0, 456.0], ['30Q575', '28-04 41st Avenue', 'Long Island City', 495.0, 482.0, 479.0], ['30Q555', '28-01 41st Avenue', 'Long Island City', 490.0, 374.0, 381.0], ['24Q299', '30-20 Thomson Avenue', 'Long Island City', 631.0, 598.0, 610.0], ['24Q530', '45-35 Van Dam Street', 'Long Island City', 425.0, 367.0, 365.0], ['30Q502', '21-16 44th Road', 'Long Island City', 443.0, 420.0, 411.0], ['24Q560', '47-07 30th Place', 'Long Island City', 478.0, 445.0, 445.0], ['24Q264', '30-20 Thomson Avenue', 'Long Island City', 489.0, 456.0, 459.0], ['30Q286', '23-15 Newtown Avenue', 'Astoria', 483.0, 464.0, 477.0], ['30Q445', '48-10 31st Avenue', 'Astoria', 466.0, 424.0, 426.0], ['30Q450', '14-30 Broadway', 'Astoria', 430.0, 423.0, 412.0], ['30Q501', '35-12 35th Avenue', 'Astoria', 536.0, 543.0, 543.0], ['30Q258', '36-41 28th Street', 'Astoria', None, None, None], ['30Q580', '34-12 36th Avenue', 'Astoria', 633.0, 620.0, 628.0], ['13K419', '49 Flatbush Avenue Extension', 'Brooklyn', 399.0, 397.0, 386.0], ['13K439', '49 Flatbush Avenue Extension', 'Brooklyn', 432.0, 334.0, 333.0], ['15K423', '112 Schermerhorn Street', 'Brooklyn', None, None, None], ['15K497', '284 Baltic Street', 'Brooklyn', 417.0, 406.0, 394.0], ['15K429', '284 Baltic Street', 'Brooklyn', 393.0, 381.0, 402.0], ['13K674', '105 Johnson Street', 'Brooklyn', 503.0, 477.0, 427.0], ['13K527', '283 Adams Street', 'Brooklyn', 397.0, 415.0, 407.0], ['13K483', '283 Adams Street', 'Brooklyn', 446.0, 443.0, 430.0], ['15K519', '347 Baltic Street', 'Brooklyn', 416.0, 420.0, 402.0], ['13K605', '105 Johnson Street', 'Brooklyn', 394.0, 422.0, 400.0], ['13K350', '49 Flatbush Avenue Extension', 'Brooklyn', 372.0, 372.0, 361.0], ['18K629', '5800 Tilden Avenue', 'Brooklyn', 382.0, 395.0, 384.0], ['17K745', '600 Kingston Avenue', 'Brooklyn', None, None, None], ['18K569', '5800 Tilden Avenue', 'Brooklyn', 378.0, 394.0, 388.0], ['17K531', '600 Kingston Avenue', 'Brooklyn', 398.0, 411.0, 400.0], ['18K563', '5800 Tilden Avenue', 'Brooklyn', 364.0, 374.0, 361.0], ['17K546', '600 Kingston Avenue', 'Brooklyn', 468.0, 454.0, 464.0], ['18K589', '905 Winthrop Street', 'Brooklyn', 370.0, 383.0, 374.0], ['17K533', '600 Kingston Avenue', 'Brooklyn', 386.0, 385.0, 390.0], ['20K609', '4200 16th Avenue', 'Brooklyn', 428.0, 413.0, 417.0], ['20K505', '5800 20th Avenue', 'Brooklyn', 504.0, 411.0, 407.0], ['13K412', '300 Willoughby Avenue', 'Brooklyn', 358.0, 386.0, 380.0], ['13K265', '101 Park Avenue', 'Brooklyn', 332.0, 346.0, 350.0], ['13K670', '71-77 Clinton Avenue', 'Brooklyn', 479.0, 484.0, 472.0], ['14K071', '215 Heyward Street', 'Brooklyn', 366.0, 356.0, 353.0], ['14K449', '223 Graham Avenue', 'Brooklyn', 625.0, 588.0, 591.0], ['14K322', '70 Tompkins Avenue', 'Brooklyn', None, None, None], ['14K614', '325 Bushwick Avenue', 'Brooklyn', None, None, None], ['14K454', '223 Graham Avenue', 'Brooklyn', 384.0, 398.0, 399.0], ['14K586', '223 Graham Avenue', 'Brooklyn', 374.0, 376.0, 357.0], ['19K510', '400 Pennsylvania Avenue', 'Brooklyn', 380.0, 389.0, 384.0], ['19K502', '400 Pennsylvania Avenue', 'Brooklyn', 365.0, 369.0, 357.0], ['19K660', '145 Pennsylvania Avenue', 'Brooklyn', 326.0, 333.0, 350.0], ['19K504', '400 Pennsylvania Avenue', 'Brooklyn', 391.0, 373.0, 376.0], ['19K507', '400 Pennsylvania Avenue', 'Brooklyn', 375.0, 393.0, 394.0], ['19K409', '2057 Linden Boulevard', 'Brooklyn', 464.0, 451.0, 421.0], ['19K639', '999 Jamaica Avenue', 'Brooklyn', 383.0, 376.0, 370.0], ['19K583', '999 Jamaica Avenue', 'Brooklyn', 319.0, 323.0, 284.0], ['19K683', '370 Fountain Avenue', 'Brooklyn', 387.0, 391.0, 383.0], ['19K764', '999 Jamaica Avenue', 'Brooklyn', None, None, None], ['19K422', '1065 Elton Street', 'Brooklyn', None, None, None], ['19K615', '1 Wells Street', 'Brooklyn', 387.0, 387.0, 384.0], ['19K659', '999 Jamaica Avenue', 'Brooklyn', 365.0, 370.0, 362.0], ['19K404', '1065 Elton Street', 'Brooklyn', 382.0, 413.0, 391.0], ['19K618', '999 Jamaica Avenue', 'Brooklyn', 395.0, 376.0, 359.0], ['20K490', '8301 Shore Road', 'Brooklyn', 513.0, 456.0, 451.0], ['22K405', '2839 Bedford Avenue', 'Brooklyn', 550.0, 514.0, 516.0], ['14K474', '850 Grand Street', 'Brooklyn', 380.0, 377.0, 384.0], ['14K478', '850 Grand Street', 'Brooklyn', 463.0, 446.0, 425.0], ['14K488', '257 North 6th Street', 'Brooklyn', 391.0, 406.0, 391.0], ['14K685', '250 Hooper Street', 'Brooklyn', 344.0, 380.0, 379.0], ['14K477', '850 Grand Street', 'Brooklyn', 393.0, 390.0, 394.0], ['14K561', '257 North 6th Street', 'Brooklyn', 443.0, 440.0, 430.0], ['14K558', '257 North 6th Street', 'Brooklyn', 415.0, 424.0, 407.0], ['23K514', '226 Bristol Street', 'Brooklyn', 400.0, 407.0, 394.0], ['23K697', '226 Bristol Street', 'Brooklyn', 394.0, 399.0, 412.0], ['17K122', '150 Albany Avenue', 'Brooklyn', 446.0, 442.0, 410.0], ['17K751', '150 Albany Avenue', 'Brooklyn', 406.0, 405.0, 396.0], ['16K455', '1700 Fulton Street', 'Brooklyn', 399.0, 392.0, 394.0], ['16K765', '1700 Fulton Street', 'Brooklyn', None, None, None], ['21K348', '2630 Benson Avenue', 'Brooklyn', 367.0, 374.0, 361.0], ['21K690', '8310 21st Avenue', 'Brooklyn', 458.0, 434.0, 434.0], ['21K337', '2630 Benson Avenue', 'Brooklyn', 424.0, 343.0, 337.0], ['21K572', '2630 Benson Avenue', 'Brooklyn', 420.0, 396.0, 396.0], ['20K445', '1601 80th Street', 'Brooklyn', 488.0, 422.0, 417.0], ['21K559', '2630 Benson Avenue', 'Brooklyn', 369.0, 379.0, 378.0], ['21K468', '2630 Benson Avenue', 'Brooklyn', 474.0, 462.0, 449.0], ['15K463', '237 7th Avenue', 'Brooklyn', 408.0, 435.0, 415.0], ['15K684', '237 7th Avenue', 'Brooklyn', 553.0, 551.0, 539.0], ['15K464', '237 7th Avenue', 'Brooklyn', 405.0, 377.0, 395.0], ['15K462', '237 7th Avenue', 'Brooklyn', 420.0, 424.0, 414.0], ['13K595', '1119 Bedford Avenue', 'Brooklyn', 505.0, 464.0, 456.0], ['15K592', '362 Schermerhorn Street', 'Brooklyn', None, None, None], ['15K656', '345 Dean Street', 'Brooklyn', 439.0, 441.0, 436.0], ['13K430', '29 Ft Greene Place', 'Brooklyn', 682.0, 608.0, 606.0], ['22K555', '350 Coney Island Avenue', 'Brooklyn', 502.0, 495.0, 493.0], ['20K485', '350 67th Street', 'Brooklyn', 475.0, 440.0, 445.0], ['32K545', '1155 Dekalb Avenue', 'Brooklyn', 389.0, 374.0, 378.0], ['16K498', '1396 Broadway', 'Brooklyn', 395.0, 401.0, 383.0], ['16K688', '125 Stuyvesant Avenue', 'Brooklyn', 395.0, 382.0, 391.0], ['16K393', '1014 Lafayette Avenue', 'Brooklyn', None, None, None], ['32K556', '797 Bushwick Avenue', 'Brooklyn', 393.0, 368.0, 382.0], ['14K610', '50 Bedford Avenue', 'Brooklyn', 367.0, 381.0, 328.0], ['14K632', '50 Bedford Avenue', 'Brooklyn', 399.0, 413.0, 400.0], ['21K540', '50 Avenue X', 'Brooklyn', 512.0, 418.0, 396.0], ['21K344', '521 West Avenue', 'Brooklyn', 436.0, 430.0, 421.0], ['17K548', '883 Classon Avenue', 'Brooklyn', 382.0, 393.0, 377.0], ['17K547', '883 Classon Avenue', 'Brooklyn', 419.0, 411.0, 416.0], ['17K590', '1186 Carroll Street', 'Brooklyn', 525.0, 500.0, 481.0], ['17K600', '901 Classon Avenue', 'Brooklyn', 408.0, 424.0, 407.0], ['17K524', '883 Classon Avenue', 'Brooklyn', 344.0, 302.0, 300.0], ['17K528', '883 Classon Avenue', 'Brooklyn', 377.0, 386.0, 375.0], ['17K543', '911 Flatbush Avenue', 'Brooklyn', 496.0, 491.0, 484.0], ['17K382', '911 Flatbush Avenue', 'Brooklyn', 386.0, 397.0, 393.0], ['17K537', '911 Flatbush Avenue', 'Brooklyn', 360.0, 382.0, 359.0], ['17K539', '911 Flatbush Avenue', 'Brooklyn', 377.0, 382.0, 356.0], ['17K408', '911 Flatbush Avenue', 'Brooklyn', 374.0, 385.0, 375.0], ['22K425', '3787 Bedford Avenue', 'Brooklyn', 492.0, 450.0, 444.0], ['21K525', '1600 Avenue L', 'Brooklyn', 500.0, 479.0, 472.0], ['15K448', '610 Henry Street', 'Brooklyn', 401.0, 411.0, 404.0], ['15K667', '153 35th Street', 'Brooklyn', 398.0, 380.0, 381.0], ['23K493', '2021 Bergen Street', 'Brooklyn', 394.0, 395.0, 399.0], ['16K594', '265 Ralph Avenue', 'Brooklyn', 377.0, 396.0, 386.0], ['23K644', '1137 Herkimer Street', 'Brooklyn', None, None, None], ['22K535', '1830 Shore Boulevard', 'Brooklyn', 563.0, 534.0, 543.0], ['21K410', '2800 Ocean Parkway', 'Brooklyn', 441.0, 422.0, 422.0], ['22K611', '3000 Avenue X', 'Brooklyn', None, None, None], ['21K620', '25 Brighton 4th Road', 'Brooklyn', 416.0, 423.0, 387.0], ['18K642', '1600 Rockaway Parkway', 'Brooklyn', 362.0, 396.0, 393.0], ['18K566', '6565 Flatlands Avenue', 'Brooklyn', 392.0, 406.0, 403.0], ['18K633', '1600 Rockaway Parkway', 'Brooklyn', 404.0, 427.0, 424.0], ['18K617', '1600 Rockaway Parkway', 'Brooklyn', 390.0, 410.0, 397.0], ['18K576', '6565 Flatlands Avenue', 'Brooklyn', 386.0, 408.0, 402.0], ['18K567', '6565 Flatlands Avenue', 'Brooklyn', 379.0, 393.0, 373.0], ['18K637', '6565 Flatlands Avenue', 'Brooklyn', 381.0, 397.0, 390.0], ['32K554', '321 Palmetto Street', 'Brooklyn', 467.0, 446.0, 448.0], ['32K168', '400 Irving Avenue', 'Brooklyn', None, None, None], ['32K549', '400 Irving Avenue', 'Brooklyn', 365.0, 357.0, 357.0], ['32K403', '400 Irving Avenue', 'Brooklyn', 365.0, 366.0, 348.0], ['32K552', '400 Irving Avenue', 'Brooklyn', 392.0, 374.0, 379.0], ['13K499', '561 Grand Avenue', 'Brooklyn', 379.0, 395.0, 385.0], ['25Q460', '35-01 Union Street', 'Flushing', 444.0, 407.0, 405.0], ['25Q241', '35-01 Union Street', 'Flushing', None, None, None], ['25Q240', '35-01 Union Street', 'Flushing', None, None, None], ['25Q281', '46-21 Colden Street', 'Flushing', 521.0, 457.0, 451.0], ['25Q263', '144-80 Barclay Avenue', 'Flushing', 481.0, 323.0, 323.0], ['25Q285', '34-65 192nd Street', 'Flushing', 484.0, 491.0, 487.0], ['26Q495', '32-24 Corporal Kennedy Street', 'Bayside', 523.0, 479.0, 485.0], ['26Q415', '57-00 223rd Street', 'Oakland Gardens', 563.0, 505.0, 510.0], ['26Q430', '58-20 Utopia Parkway', 'Fresh Meadows', 562.0, 483.0, 485.0], ['25Q252', '158-40 76th Road', 'Fresh Meadows', 516.0, 493.0, 486.0], ['25Q670', '75-40 Parsons Boulevard', 'Fresh Meadows', 460.0, 426.0, 423.0], ['25Q425', '63-25 Main Street', 'Flushing', 467.0, 422.0, 425.0], ['25Q525', '149-11 Melbourne Avenue', 'Flushing', 680.0, 640.0, 661.0], ['24Q550', '105-25 Horace Harding Expressway', 'Corona', 413.0, 405.0, 393.0], ['24Q293', '45-10 94th Street', 'Elmhurst', 435.0, 424.0, 418.0], ['24Q585', '54-40 74th Street', 'Elmhurst', 476.0, 471.0, 480.0], ['24Q296', '45-10 94th Street', 'Elmhurst', 340.0, 320.0, 318.0], ['24Q236', '48-01 90th Street', 'Elmhurst', None, None, None], ['24Q455', '48-01 90th Street', 'Elmhurst', 434.0, 401.0, 389.0], ['28Q440', '67-01 110th Street', 'Forest Hills', 517.0, 485.0, 483.0], ['28Q167', '91-30 Metropolitan Avenue', 'Forest Hills', None, None, None], ['28Q686', '91-30 Metropolitan Avenue', 'Forest Hills', 460.0, 448.0, 449.0], ['24Q485', '21-27 Himrod Street', 'Ridgewood', 452.0, 422.0, 416.0], ['29Q313', '207-01 116th Avenue', 'Cambria Heights', None, None, None], ['29Q498', '207-01 116th Avenue', 'Cambria Heights', 384.0, 409.0, 401.0], ['29Q243', '207-01 116th Avenue', 'Cambria Heights', None, None, None], ['29Q492', '207-01 116th Avenue', 'Cambria Heights', 380.0, 418.0, 388.0], ['29Q259', '109-89 204th Street', 'Saint Albans', 405.0, 427.0, 409.0], ['29Q265', '143-10 Springfield Boulevard', 'Springfield Gardens', 384.0, 407.0, 400.0], ['29Q283', '143-10 Springfield Boulevard', 'Springfield Gardens', 398.0, 410.0, 393.0], ['29Q248', '143-10 Springfield Boulevard', 'Springfield Gardens', 423.0, 422.0, 403.0], ['29Q272', '143-10 Springfield Boulevard', 'Springfield Gardens', 439.0, 428.0, 419.0], ['27Q650', '94-06 104th Street', 'Ozone Park', 489.0, 457.0, 451.0], ['27Q480', '101-01 Rockaway Boulevard', 'Ozone Park', 418.0, 401.0, 395.0], ['27Q308', '138-30 Lafayette Street', 'Ozone Park', 426.0, 435.0, 424.0], ['27Q475', '89-30 114th Street', 'Richmond Hill', 413.0, 406.0, 399.0], ['27Q334', '94-25 117th Street', 'South Richmond Hill', None, None, None], ['27Q314', '121-10 Rockaway Boulevard', 'Queens', None, None, None], ['29Q326', '188-04 91st Avenue', 'Hollis', 418.0, 424.0, 411.0], ['26Q566', '74-20 Commonwealth Boulevard', 'Bellerose', 453.0, 434.0, 439.0], ['26Q315', '230-17 Hillside Avenue', 'Queens Village', None, None, None], ['26Q435', '230-17 Hillside Avenue', 'Queens Village', 397.0, 396.0, 391.0], ['28Q680', '160-20 Goethals Avenue', 'Jamaica', 524.0, 511.0, 514.0], ['28Q350', '167-01 Gothic Drive', 'Jamaica', 487.0, 460.0, 463.0], ['28Q328', '167-01 Gothic Drive', 'Jamaica', 415.0, 392.0, 386.0], ['28Q896', '150-91 87th Road', 'Jamaica', 415.0, 420.0, 433.0], ['28Q310', '167-01 Gothic Drive', 'Jamaica', 455.0, 439.0, 441.0], ['28Q505', '160-05 Highland Avenue', 'Jamaica', 448.0, 432.0, 426.0], ['28Q620', '165-65 84th Avenue', 'Jamaica', 514.0, 473.0, 470.0], ['28Q325', '167-01 Gothic Drive', 'Jamaica', 409.0, 399.0, 404.0], ['28Q284', '108-35 167th Street', 'Jamaica', 496.0, 481.0, 473.0], ['28Q687', '94-50 159th Street', 'Jamaica', 701.0, 621.0, 625.0], ['28Q690', '116-25 Guy R Brewer Boulevard', 'Jamaica', 410.0, 431.0, 409.0], ['29Q327', '171-10 Linden Boulevard', 'Jamaica', None, None, None], ['27Q400', '156-10 Baisley Boulevard', 'Jamaica', 366.0, 372.0, 364.0], ['27Q260', '8-21 Bay 25th Street', 'Far Rockaway', 410.0, 418.0, 407.0], ['27Q309', '8-21 Bay 25th Street', 'Far Rockaway', 422.0, 424.0, 415.0], ['27Q302', '8-21 Bay 25th Street', 'Far Rockaway', 372.0, 362.0, 352.0], ['27Q324', '100-00 Beach Channel Drive', 'Rockaway Park', 357.0, 381.0, 376.0], ['27Q262', '100-00 Beach Channel Drive', 'Rockaway Park', 427.0, 430.0, 423.0], ['27Q351', '100-00 Beach Channel Drive', 'Rockaway Park', 399.0, 403.0, 405.0], ['27Q323', '320 Beach 104th Street', 'Rockaway Park', 588.0, 560.0, 568.0]]

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

def transform(raw_data):
	raw_data.fillna(
    	value={
			# Fill NaN values with column mean
			"math_score": raw_data["math_score"].mean(),
			"reading_score": raw_data["reading_score"].mean(),
			"writing_score": raw_data["writing_score"].mean()
		}, inplace=True
	)
	return raw_data

clean_testing_scores = transform(raw_testing_scores)

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

def transform(raw_data):
	# Use .loc[] to only return the needed columns
	raw_data = raw_data.loc[:, ["city","math_score","reading_score","writing_score"]]
	
    # Group the data by city, return the grouped DataFrame
	grouped_data = raw_data.groupby(by=["city"], axis=0).mean()
	return grouped_data

# Transform the data, print the head of the DataFrame
grouped_testing_scores = transform(raw_testing_scores)
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

def transform(raw_data):
	# Use the apply function to extract the street_name from the street_address
    raw_data["street_name"] = raw_data.apply(
   		# Pass the correct function to the apply method
        find_street_name,
        axis=1
    )
    return raw_data

# Transform the raw_testing_scores DataFrame
cleaned_testing_scores = transform(raw_testing_scores)

# Print the head of the cleaned_testing_scores DataFrame
print(cleaned_testing_scores.head())

"""
The find_street_name() function parses the street name from the "street_address", 
dropping the street number from the string. This function has been loaded into memory, 
and is ready to be applied to the raw_testing_scores DataFrame.

                  street_address       city  math_score  reading_score  writing_score       street_name
    02M260  425 West 33rd Street  Manhattan         NaN            NaN            NaN  West 33rd Street
    06M211    650 Academy Street  Manhattan         NaN            NaN            NaN    Academy Street
    01M539   111 Columbia Street  Manhattan       657.0          601.0          601.0   Columbia Street
    02M294      350 Grand Street  Manhattan       395.0          411.0          387.0      Grand Street
    02M308      350 Grand Street  Manhattan       418.0          428.0          415.0      Grand Street
"""

####################################################

# Update the connection string, create the connection object to the schools database
db_engine = sqlalchemy.create_engine("postgresql+psycopg2://repl:password@localhost:5432/schools")

# Write the DataFrame to the scores table
cleaned_testing_scores.to_sql(
	name="scores",
	con=db_engine,
	index=False,
	if_exists="replace"
)

####################################################

def load(clean_data, con_engine):
    clean_data.to_sql(name="scores_by_city", con=con_engine, if_exists="replace", index=True, index_label="school_id")
    
# Call the load function, passing in the cleaned DataFrame
load(cleaned_testing_scores, db_engine)

# Call query the data in the scores_by_city table, check the head of the DataFrame
to_validate = pd.read_sql("SELECT * FROM scores_by_city", con=db_engine)
print(to_validate.head())

"""
      school_id       street_address       city  math_score  reading_score  writing_score  city_rank
    0    01M539  111 Columbia Street  Manhattan       657.0          601.0          601.0        4.0
    1    02M294     350 Grand Street  Manhattan       395.0          411.0          387.0       54.0
    2    02M308     350 Grand Street  Manhattan       418.0          428.0          415.0       41.0
    3    02M545     350 Grand Street  Manhattan       613.0          453.0          463.0       18.0
    4    01M292     220 Henry Street  Manhattan       410.0          406.0          381.0       52.0
"""

####################################################

####################################################