import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lag pandas DataFrame fra csv
df = pd.read_csv('bear_attacks.csv')

# Tell opp antall linjer per måned med value_counts(). reset_index() returnerer en ny DataFram med to kolonner, måneder og antall angrep per måned
attacks_month = df["Month"].value_counts().reset_index()
attacks_month.columns = ["Month", "Number of Attacks"]

# Lag en rekkfølge for månedene slik at de vises i riktig rekkefølge i diagrammet
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Plott søylediagrammet
sns.barplot(data=attacks_month, x="Month", y="Number of Attacks", order=month_order)
plt.xlabel("Month")
plt.ylabel("Number of Attacks")
plt.title("Number of bear attacks by month")
plt.show()

# Tell opp antall angrep per type
bear_types = df["Type of bear"].value_counts().reset_index()
bear_types.columns = ['Type', 'Kills']

# Plott sektordiagrammet. Merk at seaborn ikke har et sektordiagram og vi bruker sektordiagrammet fra matplotlib-biblioteket
plt.pie(bear_types["Kills"], labels=bear_types["Type"], autopct='%.0f%%', colors=["#633624", "#454241", "#f2f2eb"])
plt.title("Bear attacks by type")
plt.show()

