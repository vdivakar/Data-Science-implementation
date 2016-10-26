import pandas
file = pandas.read_csv("forestfires.csv")
# print file.head(5)

# import matplotlib.pyplot as plt
# weight = [600,150,200,300,200,100,125,180]
# height = [60,65,73,70,65,58,66,67]

import matplotlib.pyplot as plt
# plt.scatter(height, weight)
# plt.show()

# plt.scatter(file["wind"], file["area"])
# plt.show()
# age = [5, 10, 15, 20, 25]
# height = [25, 45, 65, 75, 75]
# plt.plot(age, height)
# plt.show()


# names = ["McDonalds", "Burger King", "Wendys", "Subway"]
# patrons = [10000, 5000, 5000, 7500]
# x = [0, 1, 2, 3]

# plt.bar(x, patrons)
# plt.show()
import numpy
forest_fires = file
area_by_y = forest_fires.pivot_table(index="Y", values="area", aggfunc=numpy.mean)
area_by_x = forest_fires.pivot_table(index="X", values="area", aggfunc=numpy.mean)
print area_by_x.index
# plt.bar(area_by_y.index, area_by_y)
# plt.show()
# plt.bar(area_by_x.index, area_by_x)
# plt.show()


# area_by_month = forest_fires.pivot_table(index="month", values="area", aggfunc=numpy.mean)
# area_by_day = forest_fires.pivot_table(index="day", values="area", aggfunc=numpy.mean)
# print area_by_month
# print area_by_day

# plt.barh(area_by_month,range(len(area_by_month)) )
# plt.show()
# plt.barh(area_by_day ,range(len(area_by_day)))
# plt.show()

# wind = forest_fires["wind"]
# area = forest_fires["area"]
# plt.scatter(wind, area)
# plt.title("Wind speed vs fire area")
# plt.xlabel("Wind speed when fire started")
# plt.ylabel("Area consumed by fire")
# plt.show()
# import seaborn

# plt.style.use("ggplot") 	## bmh , dark_background, thirtyfiveight
rain = forest_fires["rain"]
area = forest_fires["area"]

plt.scatter(rain, area)
plt.title("Rain vs Area burnt")
plt.xlabel("Rain")
plt.ylabel("Area")
plt.show()






















































