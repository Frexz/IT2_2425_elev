"""
Figure og Axes er objekter i matplotlib-modulen.
Figure lar oss endre figurens størrelse, overskrift og tittel på vinduet
Axes lar oss endre selve diagrammet
"""

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# Lager et Figure-objekt og et Axes-objekt med tre diagrammer på rad
fig, ax = plt.subplots(1, 3)

# Endrer størrelsen på figuren
fig.set_size_inches(12, 5)

# Overskrift for hele figuren
fig.suptitle("Stoplediagram")

# Setter vindu-tittel
fig.canvas.manager.set_window_title("IT2")

# Legger til litt padding mellom diagrammene
fig.tight_layout(pad=3)

# ax-parameteren angir hvilket diagram som skal hvor
sns.barplot(data=df, x='day', y='tip',
            estimator='sum', errorbar=None,
            ax=ax[0]).set(title="Total tips fordelt på ukedager")

sns.barplot(data=df, x='day', y='tip', 
            order=['Sat', 'Sun', 'Thur', 'Fri'],
            estimator='sum', errorbar=None,
            ax=ax[1]).set(title="Total tips fordelt på ukedager")

sns.barplot(data=df, x='day', y='tip', hue="smoker",
            order=['Sat', 'Sun', 'Thur', 'Fri'],
            estimator='sum', errorbar=None,
            ax=ax[2]).set(title="Total tips fordelt på ukedager")

plt.show()

# catplot er også en type diagram som lar oss plotte like diagrammer side ved side
# parameteren col deler opp i ett diagram for hver verdi i col.
cp = sns.catplot(data=df, x="day", y="tip", col="smoker", errorbar=None, kind="bar")
cp.figure.suptitle("Total tips fordelt på ukedager")
cp.figure.tight_layout()
plt.show()