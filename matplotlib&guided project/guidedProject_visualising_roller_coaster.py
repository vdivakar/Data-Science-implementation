import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

pixar_movies = pd.read_csv("pixar_movies.csv")
# print pixar_movies.shape
pixar_movies.head(10)
# print pixar_movies.dtypes

# print pixar_movies.describe()

# pd.Series.str.rstrip(pixar_movies[" Gross	Domestic %"])

# clean = pixar_movies["Domestic %"].str.rstrip("%")

file = pixar_movies
# print file.head(3)
file["	IMDB Score"] = file["	IMDB Score"]*10
# print file["	IMDB Score"]

filtered_pixar = file.loc[0:13]
# print filtered_pixar
# fg = file.dropna()###### dropna not working
# print fg

filtered_pixar.set_index("	Movie", inplace = True)
# print filtered_pixar

critics_reviews = filtered_pixar[['	RT Score', '	IMDB Score', '	Metacritic Score']]
# print critics_reviews


# critics_reviews.plot(figsize=(9,5), kind = "box")
# plt.show()

a = file[['	RT Score', '	IMDB Score']]
a.plot(kind="bar", stacked=True)
plt.show()




































































