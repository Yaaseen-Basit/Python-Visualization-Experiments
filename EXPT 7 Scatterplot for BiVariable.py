# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:24:19 2019

@author: Yaaseen
"""

import pandas as pd
pd.set_option('max_columns', None)
df = pd.read_csv("D:/fifa-18-demo-player-dataset/CompleteDataset.csv", index_col=0)

import re
import numpy as np

footballers = df.copy()
footballers['Unit'] = df['Value'].str[-1]
footballers['Value (M)'] = np.where(footballers['Unit'] == '0', 0, 
                                    footballers['Value'].str[1:-1].replace(r'[a-zA-Z]',''))
footballers['Value (M)'] = footballers['Value (M)'].astype(float)
footballers['Value (M)'] = np.where(footballers['Unit'] == 'M', 
                                    footballers['Value (M)'], 
                                    footballers['Value (M)']/1000)
footballers = footballers.assign(Value=footballers['Value (M)'],
                                 Position=footballers['Preferred Positions'].str.split().str[0])
footballers.head()
import seaborn as sns
#scatter plot

#This scatterplot uses three visual variables. The horizontal position (x-value) tracks the Value of the player (how well they are paid). The vertical position (y-value) tracks the Overall score of the player across all attributes. And the color (the hue parameter) tracks which of the three categories of interest the player the point represents is in.
sns.lmplot(x='Value', y='Overall', hue='Position', 
           data=footballers.loc[footballers['Position'].isin(['ST', 'RW', 'LW'])], 
           fit_reg=False)

