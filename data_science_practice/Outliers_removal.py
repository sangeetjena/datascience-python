import pandas as pd
import numpy as np

df  = pd.read_csv("D:/Learning/DataScience/SampleData/datasets_11167_15520_test.csv")
df.describe()
df.columns
"axis indicate rows or columns 1 means columns and o means rows"
df = df.drop("id",axis=0)
df = df.rename(columns={'n_cores': 'number_of_core'})
dup = df.duplicated()
dup.head()
dup.sum()
dup.drop_duplicates()
df('battery_power').fillna(0)
"find all null values in the dada set"
df.isnull().sum()
"fill all null fields with the back fill values "
df['battery_power'] = df['battery_power'].drop_duplicates()
df['battery_power'].duplicated()
df['battery_power'] = df['battery_power'].fillna(df['battery_power'].min())
df['battery_power'].fillna(method='bfill')
