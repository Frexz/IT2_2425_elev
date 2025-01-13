import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../disasters.csv")

data = df.groupby("Region").count()
data["count"] = data["Year"]
print(data)

sns.barplot(data=data, x=data["count"], y=data.index, orient="h")
plt.show()