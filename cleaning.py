'''
Importing Libraries
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


#Salary Parsing
df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
new_salary = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['min_salary'] = new_salary.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = new_salary.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary+df.max_salary) / 2

#Company name
df['Company text'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis=1)
df['Company text'] = df['Company text'].apply(lambda x: x.replace('\n',('')))

#States
df['state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.state = df.state.apply(lambda x: x.strip() if x.strip().lower() != 'arapahoe' else 'CO')
df.state.value_counts()

#Age of the company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2023 - x)

#Job Description
#Python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#SQL
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)

#Spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
print('Spark',df.spark.value_counts())

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

#tableau
df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
print('tableau',df.tableau.value_counts())

def job_title(title):
  if 'data scientist' in title.lower():
    return 'data scientist'
  elif 'data engineer' in title.lower():
    return 'data engineer'
  elif 'analyst' in title.lower():
    return 'analyst'
  elif 'machine learning' in title.lower():
    return 'machine learning'
  elif 'manager' in title.lower():
    return 'manager'
  elif 'director' in title.lower():
    return 'director'
  else:
    return 'na'

def seniority(title):
  if 'sr' in title.lower() or 'sr.' in title.lower() or 'senior' in title.lower() or 'lead' in title.lower() or 'principle' in title.lower():
    return 'senior'
  elif 'jr' in title.lower() or 'junior' in title.lower() or 'jr.' in title.lower():
    return 'junior'
  else:
    return 'na'

#Job seniority and title
df['job_simplified'] = df['Job Title'].apply(job_title)
df['seniority'] = df['Job Title'].apply(seniority)

#Job description length
df['description length'] = df['Job Description'].apply(lambda x: len(x))

#number of competitors
df['number_competitors'] = df['Competitors'].apply(lambda x: len(x.split()) if x != '-1' else 0)

df_output = df.drop(['Unnamed: 0','Easy Apply'], axis=1)
print(df_output.columns)
df_output.to_csv('Salary_cleaned.csv', index=False)