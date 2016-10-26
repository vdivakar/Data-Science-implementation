import pandas
file = pandas.read_csv("fandango_score_comparison.csv")
# print file.head(2)
# print file.index
# print "############"

#################
# print file.iloc[0:5]
first_last = file.iloc[[0,len(file)-1]]
# print first_last
# print file.shape

##################
fandango_films = file.set_index("FILM", drop=False)
# print fandango_films.index
# print file.index

##################

types = file.dtypes
# print types
# print file[file.dtypes == "float64"]
# print types.values
file[file.dtypes[file.dtypes.values=='float64'].index]

types = file.dtypes
# print types
float_columns = types[types.values == 'float64']
# print float_columns.index
ans = file[float_columns.index]
# print ans
import numpy as np
deviations = ans.apply(lambda x: np.std(x))
# print deviations

# print file.apply(lambda x:x*2)


###################
c = ["RT_user_norm", "Metacritic_user_nom"]
new_file = file[c]

rt_mt_means = new_file.apply(lambda x: np.mean(x), axis=1)
print rt_mt_means
































