# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 00:38:41 2018

@author: Huiting
"""

import pandas as pd
import matplotlib.pyplot as plt
import pandas.plotting as pplt
import numpy as np
recent_grads=pd.read_csv("recent-grads.csv")
#print(recent_grads.iloc[0])
#print(recent_grads.head())
#print(recent_grads.tail())
#print(recent_grads.describe())
raw_data_count=173
recent_grads=recent_grads.dropna()
#print(recent_grads.describe())
cleaned_data_count=172


# =============================================================================
bar_position=np.arange(172)+1
# bar_height1=recent_grads['Men'].values
# bar_height2=recent_grads['Women'].values
# 
width=0.25 
fig,ax=plt.subplots(figsize=(100,10))
tick_position=range(1,173)
# 
plt.bar(bar_position, recent_grads['Men'].values,0.25,color='red')
plt.bar([p + 0.25 for p in bar_position], recent_grads['Women'].values,0.25, color='blue')
ax.set_xticks(tick_position)
ax.set_xticklabels(recent_grads['Major'], rotation=90)
ax.set_ylim(0,max(recent_grads['Men']+ recent_grads['Women']))
plt.legend(['Men','Women'], loc='upper left')
# p2=ax.bar(bar_position, bar_height2, 0.5, color='blue')
# ax.autoscale_view()
# =============================================================================


plt.show()


raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'pre_score': [4, 24, 31, 2, 3],
        'mid_score': [25, 94, 57, 62, 70],
        'post_score': [5, 43, 23, 23, 51]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'pre_score', 'mid_score', 'post_score'])

print(df)
print(df['first_name'][0])
# Setting the positions and width for the bars
pos = list(range(len(df['pre_score']))) 
width = 0.25 
    
# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos, 
        #using df['pre_score'] data,
        df['pre_score'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#EE3224', 
        # with label the first value in first_name
        #label=df['first_name'][0]
        ) 

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos], 
        #using df['mid_score'] data,
        df['mid_score'],
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#F78F1E', 
        # with label the second value in first_name
        #label=df['first_name'][1]
        ) 

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos], 
        #using df['post_score'] data,
        df['post_score'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#FFC222', 
        # with label the third value in first_name
        #label=df['first_name'][2]
        ) 

# Set the y axis label
ax.set_ylabel('Score')

# Set the chart's title
ax.set_title('Test Subject Scores')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['first_name'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['pre_score'] + df['mid_score'] + df['post_score'])] )

# Adding the legend and showing the plot
plt.legend(['Pre Score', 'Mid Score', 'Post Score'], loc='upper left')
plt.grid()
plt.show()

