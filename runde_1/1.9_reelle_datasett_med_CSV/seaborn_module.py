import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://hotell.difi.no/download/statens-satser/utland/2019'
# Lager en pandas DataFrame fra csv-filen
df = pd.read_csv(url, sep=';')

# Lager og viser et boksplot med verdensdel på x-aksen og kost på y-aksen
sns.set_style('darkgrid')
sns.boxplot(data=df, x='verdensdel', y='kost').set(title='Statens satser utland 2019')
plt.show()