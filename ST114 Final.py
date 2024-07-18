# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:34:22 2023

@author: tanmay
"""

import matplotlib.pyplot as plt
import numpy as np
from statistics import mean

#Plotting out all Data Points and Regression Line

with open('C:/Timeinpk.txt', 'r') as f:
    lines = f.read().splitlines()


with open('C:/comppercent.txt', 'r') as f:
    line1 = f.read().splitlines()


lines.sort()
line1.sort()

x = np.asarray(lines)
y = np.asarray(line1)

x = x.astype(float)
y = y.astype(float)

a, b= np.polyfit(x,y, 1)
plt.scatter(x,y)
plt.xlabel("Time in Pocket in Seconds")
plt.ylabel("Completion Percentage")
plt.title("Correlation between Time in pocket and completion percentage of NFL Quarterbacks")
plt.plot(x, a*x+b, 'r')


#Getting Appropriate Summary Statistics
def get_means(input_file_name):
    #Can get the mean for either one of the two data files based on the input.
    
    if input_file_name == 'Timeinpk.txt':
        with open('C:/Timeinpk.txt', 'r') as f:
            list1 = f.read().splitlines()
        list1.sort()
        h = np.asarray(list1)
        h = h.astype(float)
        mean1  = sum(h)/len(h)
        
    elif input_file_name == 'comppercent.txt':
        with open('C:/comppercent.txt', 'r') as f:
            list2 = f.read().splitlines()
            list2.sort()
            h2 = np.asarray(list2)
            h2= h2.astype(float)
            mean1 = sum(h2)/len(h2)
    
    return str(mean1)

def sample_size(input_file_name):
    if input_file_name == 'Timeinpk.txt':
        with open('C:/Timeinpk.txt', 'r') as f:
            list1 = f.read().splitlines()
        size1  = len(list1)
        
    elif input_file_name == 'comppercent.txt':
        with open('C:/comppercent.txt', 'r') as f:
            list2 = f.read().splitlines()
        size1 = len(list2)
    
    return str(size1)

def maximum(input_file_name):
    if input_file_name == 'Timeinpk.txt':
        with open('C:/Timeinpk.txt', 'r') as f:
            list1 = f.read().splitlines()
        maximum = max(list1)
        
    elif input_file_name == 'comppercent.txt':
        with open('C:/comppercent.txt', 'r') as f:
            list2 = f.read().splitlines()
        maximum = max(list2)
    
    return str(maximum)

def minimum(input_file_name):
    if input_file_name == 'Timeinpk.txt':
        with open('C:/Timeinpk.txt', 'r') as f:
            list1 = f.read().splitlines()
        minimum = min(list1)
        
    elif input_file_name == 'comppercent.txt':
        with open('C:/comppercent.txt', 'r') as f:
            list2 = f.read().splitlines()
        minimum = min(list2)
    
    return str(minimum)

def best_fit_slope(x,y):
    m = (((mean(x)* mean(y))-mean(x*y))/
         ((mean(x)**2) - mean(x**2)))
    return str(m)

def rsquared():
    corr_matrix = np.corrcoef(x, y)
    corr = corr_matrix[0,1]
    r_squared = corr**2
    return str(r_squared)

#Printing all of the functions and summary statistics
print("Summary Statistics:\n")
print("Mean time in the pocket: " + get_means('Timeinpk.txt') + " seconds")
print("Mean completion percentage: " + get_means('comppercent.txt'))
print("Sample size for time in pocket data: " + sample_size('Timeinpk.txt'))
print("Sample size for completion percentage data: " + sample_size('comppercent.txt'))
print("Maximum time in pocket: " + maximum('Timeinpk.txt') + " seconds")
print("Maximum completion percentage: " + maximum('comppercent.txt'))
print("Minimum time in pocket: " + minimum('Timeinpk.txt') + " seconds")
print("Minimum completion percentage: " + minimum('comppercent.txt'))
print("Slope of the regression line: " + best_fit_slope(x,y))
print("The R-squared value of the datasets: " + rsquared())

    
    
    