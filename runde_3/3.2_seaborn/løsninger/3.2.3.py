import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../disasters.csv")
data = df[df["Year"] == 2021]
data = data.groupby("Start Month").count()
data["count"] = data["Year"]
data.index = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt"]


sns.lineplot(data=data, x=data.index, y=data["count"])
plt.show()