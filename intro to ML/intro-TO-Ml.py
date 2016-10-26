# import auto_mp

import pandas as pd
mpg = pd.read_table("auto_mpg.data", delim_whitespace=True)
# print pd.read_table("auto-mpg.names")

from matplotlib import pyplot as plt 

# f= plt.figure()
# up = f.add_subplot(2,1,1)

'''
fig = plt.figure()
left = fig.add_subplot(1,2,1)
right = fig.add_subplot(1,2,2)
left.scatter(month_2013, temperature_2013, color='darkblue', marker='o' )
left.set(title= '2013', xlim=(0,13), ylim=(0,110))
right.scatter(month_2014, temperature_2014, color = 'darkgreen', marker='o')
right.set(title='2014', xlim=(0,13), ylim=(0,110))
'''

from sklearn.linear_model import LinearRegression

cars = mpg


c = filtered_cars
fig = plt.figure()
up = fig.add_subplot(2,1,1)
up.scatter(filtered_cars['horsepower'], filtered_cars['mpg'], color='red')
down = fig.add_subplot(2,1,2)
down.scatter(filtered_cars['weight'], filtered_cars['mpg'], color='blue')



"""
fig = plt.figure()
c = filtered_cars
up = fig.add_subplot(2,1,1)
up.scatter(c['horsepower'], predictions, color = 'red')
down = fig.add_subplot(2,1,2)
down.scatter(c['horsepower'], c['mpg'])
"""




