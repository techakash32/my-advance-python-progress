import pandas as pd
import numpy as np

df = pd.read_csv('Heart_Disease_Prediction.csv')
print(df.head(5))
print(df.tail(5))
print("=====================================================")
print(df.sample())
print(df['Age'])
print("=====================================================")
print(df['Age'].astype('float'))
print(df['Age'].dtype)
print("=====================================================")
df['Age_int'] = df['Age'].astype('int')
print(df.head())
# print((df['Number of vessels fluro'==0]).count)
cat_col=df.select_dtypes(include='object').columns
num_cols=df.select_dtypes(exclude='object').columns
print(num_cols)