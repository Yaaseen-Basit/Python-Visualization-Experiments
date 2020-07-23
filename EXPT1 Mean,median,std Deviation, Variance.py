# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 23:16:17 2019

@author: YB
"""

# Importing the statistics module 
import statistics 
from statistics import mean 

  
# list of positive integer numbers 
data1 = [1, 3, 4, 5, 7, 9, 2] 
  
x = statistics.mean(data1) 
  
# Printing the mean 
print("Mean is :", x) 
from fractions import Fraction as fr 
  
    
# tuple of a negative set of integers 
data2 = (-1, -2, -4, -7, -12, -19) 
  
# tuple of mixed range of numbers 
data3 = (-1, -13, -6, 4, 5, 19, 9) 
  
# tuple of a set of fractional numbers 
data4 = (fr(1, 2), fr(44, 12), fr(10, 3), fr(2, 3)) 
  
# dictionary of a set of values 
# Only the keys are taken in 
# consideration by mean() 
data5 = {1:"one", 2:"two", 3:"three"} 
  
  
# Printing the mean of above datsets 
print("Mean of data set 1 is % s" % (mean(data1))) 
print("Mean of data set 2 is % s" % (mean(data2))) 
print("Mean of data set 3 is % s" % (mean(data3))) 
print("Mean of data set 4 is % s" % (mean(data4))) 
print("Mean of data set 5 is % s" % (mean(data5))) 
from statistics import median 
  
# Importing fractions module as fr 
from fractions import Fraction as fr 
  
# tuple of positive integer numbers 
d1 = (2, 3, 4, 5, 7, 9, 11) 
  
# tuple of floating point values 
d2 = (2.4, 5.1, 6.7, 8.9) 
  
# tuple of fractional numbers 
d3 = (fr(1, 2), fr(44, 12), 
         fr(10, 3), fr(2, 3)) 
  
# tuple of a set of  negative integers 
d4 = (-5, -1, -12, -19, -3) 
  
# tuple of set of positive  
# and negative integers 
d5 = (-1, -2, -3, -4, 4, 3, 2, 1) 
  
# Printing the median of above datsets 
print("Median of data-set 1 is % s" % (median(d1))) 
print("Median of data-set 2 is % s" % (median(d2))) 
print("Median of data-set 3 is % s" % (median(d3))) 
print("Median of data-set 4 is % s" % (median(d4))) 
print("Median of data-set 5 is % s" % (median(d5))) 
import statistics 
  
# creating a simple data - set 
sample = [1, 2, 3, 4, 5] 
  
# Prints standard deviation 
# xbar is set to default value of 1 
print("Standard Deviation of sample is % s " 
                % (statistics.stdev(sample))) 

 
  
# variance is approximately the  
# squared result of what stdev is 
print("Variance of the sample is % s" 
     %(statistics.variance(sample))) 

#