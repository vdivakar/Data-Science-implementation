#### 3

country_is_algeria = (world_alcohol[:,2] == "Algeria")
country_algeria = world_alcohol[country_is_algeria , :]

#### 4

is_algeria_and_1986 = ( world_alcohol[:,2]=="Algeria" ) & (world_alcohol[:,0]=="1986")
 
########### 5

a = world_alcohol[:,0] == "1986"
world_alcohol[a,0] = "2014"


a = world_alcohol[:,3] == "Wine"
world_alcohol[a,3] = "Grog"
##### 6

is_value_empty = (world_alcohol[:,4]) == ''
world_alcohol[is_value_empty,4] = "0"

####### 7 
alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)

############ 8
total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

############ 9
canada_1989 = (world_alcohol[:,0]=="1986")&(world_alcohol[:,2]=="Canada")
canada_1989 = world_alcohol[canada_1989,:]
c = (canada_1989[:,4]=='')
canada_1989[c,:] = "0"
canada_alcohol=canada_1989.astype(float)
total_canadian_drinking = canada_alcohol.sum()





























