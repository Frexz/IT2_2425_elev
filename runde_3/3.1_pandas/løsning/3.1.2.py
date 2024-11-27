import pandas as pd

df = pd.read_csv("../tips.csv")

# a)
print("\n", "( a )".center(40, "-"))
print(df.sort_values(by="total_bill", ascending=False).head(3))

# b) - Alternativt kan man bruke: df.groupby("sex").size()
print("\n", "( b )".center(40, "-"))
print(df["sex"].value_counts())

# c)
print("\n", "( c )".center(40, "-"))
print(f"Største tips: ${df["tip"].max()}")

# d)
print("\n", "( d )".center(40, "-"))
df["andel"] = round(df["tip"] / df["total_bill"] * 100, 1)
print(f"Største andel: {df["andel"].max()}%")

# e)
print("\n", "( e )".center(40, "-"))
gjennomsnittlig_tips_etter_kjønn = df.groupby("sex")["andel"].mean()
kjønn_som_tipser_mest = "Kvinner" if gjennomsnittlig_tips_etter_kjønn.idxmax() == "Female" else "Menn"
print(gjennomsnittlig_tips_etter_kjønn)
print(f"De mest sjenerøse tipserne er {kjønn_som_tipser_mest.lower()}")

# f)
print("\n", "( f )".center(40, "-"))
print(f"Antall gjester: {df.sum()["size"]}")

# g)
print("\n", "( g )".center(40, "-"))
print(f"Mest vanlig antall gjester per regning: {df["size"].mode()[0]}")