import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../disasters.csv")
maks = df["Total Deaths"].idxmax()

print(df.loc[maks])

data = df.groupby("Disaster Type").count()
data.plot.pie(y="Year", radius=1, autopct="%0.1f%%")
plt.show()