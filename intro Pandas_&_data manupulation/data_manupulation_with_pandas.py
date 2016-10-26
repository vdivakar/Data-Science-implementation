#### 1
location = r'C:\Users\DIVAKAR\Desktop\food_info.csv'
import pandas
food_info = pandas.read_csv(r"C:\Users\DIVAKAR\Desktop\food_info.csv")

cols = food_info.columns.tolist()
print food_info.head(3)


###### 2
# sodium_grams = food_info["Sodium_(mg)"] / 1000
# sugar_milligrams = food_info["Sugar_Tot_(g)"] * 1000



# normalised_protein = food_info["Protein_(g)"]
food_info["Normalized_Protein"] = food_info["	Protein_(g)"]






































