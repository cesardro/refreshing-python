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
