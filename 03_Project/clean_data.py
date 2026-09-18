# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the audible_raw.csv file
audible = pd.read_csv("03_Project/audible_raw.csv")
# View the first rows of the dataframe
audible

# Inspect the columns' data types 
audible.info()

# Remove Writtenby: from the author column
audible["author"] = audible["author"].str.replace('Writtenby:','')

# Remove Narratedby: from the narrator column
audible["narrator"] = audible["narrator"].str.replace('Narratedby:','')

# Check the results
audible

# Get a glimpse of the stars column
audible.stars.sample(n=10)

# Explore the values of the star column that are not 'Not rated yet'
audible[audible.stars != 'Not rated yet'].stars.sample(n=10)

# Replace 'Not rated yet' with NaN
audible.stars.replace('Not rated yet', np.nan, inplace=True)

# Extract number of stars into rating_stars and turn into float
audible['rating_stars'] = audible['stars'].str.extract('^([\d.]+)').astype(float)
# Replace the comma, extract number of ratings into n_ratings and turn into float
audible['n_ratings'] = audible['stars'].str.replace(',', '').str.extract('(\d+) ratings').astype(float)
# Examine the new rating_stars and n_ratings columns
audible[['rating_stars','n_ratings']]

# Drop the stars column
audible.drop(columns=['stars'], axis=1, inplace=True)
# Check the results
audible

# Explore the price column
audible.price.sample(n=10)

# Replace the comma with ''
audible['price'] = audible.price.str.replace(',', '')
# Replace 'Free' with 0
audible['price'] = audible.price.str.replace('Free', '0')
# Turn price to float
audible['price'] = audible.price.astype(float)

# Look at the unique values in the rating_stars column
audible.rating_stars.unique()

# Turn rating_stars to category
audible['rating_stars'] = audible.rating_stars.astype('category')

# Convert releasedate to datetime
audible['releasedate'] = pd.to_datetime(audible.releasedate)
# Inspect the dataframe 
audible.info()

# Explore the values in the time column
audible.time.sample(n=10)

# Search the entries in the time column for different spellings of min. Let' try min, mins, minutes
audible.time[audible.time.str.contains('min')].sample(n=10)

# Replace hrs, mins, and 'Less than 1 minute'
audible['time'] = audible.time.str.replace('hrs', 'hr')
audible['time'] = audible.time.str.replace('mins', 'min')
audible['time'] = audible.time.str.replace('Less than 1 minute', '1 min')

# Check the results
audible[['time']]

# Extract the number of hours, turn to integer
hours = audible['time'].str.extract('(\d+) hr').fillna(0).astype(int)
# Extract the number of minutes, turn to integer
mins = audible['time'].str.extract('(\d+) min').fillna(0).astype(int)
# Combine hours and minutes into the time_mins column
audible['time_mins'] = hours * 60 + mins
# Check the results
audible[['time_mins']]

# Drop the time column
audible.drop(columns=['time'], axis=1, inplace=True)

# Inspect the dataframe 
audible

# Plot histograms of all the numerical columns
audible.hist(figsize=(10,10), bins=100)
plt.show()

# Look at the numeric columns
audible.describe()

# Look at the non numeric columns
audible.describe(exclude=[np.number])

# Transform prices to USD (multiply times 0.012)
audible['price'] = audible.price * 0.012
# Check the results
audible.price.describe()

# Inspect the language column before making changes
audible.language.unique()

# Update capitalization in the language column
audible['language'] = audible.language.str.capitalize()
# Check the results
audible.language.unique()

# Look for duplicate rows
audible.duplicated().sum()

# Create a list of our subset columns and assign to subset_cols
subset_cols = ['name', 'author' , 'narrator' , 'time_mins', 'price']
# Check for duplicates using our subset of columns
audible.duplicated(subset=subset_cols).sum()

# Check the duplicated rows keeping the duplicates and order by the name column
audible[audible.duplicated(subset=subset_cols, keep=False)].sort_values(by='name')

# Drop duplicated rows keeping the last release date
audible.drop_duplicates(subset=subset_cols,keep='last',inplace=True)

# Check again for duplicates using our subset of columns
audible.duplicated(subset=subset_cols).sum()

# Check for null values
audible.isna().sum()

# Save the dataframe to a new file: 'audible_clean.csv'
audible.to_csv('03_Project/audible_clean.csv', index=False)