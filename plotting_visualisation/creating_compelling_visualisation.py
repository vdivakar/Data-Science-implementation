import pandas
# print 332
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# sns.distplot(births['prglngth'], kde=False)
# sns.plt.show()
#####################

a = [1,2,3,4,5,6,7,1,2,3]
b = [600,150,200,300,200,100,125,180, 300, 500]
file = (a,b)
plt.bar(a,b)
plt.show()

file.pivot_table(index="Major_category", values="Total", aggfunc=sum	)































