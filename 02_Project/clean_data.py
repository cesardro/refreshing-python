"""
SELECT * FROM grocery_sales

         index  Store_ID       Date  Dept  Weekly_Sales
0            0         1 2010-02-05     1      24924.50
1            1         1 2010-02-05    26      11737.12
2            2         1 2010-02-05    17      13223.76
3            3         1 2010-02-05    45         37.44
4            4         1 2010-02-05    28       1085.29
...        ...       ...        ...   ...           ...
231517  232414        24 2011-05-06     8      49471.07
231518  232415        24 2011-05-06    50       1210.00
231519  232416        24 2011-05-06    87      25893.32
231520  232417        24 2011-05-06    85       1357.83
231521  232418        24 2011-05-06    35       3648.91

"""

import pandas as pd
import os

# Extract function is already implemented for you 
def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on = "index")
    return merged_df

# Call the extract() function and store it as the "merged_df" variable
merged_df = extract(grocery_sales, "extra_data.parquet")

# Create the transform() function with one parameter: "raw_data"
def transform(raw_data):
    raw_data = raw_data.fillna(0)
    raw_data["Date"] = pd.to_datetime(raw_data["Date"], errors='coerce')
    raw_data["Month"] = raw_data["Date"].dt.month
    raw_data = raw_data.loc[raw_data['Weekly_Sales'] > 10000, ["Store_ID","Month", "Dept","IsHoliday","Weekly_Sales","CPI","Unemployment"]]
    print(raw_data)
    return raw_data 
    pass

clean_data = transform(merged_df)

"""
        Store_ID  Month  Dept  ...  Weekly_Sales         CPI  Unemployment
0              1    2.0     1  ...      24924.50  211.096358         8.106
1              1    2.0    26  ...      11737.12  211.096358         8.106
2              1    2.0    17  ...      13223.76  211.096358         8.106
5              1    2.0    79  ...      46729.77  211.096358         0.000
6              1    2.0    55  ...      21249.31  211.096358         0.000
...          ...    ...   ...  ...           ...         ...           ...
231513        24    5.0    40  ...      45396.26  134.514367         8.212
231515        24    5.0    93  ...      41295.84  134.514367         8.212
231516        24    5.0     9  ...      24024.18  134.514367         8.212
231517        24    5.0     8  ...      49471.07  134.514367         8.212
231519        24    5.0    87  ...      25893.32  134.514367         8.212

[106193 rows x 7 columns]
"""

# Create the avg_weekly_sales_per_month function that takes in the cleaned data from the last step
def avg_weekly_sales_per_month(clean_data):
    clean_data = clean_data[["Month", "Weekly_Sales"]]

    clean_data = (
        clean_data
        .groupby("Month")
        .agg(Avg_Sales=("Weekly_Sales", "mean"))
        .reset_index()
        .round(2)
    )
    print(clean_data)
    return clean_data

agg_data = avg_weekly_sales_per_month(clean_data)

"""
    Month  Avg_Sales
0     1.0   33174.18
1     2.0   34342.44
2     3.0   33227.31
3     4.0   33414.78
4     5.0   33339.89
5     6.0   34582.47
6     7.0   33930.77
7     8.0   33644.79
8     9.0   33266.59
9    10.0   32736.99
10   11.0   36594.03
11   12.0   39248.98
"""

# Create the load() function that takes in the cleaned DataFrame and the aggregated one with the paths where they are going to be stored
def load(full_data, full_data_file_path, agg_data, agg_data_file_path):
    # Write your code here
    full_data.to_csv(full_data_file_path, index=False)
    agg_data.to_csv(agg_data_file_path, index=False)

# Call the load() function and pass the cleaned and aggregated DataFrames with their paths 
load(clean_data, "clean_data.csv", agg_data, "agg_data.csv")

# Create the validation() function with one parameter: file_path - to check whether the previous function was correctly executed
def validation(file_path):
    if not os.path.exists(file_path):
        raise Exception(f"There is no file at the path {file_path}")

# Call the validation() function and pass first, the cleaned DataFrame path, and then the aggregated DataFrame path
validation("clean_data.csv")
validation("agg_data.csv")