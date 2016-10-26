
location = r'C:\Users\DIVAKAR\Desktop\food_info.csv'
import pandas
food_info = pandas.read_csv(location)
cols = (food_info.columns).tolist()
# print cols




###### 1
import pandas
food_info = pandas.read_csv(location)
# print type(food_info)


##### 2
first_rows = food_info.head(0)
# print first_rows

####### 3
column_names = food_info.columns
print column_names.tolist()
# print food_info.shape

######## 4
first_twenty = food_info.head(20)
# print first_twenty

############ 7 
hundred_row = food_info.loc[:]
# print hundred_row















