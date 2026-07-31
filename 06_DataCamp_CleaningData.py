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

# Membership Connstrain

'''
# Print categories DataFrame
print(categories)

      cleanliness           safety          satisfaction
0           Clean          Neutral        Very satisfied
1         Average        Very safe               Neutral
2  Somewhat clean    Somewhat safe    Somewhat satisfied
3  Somewhat dirty      Very unsafe  Somewhat unsatisfied
4           Dirty  Somewhat unsafe      Very unsatisfied

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")

Cleanliness:  ['Clean', 'Average', 'Unacceptable', 'Somewhat clean', 'Somewhat dirty', 'Dirty']
Categories (6, object): ['Average', 'Clean', 'Dirty', 'Somewhat clean', 'Somewhat dirty', 'Unacceptable'] 

print('Safety: ', airlines['safety'].unique(), "\n")
Safety:  ['Neutral', 'Very safe', 'Somewhat safe', 'Very unsafe', 'Somewhat unsafe']
Categories (5, object): ['Neutral', 'Somewhat safe', 'Somewhat unsafe', 'Very safe', 'Very unsafe'] 

print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")
Satisfaction:  ['Very satisfied', 'Neutral', 'Somewhat satisfied', 'Somewhat unsatisfied', 'Very unsatisfied']
Categories (5, object): ['Neutral', 'Somewhat satisfied', 'Somewhat unsatisfied', 'Very satisfied', 'Very unsatisfied'] 
'''

'''
# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

           id        day           airline  destination  dest_region dest_size boarding_area   dept_time  wait_min   cleanliness         safety        satisfaction
    4    2992  Wednesday          AMERICAN        MIAMI      East US       Hub   Gates 50-59  2018-12-31     559.0  Unacceptable      Very safe  Somewhat satisfied
    18   2913     Friday  TURKISH AIRLINES     ISTANBUL  Middle East       Hub  Gates 91-102  2018-12-31     225.0  Unacceptable      Very safe  Somewhat satisfied
    100  2321  Wednesday         SOUTHWEST  LOS ANGELES      West US       Hub   Gates 20-39  2018-12-31     130.0  Unacceptable  Somewhat safe  Somewhat satisfied

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])
'''

# Categorical 
airlines = ()

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

'''
    ['Asia' 'Canada/Mexico' 'West US' 'East US' 'Midwest US' 'EAST US'
     'Middle East' 'Europe' 'eur' 'Central/South America'
     'Australia/New Zealand' 'middle east']
    ['Hub' 'Small' '    Hub' 'Medium' 'Large' 'Hub     ' '    Small'
     'Medium     ' '    Medium' 'Small     ' '    Large' 'Large     ']
'''

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower() 
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()

# Verify changes have been effected
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

'''
    ['asia' 'canada/mexico' 'west us' 'east us' 'midwest us' 'middle east'
     'europe' 'central/south america' 'australia/new zealand']
    ['Hub' 'Small' 'Medium' 'Large']
'''
import numpy as np

# Create ranges -> 0 -------- 60 -------- 180 -------- ∞
label_ranges = [0, 60, 180, np.inf]
# Create intervals.
label_names = ['short', 'medium', 'long']

# Create wait_type column
# .cut() converts continue numeric values into categories based on intervals.
# airlines['wait_min'] -> 45, bins -> range 0-60-180+, labels -> name of catergory
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, labels = label_names)

# Create mapping dictionary
mappings = {
    'Monday': 'weekday',
    'Tuesday': 'weekday',
    'Wednesday': 'weekday',
    'Thursday': 'weekday',
    'Friday': 'weekday',
    'Saturday': 'weekend',
    'Sunday': 'weekend'
}

airlines['day_week'] = airlines['day'].replace(mappings)

# Clean text data. 

# Replace "Dr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss","")

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.","")

# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False

############################

# Store length of each row in survey_response column
resp_length = airlines['survey_response'].str.len()

# Find rows in airlines where resp_length > 40
airlines_survey = airlines[resp_length > 40]

# Assert minimum survey_response length is > 40
assert airlines_survey['survey_response'].str.len().min() > 40

# Print new survey_response column
print(airlines_survey['survey_response'])

'''
    18    The airport personnell forgot to alert us of d...
    19    The food in the airport was really really expe...
    20    One of the other travelers was really loud and...
    21    I don't remember answering the survey with the...
    22    The airport personnel kept ignoring my request...
    23    The chair I sat in was extremely uncomfortable...
    24    I wish you were more like other airports, the ...
    25    I was really unsatisfied with the wait times b...
    27    The flight was okay, but I didn't really like ...
    28    We were really slowed down by security measure...
    29    There was a spill on the aisle next to the bat...
    30    I felt very unsatisfied by how long the flight...
    Name: survey_response, dtype: object
'''