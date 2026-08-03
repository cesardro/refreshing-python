# Numeric Data

# ride_sharing is a DataFrame from Pandas CSV.
import recordlinkage
from thefuzz import process
import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import datetime as dt
import pandas as pd
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
assert ride_sharing['user_type_cat'].dtype == 'category'

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
print(ride_sharing[['duration', 'duration_trim', 'duration_time']])
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
print(ride_sharing['duration_time'].mean())  # 11.389052795031056

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


# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())  # 2026-07-30

# Duplicates.
# .duplicated() ->
# subset: List of column names to check for duplication.
# keep: Whether to keep first ('first'), last('last') or all(False) duplicated values.

# Find duplicates
duplicates = ride_sharing.duplicated('ride_id', False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id', 'duration', 'user_birth_year']])

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
duplicates = ride_unique.duplicated(subset='ride_id', keep=False)
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
airlines['dest_region'] = airlines['dest_region'].replace({'eur': 'europe'})

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

# Create ranges -> 0 -------- 60 -------- 180 -------- ∞
label_ranges = [0, 60, 180, np.inf]
# Create intervals.
label_names = ['short', 'medium', 'long']

# Create wait_type column
# .cut() converts continue numeric values into categories based on intervals.
# airlines['wait_min'] -> 45, bins -> range 0-60-180+, labels -> name of catergory
airlines['wait_type'] = pd.cut(
    airlines['wait_min'], bins=label_ranges, labels=label_names)

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
airlines['full_name'] = airlines['full_name'].str.replace("Dr.", "")

# Replace "Mr." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Mr.", "")

# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss", "")

# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.", "")

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

# Uniformity.

banking = ()

# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
# .loc[row, col] -> Loc can be read and/or writte, in this example we are looking in banking for rows
# that are in euro (acct_eu) and column 'acct_amount' and multiplying the values by 1.1.
# Then we are assigning the new values to the same rows and column in banking.
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

# Unify acct_cur column by changing 'euro' values to 'dollar'
# In this example we are looking in banking for rows that are in euro (acct_eu) and column 'acct_cur', and then assining the value 'dollar'.
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'

# Print the header of account_opend
print(banking['account_opened'].head())
'''
0          2018-03-05
1            21-01-18
2    January 26, 2018
3            21-14-17
4            05-06-17
Name: account_opened, dtype: object
'''

# Convert account_opened to datetime
# to_datetime() -> Converts arguments to datetime. For errors handling we have:
# errors = 'raise' -> Raises an exception, program stops.
# errors = 'coerce' -> Returns missing value for error. -> NaT.
# errors = 'ignore' -> Does not convert anything and leave strings as is.
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Return missing value for error
                                           errors='coerce')

# Get year of account opened
# strftime() -> Means "String Format Time". It is used to convert datetime object to string.
# In this case it transforms to a string with the year only due to the format '%Y'.
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print acct_year
print(banking['acct_year'])
'''
0    2018
1     NaN
2     NaN
3     NaN
4     NaN
Name: acct_year, dtype: object
'''

# Cross field validation.

# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where fund_columns row sum == inv_amount
# Axis = 1 -> Sum across columns.
# Axis = 0 -> Sum across rows.
inv_equ = banking[fund_columns].sum(axis=1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])
# Number of inconsistent investments:  8

# Store today's date and find ages
today = dt.date.today()

# Calculate ages_manual by subtracting birth year from current year.
ages_manual = today.year - banking['birth_date'].dt.year

# Find rows where age column == ages_manual, which it means that the ages are consistent.
age_equ = ages_manual == banking['age']

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])
# Number of inconsistent ages:  4

# Completeness.

# Missing Completely at Random: No systematic relationship between a column's missing values and other or own values.
# Missing at Random: There is a systematic relationship between a column's missing values and other observed values.
# Missing not at Random: There is a systematic relationship between a column's missing values and unobserved values.


# Print number of missing values in banking
# isna() -> Detect missing values.
# Using isna along with sum will give you the total number of missing values in each column.
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
# In this example banking is being anidaly index. First we say "get inv_amount column from banking and check if it is missing with isna()".
# Then we use the return boolean (True or False) to return the all rows of banking where inv_amount is missing.
# The same logic is applied to the second line, but with the negation operator ~, which means "not".
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

# Sort banking by age and visualize
banking_sorted = banking.sort_values(by='age')
msno.matrix(banking_sorted)
plt.show()

# Mising.

# Drop missing values of cust_id by using subset (only drop rows where cust_id is null)
# You need to assign the result to a new object, otherwise the original DataFrame will remain unchanged.
banking_fullid = banking.dropna(subset=['cust_id'])

# Compute estimated acct_amount using the correct DataFrame
acct_imp = banking_fullid['inv_amount'] * 5

