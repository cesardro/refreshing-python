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

#Pickle files
print("\n*****Pickle File*****")
# Pickle files are a way to store python objects in a file. They are used to save and load data in Python.
import pickle

# Load the pickled data: d, rb -> read binary
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)

print(d)
print(type(d))

####################################
file = 'battledeath.xlsx'
# Load spreadsheet: xls
xls = pd.ExcelFile(file)

print(xls.sheet_names)
####################################
xls = pd.ExcelFile('sales.xlsx')
print(xls.sheet_names)
# ['2003', '2004', '2005']
df1 = xls.parse('2004')
####################################
# Same as above, but now we use the sheet index instead of the name.
df1 = pd.read_excel('sales.xlsx', sheet_name='2004')
####################################
# Load a sheet into a DataFrame by name.
df1 = xls.parse('2004')

# Load a sheet into a DataFrame by index.
df2 = xls.parse(0)

print(df1.head())
print(df2.head())
#####################################
# Parse -> Load a specific sheet of an Excel file into a DataFrame.
# First argument is the sheet name or index, and the second argument is a list of options to customize the loading process.
# Skiprows -> Skip the first row of the sheet, always with a list.
# Names -> Rename the columns of the DataFrame, always with a list.
# Usecols -> Load only the first column of the sheet into a DataFrame, always with a list.
df1 = xls.parse(0, skiprows=[0], names=['Country','AAM due to War (2002)'])
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

print(df1.head())
print(df2.head())

# SAS and Stata files
print("\n*****SAS and Stata Files*****")
# SAS -> Statistical Analysis System.
# Stata -> Statistical + Data Analysis.
# SAS: Business Analytics and biostatistics.
# Stata: Academic social science and research.
# SAS is used for -> Advanced analytics, multivariate analysis, business intelligence, data management, predictive analytics and standard for computational statistics.

from sas7bdat import SAS7BDAT

# to_data_frame() -> Convert the SAS dataset to a pandas DataFrame.
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

print(df_sas.head())

# read_stata() -> Read a Stata file into a pandas DataFrame.
df = pd.read_stata('disarea.dta')

print(df.head())

# HDF5 files
print("\n*****HDF5 Files*****")
# HDF5 -> Hierarchical Data Format version 5.
# Standard for soring large quantities of numerical data.
# Datasets can be hundreds of gigabytes in size, and can be organized in a hierarchical structure.
# HDF5 files are used in -> High performance computing, scientific computing, and data analysis

import h5py

file = 'LIGO_data.hdf5'
data = h5py.File(file, 'r')

print(type(data))

# data.keys() -> List the names of the datasets in the file.
for key in data.keys():
    print(key)

#Matlab files
print("\n*****Matlab Files*****")
# MATLAB -> Matrix Laboratory.
# Standard in engineering and scientific computing.
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat)) # <class 'dict'>
