import pandas as pd
import numpy as np

client = pd.read_csv('bank_marketing.csv')
campaign = pd.read_csv('bank_marketing.csv')
economics = pd.read_csv('bank_marketing.csv')

client['job'] = client['job'].str.replace(".", "_")

client['education'] = client['education'].str.replace(".", "_")
client['education'] = client['education'].replace('unknown', np.nan)

client['credit_default'] = client['credit_default'].map({'yes': 1, 'no': 0, 'unknown': 0})
client['credit_default'] = client['credit_default'].astype('boolean')

client['mortgage'] = client['mortgage'].map({'yes': 1, 'no': 0, 'unknown': 0})
client['mortgage'] = client['mortgage'].astype('boolean')

final_client = client[['client_id','age','job', 'marital', 'education', 'credit_default', 'mortgage']]
final_client.to_csv('client.csv', index=False)

campaign['previous_outcome'] = campaign['previous_outcome'].map({'success': 1, 'failure': 0, 'nonexistent': 0})
campaign['previous_outcome'] = campaign['previous_outcome'].astype('boolean')

campaign['campaign_outcome'] = campaign['campaign_outcome'].map({'yes': 1, 'no': 0})
campaign['campaign_outcome'] = campaign['campaign_outcome'].astype('boolean')

campaign['year'] = 2022

month_map = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12
}

campaign['month'] = campaign['month'].map(month_map)

campaign['last_contact_date'] = pd.to_datetime({'year': campaign['year'], 'month': campaign['month'],'day': campaign['day']})

final_campaign = campaign[['client_id','number_contacts','contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome', 'last_contact_date']]
final_campaign.to_csv('campaign.csv', index=False)

final_economics = economics[['client_id', 'cons_price_idx', 'euribor_three_months']]
final_economics.to_csv('economics.csv', index=False)