# -*- coding: utf-8 -*-
"""Depression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IGn1NnwXmv_7zmRxRWAoqRSZrV0BBnjk

1. Import all the libraries for predictive modelling
"""

import numpy as np #create arrays
import pandas.util.testing as tm
import pandas as pd
import matplotlib.pyplot as plt #plot data
import seaborn as sns #plot data
import missingno as ms #plot missing data

"""2. Data Cleaning"""

url='https://raw.githubusercontent.com/hiyabose/Depression/master/depressiondataset.csv'
df = pd.read_csv(url)

df.head()

df.info()

"""We can see there are 1429 rows of data and there are a few missing values in 'no_lasting_investment' columns."""

ms.matrix(df)

sum(df['no_lasting_investmen'].isna())

"""So, we can see that there are 20 missing values. I will fix it"""

df1=df.interpolate(method ='linear', limit_direction ='forward') 
sum(df1['no_lasting_investmen'].isna())

"""Thus we can see that our new dataset do not contain any missing values."""

df1.info()

df1.max()

df1.describe()

"""From this we can tell that mid aged people have depressions, more than children or old people"""

df1.shape

sns.swarmplot(y="Age", x="depressed", data=df1)
plt.show()



"""Here also we can see that the majority are depressed in their mid life."""

from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

train = df1.drop(['Survey_id','Ville_id'], axis=1)
train= np.asarray(train, dtype='float64')
test = df1['depressed']
test= np.asarray(test, dtype='float64')

X_train, X_test, y_train, y_test = train_test_split(train,test, test_size=0.3, random_state=2)

reg = LogisticRegression()

reg.fit(X_train, y_train)

pred = reg.predict_proba(X_test)

pred

n =[[1,23,1,3,8,5,28912201,22861940,23399979,26692283,28203066,0,0,0,0,30028818,31363432,0,28411718,28292707,4]]

o = reg.predict_proba(n)

print (o)

pred.shape

reg.score(X_test, y_test)

X_test.shape

"""Accuracy rate 82.5% we can say :)"""

import pickle

pickle.dump(reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))