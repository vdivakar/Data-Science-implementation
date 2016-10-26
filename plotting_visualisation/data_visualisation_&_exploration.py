import pandas
file = pandas.read_csv("recent-grads.csv")
# # print file.head(2)
# # print file.columns
recent_grads = file
import matplotlib.pyplot as plt

# columns = ['Median', 'Sample_size']
# file.plot.hist(by = 'Median')

#######################

# Select just `Sample_size` & `Major_category` columns from `recent_grads` 
# Name the resulting DataFrame as `sample_size`
# sample_size = recent_grads[['Sample_size', 'Major_category']]

# # Run the `boxplot()` function on `sample_size` DataFrame and specify, as a parameter, 
# # that we'd like a box and whisker diagram to be generated for each unique `Major_category`
# sample_size.boxplot(by='Major_category')

# # Format the resulting plot to make the x-axis labels (each `Major_category` value) 
# # appear vertically instead of horizontally (by rotating 90 degrees)
# plt.xticks(rotation=270)
# print sample_size
# plt.show()
#############################3

# recent_grads[['Total', 'Major_category']].boxplot(by='Major_category')
# plt.xticks(rotation=90)
# plt.show()

####################PLOTTING 2 GRAPHS TOGETHER
# Plot Unemployment_rate on x-axis, Median salary on y-axis, in red
plt.scatter(recent_grads['Unemployment_rate'], recent_grads['Median'], color='red')
# Plot ShareWomen (Female % in major) on x-axis, Median salary on y-axis, in blue
plt.scatter(recent_grads['ShareWomen'], recent_grads['Median'], color='blue')
plt.show()








































