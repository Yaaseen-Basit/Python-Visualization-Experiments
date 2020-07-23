# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:26:09 2019

@author: YB
"""



import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

train_df = pd.read_csv('Y:/EDA/train.csv')
test_df = pd.read_csv('Y:/EDA/test.csv')
titanic=pd.concat([train_df,test_df],axis=0,sort=False)
#we will combine both train and test data test to do eda.

titanic.head()

titanic.info()


labels={1:'First class',
       2:'Second class',
       3:'Third class'}
titanic['Pclass']=titanic['Pclass'].replace(labels)
titanic['Pclass'].value_counts()
pc=(titanic['Pclass'].value_counts()/titanic.shape[0])*100
pc.plot.bar(color='steelblue',figsize=(12,5))

#Most people were travelling in third class.

