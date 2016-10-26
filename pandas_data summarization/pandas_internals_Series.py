from pandas import Series
import pandas
file = pandas.read_csv("fandango_score_comparison.csv")
series_film = file["FILM"]
series_film=series_film.values
series_rt = file["RottenTomatoes"]
series_rt=series_rt.values
# print series_rt.values

ans = Series(index=series_film, data=series_rt)
# print ans

######################
fiveten = ans[5:11]
# print fiveten
##############

series_custom = ans
original_index = series_custom.index.tolist()
# print original_index
# print sorted(original_index)
sortd_by_index = ans.reindex(sorted(original_index))
# print sortd_by_index

##################
sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
# print sc3.head(10)

####################

series_normalized = series_custom / 20
# print series_normalized

################
a = series_custom>50
series_greater_than_50 =  series_custom[a]

b = series_custom <20
# print series_custom[a|b]

###################

rt_critics = Series(file["RottenTomatoes"].values, index = file["FILM"])
rt_users = Series(file["RottenTomatoes_User"].values, index = file["FILM"])
import numpy as np
x = [rt_users, rt_critics]
m = np.mean(x,axis=0)
# print m
m2 = Series(m, index = file["FILM"])
print m22
# mean_2 = (rt_critics+rt_users)/2
# print mean_2
















































