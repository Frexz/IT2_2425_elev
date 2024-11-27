import pandas as pd

df = pd.read_csv("homes.csv", encoding="utf-8")
df.columns = ["Salg", "Liste", "Stue", "Rom", "Soverom", "Bad", "Alder", "Tomt", "Skatt"]
df = df.groupby(df["Soverom"]).mean()
print(df)