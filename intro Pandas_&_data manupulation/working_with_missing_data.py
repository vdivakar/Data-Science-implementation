location = r'C:\Users\DIVAKAR\Desktop\train.csv'

import pandas
file = pandas.read_csv(location)

# print file["Age"]

age_null_count = pandas.isnull(file["Age"])
# print age_null_count
count = 0
for x in age_null_count:
	if (x==True):
		count+=1
# print count

#####################

age_null = file["Age"][age_null_count==False]
average = age_null.sum() / len(age_null)
# print average

######################
# print file["Age"].mean()

#####################
passenger_classes = [1,2,3]
fares_by_class={}
for x in passenger_classes:
	age_group =(file["Pclass"]==x)
	fares_by_class[x]= (file["Fare"][age_group==True]).mean()
print fares_by_class

for x in passenger_classes:
	rows = file[file["Pclass"]==x]
	av = rows["Fare"].mean()
	fares_by_class[x]= av

# print fares_by_class



###############

import numpy as np
passenger_survival = file.pivot_table(index = "Survived", values = "Age", aggfunc=np.mean)
# print passenger_survival

################

port_stats = file.pivot_table(index="Pclass", values=["Age","Survived"], aggfunc=np.mean)
# print port_stats

################
new_file = file.dropna(subset=["Age", "Sex"])
# print new_file
##################
# print file.iloc[5:15,3:5]
f = file.dropna(subset=["Age"])
# print f.iloc[5:15,3:5]
# print f.loc[3,:]

#############################
f = file.dropna(subset=["Cabin"])
# print f
f2 = f.reset_index(drop=True)
# print f2

##################
def is_minor(row):
	if row["Age"] < 18:
		return True
	else:
		return False

minors = file.apply(is_minor, axis=1)
# print minors
n = pandas.isnull(minors)
minors[n==True] = "unknown"
# print minors

####################
table = file.pivot_table(index="Age", values="Survived", aggfunc=np.mean)
age_group_survival = table
# print age_group_survival

# print file.index
print file.iloc[[0,len(file)-1]]












