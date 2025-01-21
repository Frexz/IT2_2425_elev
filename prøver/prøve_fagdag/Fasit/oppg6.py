import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# a)
df = pd.read_csv("svalbard.csv")
df = df.drop(columns=["D-J-F","M-A-M","J-J-A","S-O-N","metANN"])
df.replace(999.9, np.nan, inplace=True)
months = df[df.columns.difference(["YEAR"])]

min_temp = months.min().min()
max_temp = months.max().max()

min_idx = months.stack().idxmin()
max_idx = months.stack().idxmax()

min_year = df.loc[min_idx[0], "YEAR"]
max_year = df.loc[max_idx[0], "YEAR"]

print(f"Kaldeste\n{min_year}: {min_temp}")
print(f"Varmeste\n{max_year}: {max_temp}")

# b)
last_years = df[(df["YEAR"] >= 2000) & (df["YEAR"] <= 2017)]
last_monts = last_years[last_years.columns.difference(["YEAR"])]
last_years["Gjennomsnittstemperatur"] = last_monts.mean(axis=1).round(1)
print(last_years[["YEAR", "Gjennomsnittstemperatur"]])

# c)
months_2016 = df[df["YEAR"] == 2016]
months_2016 = months_2016.drop(columns=["YEAR"])
print(months_2016)
print(months_2016.T)
sns.lineplot(data=months_2016.T)
plt.show()