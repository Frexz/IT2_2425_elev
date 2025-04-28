import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dnd5e_monsters.csv")
df = df.drop(columns=["Size", "Armor", "Speed"])
drager = df[df["Type"] == "dragon"] 
drager = drager.sort_values(by="CR", ascending=False).head(10)

fig, ax = plt.subplots(figsize=(8, 12))
ax.tick_params(axis="x", labelrotation=45)
plt.subplots_adjust(bottom=0.3)
sns.barplot(data=drager, x="Name", y="HP")
plt.show()