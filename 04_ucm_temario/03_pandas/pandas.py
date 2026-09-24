import pandas as pd

orders_df = []  # DataFrame

category_groups = orders_df.groupby('category')

summary_df = category_groups.agg(
    order_count=('order_id', 'count'),
    user_count=('user_id', 'nunique'),
    revenue=('amount', 'sum'),
    avg_amount=('amount', 'mean')
)

summary_df = summary_df.reset_index()

summary_df

print('##############################################')

trips_df = []  # DataFrame

summary_df = trips_df.groupby('ride_type').agg(
    total_fare=('fare', 'sum'),
    mean_fare=('fare', 'mean'),
    total_trips=('trip_id', 'count')
).reset_index()

summary_df

print('##############################################')

orders_df['category'].value_counts()

"""
category       count
Fashion        390
Grocery        330
Electronics    180
Home & Gardem  5
"""

# Returns percentage.
orders_df['category'].value_counts(normalize=True)

# Order By min to max.
orders_df = orders_df.sort_values(by='revenue')

# Order By max to min.
orders_df = orders_df.sort_values(by='revenue', ascending=False)

print('##############################################')

summary_df = trips_df.groupby('ride_type').agg(
    unique_rider=('rider_id', 'nunique')
).reset_index()

summary_df = summary_df.sort_values(by='unique_rider')

summary_df

print('##############################################')

print('##############################################')

print('##############################################')

print('##############################################')

print('##############################################')

print('##############################################')

print('##############################################')

print('##############################################')

print('##############################################')

print('##############################################')
