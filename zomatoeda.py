# -*- coding: utf-8 -*-
"""ZomatoEDA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YrIzXdfGq5NStp1JSafZIKWtUlnPz9wG

###EDA And Feature Engineering(zomato data set)
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df=pd.read_csv('/zomato.csv', encoding='latin-1')

df.head()

df.columns

df.info()

df.describe()

"""##Data analysis
1.Missing value

2.Explore about numerical value

3.Explore about categorical value

4.Finding relationship between  features
"""

df.isnull().sum()

[features for features in df.columns if df[features].isnull().sum()>0]

sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')

df.shape

df_country=pd.read_excel('/Country-Code.xlsx')

df_country.head()

final_df=pd.merge(df,df_country,on='Country Code',how='left')

final_df.head()

final_df.Country.value_counts()# we will check how many records are there in each country

# we will save as index
final_df.Country.value_counts().index

country_name=final_df.value_counts().index

#we will creat numpy array
country_values=final_df.Country.value_counts().values

plt.pie(country_values[:3],labels=country_name[:3],autopct='%1.2f%%')

final_df.columns

final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size()

final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index()

ratings=final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0: 'Rating count'})

ratings

import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="Aggregate rating",y="Rating count",data=ratings)

sns.barplot(x="Aggregate rating",y="Rating count",hue='Rating color',data=ratings)

sns.barplot(x="Aggregate rating",y="Rating count",hue='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])

## Count plot
sns.countplot(x="Rating color",data=ratings,palette=['blue','red','orange','yellow','green','green'])

### Find the countries name that has given 0 rating
final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()

final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)

##find out which currency is used by which country?
final_df.columns

final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()

## Which Countries do have online deliveries option
final_df[final_df['Has Online delivery'] =="Yes"].Country.value_counts()

final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()

#Observations:
#Online Deliveries are available in India and UAE

final_df.columns

final_df.City.value_counts().index

city_values=final_df.City.value_counts().values

city_values

city_labels=final_df.City.value_counts().index

city_labels

plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')