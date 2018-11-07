# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 22:04:58 2018

@author: Huiting
"""
# =============================================================================
# This project is for studying the relationship of College Majors and the earnings
# It is going to use Pandas,Numpy and Matplotlib.pyplot 
# It will answer the following questions:
#   Do students in more popular majors make more money?
#       Using scatter plots
#   How many majors are predominantly male? Predominantly female?
#      Using histograms
#   Which category of majors have the most students?
#      Using bar plots

# =============================================================================
import pandas as pd
import matplotlib.pyplot as plt
import pandas.plotting as pplt
import numpy as np

# import file
recent_grads=pd.read_csv("recent-grads.csv")
print(recent_grads.iloc[0])
print(recent_grads.head())
print(recent_grads.tail())
print(recent_grads.describe())

#drop rows with missing data
recent_grads=recent_grads.dropna()


# =============================================================================
# 
# # generate scatter plots and explore the following relations:
# #   Sample_size and Median
# #   Sample_size and Unemployment_rate
# #   Full_time and Median
# #   ShareWomen and Unemployment_rate
# #   Men and Median
# #   Women and Median
# =============================================================================


recent_grads.plot(x='Sample_size', y='Employed', kind='scatter', title='Employed vs. Sample_size', figsize=(5,10))

recent_grads.plot(x="Sample_size", y="Median", kind='scatter', title='Median vs Sample_size')
recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter', title='Unemployment_rate vs Sample_size')
recent_grads.plot(x='Full_time', y='Median', kind='scatter', title='Median vs Full-time')
recent_grads.plot(x='ShareWomen', y='Unemployment_rate',kind='scatter', title='Unemployment_rate vs ShareWomen')
recent_grads.plot(x='Men', y='Median',kind='scatter', title='Median vs Men')


recent_grads.plot(x='Sample_size', y='Employed', kind='scatter', title='Employed vs. Sample_size', figsize=(5,10))

recent_grads.plot(x="Sample_size", y="Median", kind='scatter', title='Median vs Sample_size')
recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter', title='Unemployment_rate vs Sample_size')
recent_grads.plot(x='Full_time', y='Median', kind='scatter', title='Median vs Full-time')
recent_grads.plot(x='ShareWomen', y='Unemployment_rate',kind='scatter', title='Unemployment_rate vs ShareWomen')
recent_grads.plot(x='Men', y='Median',kind='scatter', title='Median vs Men')

#Do students in more popular majors make more money?
recent_grads.plot(x='Total', y='Median',kind='scatter', title='total vs Median')

#Do students that majored in subjects that were majority female make more money?
recent_grads.plot(x='ShareWomen', y='Median',kind='scatter', title='ShareWomen vs Median')

#Is there any link between the number of full-time employees and median salary?
recent_grads.plot(x='Full_time', y='Median',kind='scatter', title='Full_time vs Median')
plt.show()

#  explore the distributions of the following columns

cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

fig = plt.figure(figsize=(5,12))
for r in range(1,9):
    ax = fig.add_subplot(8,1,r)
    ax = recent_grads[cols[r-1]].plot(kind='hist',  rot=40, title=str(cols[r-1]))
    plt.show()    
  
    
#What's the most common median salary range?
# 2500 to 5500    
recent_grads['Median'].plot(kind='hist') 
plt.show()  


# generate scatter_matrix plots


pplt.scatter_matrix(recent_grads[['Women', 'Men']], figsize=(10,10))

pplt.scatter_matrix(recent_grads[['Sample_size', 'Median']])

pplt.scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']])
plt.show()

recent_grads[:5].plot.bar(x='Major', y='Women')
plt.show()

recent_grads.sort_values('ShareWomen').head(10).plot.bar(x='Major', y='ShareWomen')

recent_grads.sort_values('ShareWomen').tail(10).plot.bar(x='Major', y='ShareWomen')
plt.show()


recent_grads.sort_values('Unemployment_rate').head(10).plot.bar(x='Major', y='Unemployment_rate')
plt.show()
recent_grads.sort_values('Unemployment_rate').tail(10).plot.bar(x='Major', y='Unemployment_rate')
plt.show()




#Use a box plot to explore the distributions of median salaries and unemployment rate.

recent_grads['Median'].plot(kind='box')
plt.show()
recent_grads['Unemployment_rate'].plot(kind='box')

#Use a hexagonal bin plot to visualize the columns that had dense scatter plots from earlier in the project.
recent_grads.plot(kind='hexbin', x='Full_time', y='Median')

recent_grads.plot(kind='scatter', x='ShareWomen', y='Full_time')

