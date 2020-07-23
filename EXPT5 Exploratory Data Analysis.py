# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 18:15:34 2019

@author: YB
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
iris=pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
print(iris.shape)
print(iris.describe)
print(iris.columns)
print(iris["species"].value_counts())
print(iris.isnull())
X = iris.iloc[:, :].values

from sklearn.preprocessing import LabelEncoder
labelencoder_X=LabelEncoder()

X[:,4]=labelencoder_X.fit_transform(X[:,4])
Y=pd.DataFrame(X)
iris_group=iris.groupby(iris['species'])
print(iris_group.mean())
# Identifiy missing values
iris.isnull()
