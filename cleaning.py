'''
Importing Libraries
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from sklearn.preprocessing import StandardScaler
#from sklearn.model_selection import train_test_split
#%matplotlib inline


'''
Data Loading
'''
df = pd.read_csv('DataScience.csv')

'''
Preprocessing
'''
print(df.shape)
print(df.head(3))
print(df.columns)
print(df.info())
print(df.isnull().sum())
df.dropna(inplace=True)

#plt.figure(figsize=(6,6))
#sns.heatmap(df.corr(), annot=True, fmt='.0%')


#Salary Parsing
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
new_salary = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['min_salary'] = new_salary.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = new_salary.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary) / 2

#Company name
df['Company text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1)

#States
df['state'] = df['Location'].apply(lambda x: x.split(',')[1])
print(df.state.value_counts())

#Age of the company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2023 - x)

#Job Description
#Python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#SQL
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
print('SQL',df.sql.value_counts())

#Spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
print('Spark',df.spark.value_counts())

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
print('aws',df.aws.value_counts())

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
print('excel',df.excel.value_counts())

#tableau
df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
print('tableau',df.tableau.value_counts())


df_output = df.drop(['Unnamed: 0','Easy Apply'], axis=1)
print(df_output.columns)
df_output.to_csv('Salary_cleaned.csv', index=False)