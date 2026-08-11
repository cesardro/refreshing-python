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

# Spreadsheets.

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel('fcc_survey.xlsx')

# View the head of the dataframe
print(survey_responses.head())

'''
        Age  AttendedBootcamp  BootcampFinish  BootcampLoanYesNo BootcampName  ...  ResourceUdemy  ResourceW3Schools                             SchoolDegree              SchoolMajor  StudentDebtOwe
    0  28.0               0.0             NaN                NaN          NaN  ...            NaN                NaN           some college credit, no degree                      NaN           20000
    1  22.0               0.0             NaN                NaN          NaN  ...            1.0                NaN           some college credit, no degree                      NaN             NaN
    2  19.0               0.0             NaN                NaN          NaN  ...            NaN                NaN  high school diploma or equivalent (GED)                      NaN             NaN
    3  26.0               0.0             NaN                NaN          NaN  ...            NaN                NaN                        bachelor's degree  Cinematography And Film            7000
    4  20.0               0.0             NaN                NaN          NaN  ...            NaN                NaN           some college credit, no degree                      NaN             NaN
'''

# Create string of lettered columns to load
col_string = "AD, AW:BA"

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("fcc_survey_headers.xlsx",
                                 usecols=col_string,
                                 skiprows=2)

# View the names of the columns selected
print(survey_responses.columns)

'''
Index(['ExpectedEarning', 'JobApplyWhen', 'JobPref', 'JobRelocateYesNo', 'JobRoleInterest', 'JobWherePref'], dtype='object')
'''
responses = pd.DataFrame()  # Dummy

# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
# .values() -> Returns all values in dictionary.
# .keys() -> Returns all keys in dictionary.
for df in responses.values():
    # Print the number of rows being added
    print("Adding {} rows".format(df.shape[0]))
    # Concatenate all_responses and df, assign result
    all_responses = pd.concat([all_responses, df])

# Booleans

# Load the data
survey_data = pd.read_excel("fcc_survey_subset.xlsx")

# Count NA values in each column
print(survey_data.isna().sum())

'''
ID.x                        0
HasDebt                     0
HasFinancialDependents      7
HasHomeMortgage           499
HasStudentDebt            502
'''

# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype={'HasDebt': bool})

# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())

'''
HasDebt   HasFinancialDependents  HasHomeMortgage  HasStudentDebt                                       
False                     112.0              0.0             0.0
True                      205.0            151.0           281.0
'''
# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel("fcc_survey_yn_data.xlsx",
                              dtype={"HasDebt": bool,
                                     "AttendedBootCampYesNo": bool},
                              true_values=['Yes'],
                              false_values=['No'])

# View the data
print(survey_subset.head())

'''
                                ID.x  AttendedBootCampYesNo  HasDebt  HasFinancialDependents  HasHomeMortgage  HasStudentDebt
0  cef35615d61b202f1dc794ef2746df14                  False     True                     1.0              0.0             1.0
1  323e5a113644d18185c743c241407754                  False    False                     0.0              NaN             NaN
2  b29a1027e5cd062e654a63764157461d                  False    False                     0.0              NaN             NaN
3  04a11e4bcb573a1261eb0d9948d32637                  False     True                     0.0              0.0             1.0
4  9368291c93d5d5f5c8cdb1a575e18bec                  False     True                     0.0              0.0             0.0
'''

# Datetime

# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx",
                            parse_dates=['Part1StartTime'])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())

'''
0   2016-03-29 21:23:13
1   2016-03-29 21:24:59
2   2016-03-29 21:25:37
3   2016-03-29 21:21:37
4   2016-03-29 21:26:22
Name: Part1StartTime, dtype: datetime64[ns]
'''

# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ["Part2StartDate", "Part2StartTime"]}


# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates=datetime_cols)

# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())

'''
count                    1000
unique                    985
top       2016-03-30 07:27:25
freq                        2
first     2016-03-29 21:24:57
last      2016-03-30 09:08:18
Name: Part2Start, dtype: object
'''

# Formatting

'''
Datetime Formatting

Code   Meaning               Example
%Y     Year (4-digit)        1999
%m     Month (zero-padded)   03
%d     Day (zero-padded)     01
%H     Hour (24-hour clock)  21
%M     Minute (zero-padded)  09
%      SSecond (zero-padded) 05

format_string = "%m%d%Y %H:%M:%S"
survey_df["Part2EndTime"] = pd.to_datetime(survey_df["Part2EndTime"],format=format_string)
'''

# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"],
                                   format = "%m%d%Y %H:%M:%S")

print(survey_data.Part2EndTime.head())

# Before: 

'''
0      03292016 21:27:25
1      03292016 21:29:10
2      03292016 21:28:21
3      03292016 21:30:51
4      03292016 21:31:54
             ...        
995    03302016 09:04:49
996    03302016 09:05:06
997    03302016 09:06:21
998    03302016 09:08:29
999    03302016 09:09:58
'''

# After, print:

'''
0   2016-03-29 21:27:25
1   2016-03-29 21:29:10
2   2016-03-29 21:28:21
3   2016-03-29 21:30:51
4   2016-03-29 21:31:54
'''