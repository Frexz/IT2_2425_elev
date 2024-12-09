import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
p1 = sns.color_palette('pastel', 8)

fig, ax = plt.subplots(2, 2)

sns.barplot(data=df, x="day", y="tip", hue="day", estimator="sum", errorbar=None,
            palette=p1, ax=ax[0][0])

sns.barplot(data=df, x="day", y="size", hue="day", estimator="size", errorbar=None,
            palette=p1, ax=ax[0][1])
plt.show()

