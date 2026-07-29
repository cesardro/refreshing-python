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

#Lambda Functions
print("\n*****Lambda Functions*****")
#Lambda functions are anonymous functions defined using the lambda keyword. 
#They can take any number of arguments but can only have one expression. The expression is evaluated and returned when the function is called.
#Lambda functions are often used for short, simple operations that can be defined in a single line
#Lambda VS Custom Functions.
#For complex tasks and same task repeated multiple times, custom functions are better.
#For performed once and simple tasks, lambda functions are better.

file_size = 2500
extra_space = 0.15

# Define a lambda function
calculate_total = lambda x: x * (1 + extra_space)

# Call the lambda function
print(calculate_total(file_size))

# Call a lambda function in one line
print((lambda x: x * (1 + extra_space))(file_size))

###################################################################
colleagues = ["Sarah Martinez", "Michael Chen", "Emily Brown"]

# Apply the lambda function to each colleague's name
# Map function applies the lambda function to each element in the colleagues list and returns a map object.
# Basically, do this fuction with every element in the list and return a new list with the results.
cleaned = map(lambda x: x.replace(" ", "_").lower(), colleagues)

# Convert map object to list
cleaned_list = list(cleaned)
print(cleaned_list)

#Error Handling
print("\n*****Error Handling*****")

def clean_text(text):
  # Attempt to clean the text
  try:
    return text.replace(" ", "_").lower()
  # Run this code if an error occurs
  except:
    print("The clean_text() function expects a string as an argument, please check the data type provided!")
    
clean_text(187)

def clean_text1(text):
  # Check the data type
  if type(text) == str:
    return text.replace(" ", "_").lower()
  else:
    # Return a TypeError error if the wrong data type was used
    raise TypeError("The clean_text() function expects a string as an argument, please check the data type provided!")
    
clean_text1("User Name 187")