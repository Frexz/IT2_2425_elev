import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://data.ssb.no/api/v0/dataset/86813.csv"

# Lager en pandas.DataFrame der vi angir ; som separator, komma som desimaltegn og enkoding windows-1252
df = pd.read_csv(url, sep=';', decimal=',', encoding='windows-1252')

# Endrer kolonnenavnet til Prosent
df.columns.values[4] = "Prosent"

# Endrer årstall til DateTime-objekter slik at de vises som heltall i stedet for flyttall.
df["år"] = pd.to_datetime(df["år"].astype(str), format="%Y")

# Linjeplottet til seaborn tar en pandas.DataFram som argument for data-parameteren,
# x og y er kolonnenavnet til dataene som skal plottes på henholdsvis x og y-akse.
# hue-parameteren grupperer dataene i ulike kategorier der samlivsform er kolonnenavnet til kategoriene
# vi ønsker å dele inn i.
sns.lineplot(data=df, x='år', y='Prosent', hue='samlivsform')
plt.show()



