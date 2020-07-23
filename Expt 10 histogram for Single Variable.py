# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:43:32 2019

@author: YB
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
pd.set_option('max_columns', None)
df = pd.read_csv("D:/fifa-18-demo-player-dataset/CompleteDataset.csv", index_col=0)

# To show Different Speciality Score of the players participating in the FIFA 2019

sns.set(style = 'dark', palette = 'colorblind', color_codes = True)
x = df.Special
plt.figure(figsize = (12, 8))
ax = sns.distplot(x, bins = 58, kde = False, color = 'm')
ax.set_xlabel(xlabel = 'Special score range', fontsize = 16)
ax.set_ylabel(ylabel = 'Count of the Players',fontsize = 16)
ax.set_title(label = 'Histogram for the Speciality Scores of the Players', fontsize = 20)
plt.show()
