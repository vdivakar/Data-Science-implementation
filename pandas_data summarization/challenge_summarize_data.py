import pandas
file = pandas.read_csv("all-ages.csv")
# print file.head(5)

#################
import numpy
# print file["Major_category"].value_counts() 
all_ages_major_categories = file.pivot_table(index="Major_category", values="Total", aggfunc=sum	)
# print f
recent_grads = pandas.read_csv("recent-grads.csv")
# recent_grads_major_categories = recent_grads.pivot_table(index="Major_category", values="Total", aggfunc=sum)
# print recent_grads_major_categories
dictionary = dict()
all_ages_major_categories = dict()
cats =  file["Major_category"].value_counts().index
for x in cats:
	major = file[file["Major_category"]==x]
	Total = major["Total"].sum
	dictionary[x] = Total
	# print major
	# break 
# print dictionary 
##########################

file = pandas.read_csv("recent-grads.csv")
t = file["Total"].sum()
l = file["Low_wage_jobs"].sum()
# print float(l)/float(t) *100

#############################
recent_grads_lower_unemp_count=0
all_ages_lower_unemp_count =0
recent_grads = pandas.read_csv("recent-grads.csv")
all_ages = pandas.read_csv("all-ages.csv")
majors = recent_grads["Major"].value_counts().index
# print majors
for x in majors:
	recent = recent_grads[recent_grads["Major"]==x]
	all_ag = all_ages[all_ages["Major"]==x]

	sum_recent = recent["Unemployment_rate"].sum()
	sum_all = all_ag["Unemployment_rate"].sum()

	if sum_recent< sum_all:
		recent_grads_lower_unemp_count+=1
	elif sum_recent> sum_all:
		all_ages_lower_unemp_count+=1

print recent_grads_lower_unemp_count
print all_ages_lower_unemp_count

















































