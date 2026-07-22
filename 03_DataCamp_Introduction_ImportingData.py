#Reading text file
print("\n*****Text File*****")
# r to only read.
# w to write.
# We can use "with" so everything done inside of function will be automatically closed when finished function.

# Open a file as read-only and bind it to file
with open('moby_dick.txt', 'r') as file:
  	# Print it
    print(file.read())

# Read & print the first 3 lines
with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

#Flat files
print("\n*****Flat file with NUMPY*****")

import numpy as np

file = 'digits.csv'

digits = np.loadtxt(file, delimiter=',')

print(digits)
###################################################
# Assign the filename: file
file2 = 'digits_header.txt'

# Delimiter tab, skip 1st row, only use 1st and 3rd row.
data = np.loadtxt(file2, delimiter='\t', skiprows=1, usecols=[0,2])

print(data)
###################################################
# Assign filename: file
file = 'seaslug.txt'

# Import file: data
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import file as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

print("\n*****Flat file with PANDAS*****")

import pandas as pd

file = 'titanic.csv'

df = pd.read_csv(file)

print(df.head())
###################################################

file = 'digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows=5, header=None)

# Build a numpy array from the DataFrame: data_array
data_array = data.to_numpy()

# Print the datatype of data_array to the shell
print(type(data_array))
###################################################
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

file = 'titanic_corrupt.txt'

# Tab delimiter, commets are after # and N/A values are found as Nothing.
data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()