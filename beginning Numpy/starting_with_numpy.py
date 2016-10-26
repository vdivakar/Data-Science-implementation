import csv
world_alcohol = open("world_alcohol.csv" , 'r')
read = csv.reader(world_alcohol)
world_alcohol = list(world_alcohol)		#makes it a list of list
years = []
for row in world_alcohol:
	years= years.append([0])
years = years[1:len(years)]
total = 0
for rows in years:
	total += float(row)
avg_year = total / len(years)
 

""""""" 4 "

import NumPy
world_alcohol = genfromtxt("world_alcohol.csv" , delimeter=",")

##### 5

vector = numpy.array([10,20, 30])
matrix = numpy.array([......])

##6

vector_shape = vector.shape 
matrix_shape = matrix.shape 
#########7

world_alcohol_dtype = world_alcohol.dtype 
########### 8

world_alcohol = genfromtxt("world_alcohol.csv", dtype = "U75", skip_header = True, delimeter = ",")
print (world_alcohol)

########### 10

uruguay_other_1986 = world_alcohol[1,4]
third_country = world_alcohol[2,2]

####### 11

countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]
########### 12

first_two_columns = world_alcohol[:,0:2]
first_ten_years = world_alcohol[0:10, 0]
first_ten_rows = world_alcohol[0:10 , :]
############ 13

f = world_alcohol[0:20,1:3]








