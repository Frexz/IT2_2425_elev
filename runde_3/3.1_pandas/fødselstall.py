import pandas as pd

df = pd.read_csv("fødselstall.csv", encoding="utf-8").fillna(0)
df.columns = ["År", "Fødsler", "Innflyttinger", "Utflyttinger"]
df = df.drop(index=79)
df["Netto"] = df["Fødsler"] + df["Innflyttinger"] - df["Utflyttinger"]
print(df)
