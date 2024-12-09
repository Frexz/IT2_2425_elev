import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("disasters.csv")
data = df.groupby("Year").count()

sns.lineplot(data=data, x="Year", y="Disaster Type")
plt.show()