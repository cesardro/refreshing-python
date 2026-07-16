#Modules
#OS is to interact with our operating system.
import os
print("\n*****OS*****")
print("Current working directory:", os.getcwd())
#print("Environment variables:", os.environ)

#string module is to work with strings.
import string
print("\n*****String*****")
print(string.ascii_lowercase)
print(string.punctuation)

#Packages
# "python3 -m pip install <package_name>" to install a package
import pandas as pd
print("\n*****Packages*****")
sales = {"user_id": ["KM37", "PR19", "YU88"],"order_value": [197.75, 208.21, 134.99]}
sales_df = pd.DataFrame(sales)
print(sales_df.head()) # Print the first 5 rows of the DataFrame
#sales_df = pd.read_csv("sales.csv") # Read a CSV file into a DataFrame
print(sales_df.info()) # Print information about the DataFrame, including the number of non-null values and data types

#Functions
print("\n*****Functions*****")
def average(values):
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)
    return rounded_average

preparation_times = [19.23, 15.67, 48.57, 23.45, 12.06, 34.56, 45.67]
print(average(preparation_times)) # Call the function and print the result

#Arguments
# Arguments are values provided to a function when it is called. They can be positional or keyword arguments. 
# Positional arguments are assigned based on their position in the function call, while keyword arguments are assigned based on their name.
# Keyword arguments are specified by the name of the parameter followed by an equal sign and the value.

#Keywords
print("\n*****Keywords*****")
print(help(round)) # Print the documentation for the round() function

original_price = 899.99

def calculate_discount(price, discount_percent=15, round_result=True):
    """Alejandro Doc: Calculate the discounted price of an item."""
    discounted_price = price - (price * (discount_percent / 100))
    
    if round_result == True:
        return round(discounted_price, 2)
    else:
        return discounted_price

final_price = calculate_discount(price=original_price, discount_percent=25, round_result=False)
print(final_price)

#Docstrings
print("\n*****Docstrings*****")
print(round.__doc__) # Print the docstring of the function
print("\n" + calculate_discount.__doc__ + "\n") # Print the docstring of the function

def clean_text(text, lower=True):
    """
    Clean text by swapping spaces to underscores and converting to lowercase.
    
    Args:
    	text (str): A string to be cleaned.
    	lower (bool): Whether to convert the text to lowercase.
    
    Returns:
    	text (str): Cleaned string.
    """
    clean_text = text.replace(' ', '_')
    if lower == False:
        return clean_text
    else:
        return clean_text.lower()
      
print(help(clean_text))

#Arguments
print("\n*****Arguments*****")
#*args allows you to pass a variable number of arguments to a function. It collects them into a tuple.
def concat(*args):
    """Concatenates multiple string arguments with spaces between them."""
    print("Tuple of arguments:", args)
    result = ""

    for arg in args:
        result += " " + arg
    return result

print(concat("Python", "is", "great!"))

#**kwargs allows you to pass a variable number of keyword arguments to a function. It collects them into a dictionary.
def concat(**kwargs):
    """Concatenates keyword arguments into a single string with spaces."""
    print("Dictionary of keyword arguments:", kwargs)
    result = ""

    for kwarg in kwargs.values():
        result += " " + kwarg
    return result

print(concat(start="Python", middle="is", end="great!"))