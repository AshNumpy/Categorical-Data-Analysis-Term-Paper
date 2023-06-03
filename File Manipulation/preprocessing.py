import pandas as pd 
import numpy as np 

df = pd.read_csv('../Datasets/Ders Sonu Anketi.csv')

# write columns to text file
with open('../Datasets/questions.txt', 'w') as f:
    for col in df.columns:
        f.write(col + '\n')
    f.close()

df.columns = ['DateTime', 'Sex', 'Department', 
            'likert_1', 'likert_2', 'likert_3', 'likert_4', 'likert_5', 'likert_6', 'likert_7',
            'soru8', 'soru9', 'soru10', 'soru11', 'soru12', 'soru13']

import re
# Regex ile tarih kısmını ayıklama
pattern = r'(\d{4}/\d{2}/\d{2})'

df['Date'] = df['DateTime'].str.extract(pattern)

df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')
df.iloc[0,4]

for i in range(1, 8):
    df.loc[df[f'likert_{i}'] == '5 (Kesinlikle Katılıyorum)', f'likert_{i}'] = 5
    df.loc[df[f'likert_{i}'] == '1 (Kesinlikle Katılmıyorum)', f'likert_{i}'] = 1

df.drop(['DateTime'], axis=1, inplace=True)

df['soru8'].value_counts()
df['soru9'].value_counts()
df['soru10'].value_counts()
df = df[['Date', 'Sex', 'Department', 'likert_1', 'likert_2', 'likert_3', 'likert_4',
       'likert_5', 'likert_6', 'likert_7', 'soru8', 'soru9', 'soru10',
       'soru11', 'soru12', 'soru13']]

df.to_csv('../Datasets/processed.csv', index=False)