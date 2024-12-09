import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
data = df.groupby("day").sum(numeric_only=True).sort_values("tip")
data.plot.pie(y="tip",
              radius=0.8, autopct="%0.1f%%").set(title="Total tips fordelt på ukedager", ylabel="")

plt.show()