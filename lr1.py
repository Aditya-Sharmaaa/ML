# -*- coding: utf-8 -*-
"""LR1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1exjZM6B-I5DYqquEPQW2GJ1MZsTRgRqF
"""

import seaborn as sns
import pandas as pd
import numpy as np

df=sns.load_dataset('iris')
df.head()

df['species'].unique()

df.isnull().sum()

df=df[df['species']!='setosa']
df.head()

df['species'].unique()

df['species']=df['species'].map({'versicolor':0,'virginica':1})

df.head()

X=df.iloc[:,:-1]
y=df.iloc[:,-1]

X

y

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
     X, y, test_size=0.25, random_state=42)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()

from sklearn.model_selection import GridSearchCV
Parameter={'penalty':['l2'],'C':[1,2,3,4,5,6,7,8],'max_iter':[100,200,300]}

classifier_regression=GridSearchCV(classifier,param_grid=Parameter,scoring='accuracy',cv=5)

classifier_regression.fit(X_train,y_train)

print(classifier_regression.best_score_)

print(classifier_regression.best_params_)