# Flat Files
import pandas as pd

# Create list of columns to use
cols = ['zipcode', 'agi_stub', 'mars1', 'MARS2', 'NUMDEP']

# Create dataframe from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols=cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())

'''
    agi_stub  zipcode   mars1  MARS2  NUMDEP                          
    1         1439444  170320  28480   52490
    2         1439444  104000  37690   64660
    3         1439444   39160  45390   47330
    4         1439444   11670  44410   37760
    5         1439444    7820  67750   60730
    6         1439444    1210  16340   16300
'''

# Create dataframe of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("vt_tax_data_2016.csv",
                              nrows=500,
                              skiprows=500,
                              header=None,
                              names=list(vt_data_first500))

# View the Vermont dataframes to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())

'''
       STATEFIPS STATE  zipcode  agi_stub      N1  ...  A85300  N11901  A11901  N11902  A11902
    0         50    VT        0         1  111580  ...       0   10820    9734   88260  138337
    1         50    VT        0         2   82760  ...       0   12820   20029   68760  151729
    2         50    VT        0         3   46270  ...       0   10810   24499   34600   90583
    3         50    VT        0         4   30070  ...       0    7320   21573   21300   67045
    4         50    VT        0         5   39530  ...       0   12500   67761   23320  103034
    
       STATEFIPS STATE  zipcode  agi_stub   N1  ...  A85300  N11901  A11901  N11902  A11902
    0         50    VT     5356         2  180  ...       0      50      76     130     212
    1         50    VT     5356         3   80  ...       0      40     142      50     148
    2         50    VT     5356         4   50  ...       0       0       0      30      87
    3         50    VT     5356         5   80  ...       0      30     531      30     246
    4         50    VT     5356         6    0  ...       0       0       0       0       0
'''

# Create dict specifying data types for agi_stub and zipcode
data_types = {'agi_stub': 'category',
                          'zipcode': str}

# Load csv using dtype to set correct data types
data = pd.read_csv("vt_tax_data_2016.csv", dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())

'''
STATEFIPS       int64
STATE          object
zipcode        object
agi_stub     category
N1              int64
'''

# Create dict specifying that 0s in zipcode are NA values
null_values = {'zipcode': 0}

# Load csv using na_values keyword argument
data = pd.read_csv("vt_tax_data_2016.csv",
                   na_values=null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])

'''
       STATEFIPS STATE  zipcode  agi_stub      N1  ...  A85300  N11901  A11901  N11902  A11902
    0         50    VT      NaN         1  111580  ...       0   10820    9734   88260  138337
    1         50    VT      NaN         2   82760  ...       0   12820   20029   68760  151729
    2         50    VT      NaN         3   46270  ...       0   10810   24499   34600   90583
    3         50    VT      NaN         4   30070  ...       0    7320   21573   21300   67045
    4         50    VT      NaN         5   39530  ...       0   12500   67761   23320  103034
    5         50    VT      NaN         6    9620  ...   20428    3900   93123    2870   39425
'''
# Error_bad_lines -> False -> Skip bad lines and keep the others
# Warn_bad_lines -> True -> Display messages when unparseable lines are skipped.

try:
  # Set warn_bad_lines to issue warnings about bad records
  data = pd.read_csv("vt_tax_data_2016_corrupt.csv", 
                     error_bad_lines=False, 
                     warn_bad_lines=True)
  
  # View first 5 records
  print(data.head())
  
except pd.errors.ParserError:
    print("Your data contained rows that could not be parsed.")