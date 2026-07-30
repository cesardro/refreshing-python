# Numeric Data

# ride_sharing is a DataFrame from Pandas CSV.
ride_sharing = []
# Description of dataframe, with details.
print(ride_sharing.info())
'''
<class 'pandas.core.frame.DataFrame'>
Index: 25760 entries, 0 to 25759
Data columns (total 9 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   duration         25760 non-null  object
 1   station_A_id     25760 non-null  int64 
 2   station_A_name   25760 non-null  object
 3   station_B_id     25760 non-null  int64 
 4   station_B_name   25760 non-null  object
 5   bike_id          25760 non-null  int64 
 6   user_type        25760 non-null  int64 
 7   user_birth_year  25760 non-null  int64 
 8   user_gender      25760 non-null  object
dtypes: int64(5), object(4)
memory usage: 2.0+ MB
None
'''
# Generates descriptive statistics.
print(ride_sharing['user_type'].describe())
'''
count    25760.000
mean         2.008
std          0.705
min          1.000
25%          2.000
50%          2.000
75%          3.000
max          3.000
Name: user_type, dtype: float64
'''

# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype  == 'category'

# Print new summary statistics 
print(ride_sharing['user_type_cat'].describe())
'''
count     25760
unique        3
top           2
freq      12972
Name: user_type_cat, dtype: int64
'''

# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
'''
             duration duration_trim  duration_time
    0      12 minutes           12              12
    1      24 minutes           24              24
    2       8 minutes            8               8
    3       4 minutes            4               4
    4      11 minutes           11              11
    ...           ...           ...            ...
    25755  11 minutes           11              11
    25756  10 minutes           10              10
    25757  14 minutes           14              14
    25758  14 minutes           14              14
    25759  29 minutes           29              29
'''
print(ride_sharing['duration_time'].mean()) #11.389052795031056

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())
'''
    count     25760
    unique        2
    top          27
    freq      13274
    Name: tire_sizes, dtype: int64
'''

import pandas as pd
import datetime as dt

# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max()) #2026-07-30

# Duplicates.
# .duplicated() ->
# subset: List of column names to check for duplication.
# keep: Whether to keep first ('first'), last('last') or all(False) duplicated values.

# Find duplicates
duplicates = ride_sharing.duplicated('ride_id', False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])

'''
        ride_id  duration  user_birth_year
    22       33        10             1979
    39       33         2             1979
    53       55         9             1985
    65       55         9             1985
    74       71        11             1997
    75       71        11             1997
    76       89         9             1986
    77       89         9             2060
'''

# .drop_duplicates() ->
# subset: List of column names to check for duplication.
# keep: Whether to keep first ('first'), last('last') or all(False) duplicated values.
# inplace: Drop duplicated rows directly inside DataFrame without creating new object (True).

# Drop complete duplicates from ride_sharing - creating a new object.
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby('ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0