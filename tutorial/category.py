import pandas as pd
import numpy as np

df = pd.read_csv('kickstarter/ks-projects-201801.csv', nrows = 30000)

df = df.drop(columns = ['ID', 'name', 'deadline', 'goal', 'launched', 'pledged', 'backers', 'usd pledged', 'usd_pledged_real'])

success_rate = round(df['state'].value_counts() / len(df['state']), 2)
print(success_rate)

category = df['main_category'].value_counts()
category_success = df[df['state'] == 'successful']['main_category'].value_counts()

category_success_rate = round(category_success / category, 2).sort_values(ascending = False)
print(category_success_rate)

print(df.groupby('main_category').sum())

print(df['currency'].value_counts())

def others(currency):
    return np.where((currency == 'MXN') | (currency == 'SEK') | (currency == 'NZD') | (currency == 'DKK') |
                   (currency == 'NOK') | (currency == 'HKD') | (currency == 'CHF') | (currency == 'SGD') | (currency == 'JPY'), 'Others', currency)

df['currency'] = others(df['currency'])
print(df['currency'].value_counts())

from sklearn.preprocessing import LabelEncoder

cat_features = ['category', 'main_category', 'currency', 'state', 'country']

for col in cat_features:
    lbl = LabelEncoder()
    df[col] = lbl.fit_transform(df[col].values)

print(df.head())