# Ensure you're imputing the correct column
banking_imputed = banking_fullid.fillna({'acct_amount': acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())

# Fuzz

# Import process from thefuzz

restaurants = pd.DataFrame({'cuisine_type': [
                           'asian', 'american', 'italian', 'mexican', 'indian', 'aisan', 'amrican', 'italian', 'mesican', 'indain']})

# Store the unique values of cuisine_type in unique_types
unique_types = restaurants['cuisine_type'].unique()

# Calculate similarity of 'asian' to all values of unique_types
# process.extract() -> Returns a list of tuples with the matched strings, from highest to lowest.
# 1st argument -> The strinng to look for.
# 2nd argument -> The list of strings to look in.
# 3rd argument -> The number of matches to return. In this case we are returning all the matches by using the length of unique_types.
print(process.extract('asian', unique_types, limit=len(unique_types)))

# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit=len(unique_types)))

# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit=len(unique_types)))

'''
[('asian', 100), ('asiane', 91), ('asiann', 91), ('asiian', 91), ('asiaan', 91), ('asianne', 83), ('asiat', 80), ('italiann', 72), ('italiano', 72), ('italianne', 72), ('italiaan', 68), ('italiian', 68), ('itallian', 68), ('italian', 67), ('amurican', 62), ('american', 62), ('ameerican', 60), ('aamerican', 60), ('ameriican', 60), ('amerrican', 60), ('ameerrican', 60), ('ammereican', 60), ('americann', 57), ('americano', 57), ('ammericann', 54), ('americin', 51), ('amerycan', 51), ('america', 50), ('merican', 50), ('murican', 50), ('italien', 50), ('americen', 46), ('itali', 40)]
[('american', 100), ('americann', 94), ('americano', 94), ('ameerican', 94), ('aamerican', 94), ('ameriican', 94), ('amerrican', 94), ('america', 93), ('merican', 93), ('ammericann', 89), ('ameerrican', 89), ('ammereican', 89), ('amurican', 88), ('americen', 88), ('americin', 88), ('amerycan', 88), ('murican', 80), ('asian', 62), ('asiane', 57), ('asiann', 57), ('asiian', 57), ('asiaan', 57), ('italian', 53), ('asianne', 53), ('italiann', 50), ('italiano', 50), ('italiaan', 50), ('italiian', 50), ('itallian', 50), ('italianne', 47), ('asiat', 46), ('itali', 40), ('italien', 40)]
[('italian', 100), ('italiann', 93), ('italiano', 93), ('italiaan', 93), ('italiian', 93), ('itallian', 93), ('italianne', 88), ('italien', 86), ('itali', 83), ('asian', 67), ('asiane', 62), ('asiann', 62), ('asiian', 62), ('asiaan', 62), ('asianne', 57), ('amurican', 53), ('american', 53), ('americann', 50), ('asiat', 50), ('americano', 50), ('ameerican', 50), ('aamerican', 50), ('ameriican', 50), ('amerrican', 50), ('ammericann', 47), ('ameerrican', 47), ('ammereican', 47), ('america', 43), ('merican', 43), ('murican', 43), ('americen', 40), ('americin', 40), ('amerycan', 40)]
'''

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract(
    'italian', restaurants['cuisine_type'], limit=len(restaurants.cuisine_type))

# Iterate through the list of matches to italian
for match in matches:
    # Check whether the similarity score is greater than or equal to 80
    if match[1] >= 80:
        # Select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
        restaurants.loc[restaurants['cuisine_type']
                        == match[0], 'cuisine_type'] = 'italian'

# Pairs


restaurants_new = ()

# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types
# Here you are only creating the rule to compare the two DataFrames, it will be city vs city. Its not execute till .compute() is called.
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('cuisine_type', 'cuisine_type', label='cuisine_type')

# Find similar matches of rest_name
comp_cl.string('rest_name', 'rest_name', label='name', threshold=0.8)

# Get potential matches and print
# pairs is a pandas MultiIndex object that tells you which rows are potential matches.
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)

'''
            city  cuisine_type  name
    0   0      0             1   0.0
        1      0             1   0.0
        7      0             1   0.0
        12     0             1   0.0
        13     0             1   0.0
    ...      ...           ...   ...
    334 79     0             1   0.0
    335 26     0             1   0.0
        65     0             1   0.0
        71     0             1   0.0
        79     0             1   0.0
'''

# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis=1) >= 3]

# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

# Concatenate restaurants and non_dup
full_restaurants = pd.concat([restaurants, non_dup])
print(full_restaurants)

'''
                        rest_name                  rest_addr               city       phone cuisine_type
    0   arnie morton's of chicago   435 s. la cienega blv .         los angeles  3102461501     american
    1          art's delicatessen       12224 ventura blvd.         studio city  8187621221     american
    2                   campanile       624 s. la brea ave.         los angeles  2139381447     american
    3                       fenix    8358 sunset blvd. west           hollywood  2138486677     american
    4          grill on the alley           9560 dayton way         los angeles  3102760615     american
    ..                        ...                        ...                ...         ...          ...
    76                        don        1136 westwood blvd.           westwood  3102091422      italian
    77                      feast        1949 westwood blvd.            west la  3104750400      chinese
    78                   mulberry        17040 ventura blvd.             encino  8189068881        pizza
    80                    jiraffe      502 santa monica blvd       santa monica  3109176671  californian
    81                   martha's  22nd street grill 25 22nd  st. hermosa beach  3103767786     american
'''
