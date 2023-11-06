import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

url = 'Placement_Data_Full_Class.csv'
data = pd.read_csv(url)


print(data.head())


data.hist(bins=10)

#plt.show()

# for i in data.columns:
#     print(data[i].describe())
print(data.columns)

filter_m = data.query("gender == 'M'").dropna(subset=['salary'])
filter_f = data.query("gender == 'F'").dropna(subset=['salary'])

#print(f"filter_m: {filter_m} \n filter_f: {filter_f}")
#for i in filter_m.columns:
#    if i == 'gender':
#        print(filter_m[i])

t, p = ttest_ind(filter_m['salary'], filter_f['salary'])
print(f"t = {t}, p = {p}")