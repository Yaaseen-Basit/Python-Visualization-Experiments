# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:43:17 2019

@author: YB
"""


# stats.zscore() method   
import numpy as np 
from scipy import stats 
    
arr1 = [[20, 2, 7, 1, 34], 
        [50, 12, 12, 34, 4]] 
  
arr2 = [[50, 12, 12, 34, 4],  
        [12, 11, 10, 34, 21]] 
  
print ("\narr1 : ", arr1) 
print ("\narr2 : ", arr2) 
  
print ("\nZ-score for arr1 : \n", stats.zscore(arr1)) 
print ("\nZ-score for arr1 : \n", stats.zscore(arr1, axis = 1)) 
#Computing along a specified axis, using n-1 degrees of freedom (ddof=1) to calculate the standard deviation:


b = np.array([[ 0.3148,  0.0478,  0.6243,  0.4608],
              [ 0.7149,  0.0775,  0.6072,  0.9656],
              [ 0.6341,  0.1403,  0.9759,  0.4064],
              [ 0.5918,  0.6948,  0.904 ,  0.3721],
              [ 0.0921,  0.2481,  0.1188,  0.1366]])
stats.zscore(b, axis=1, ddof=1)


