import pandas as pd

url = 'https://hotell.difi.no/download/statens-satser/utland/2019'
# Lager en pandas DataFrame fra csv-filen
df = pd.read_csv(url, sep=';')
# Skriver u DataFrame-objektet (som en tabell)
# Sortert etter kost fra høyest til laves, head(5) betyr de fem først, og
# fillna angir hva man fyller tomme felter med.
print(df.sort_values(by='kost', ascending=False).head(5).fillna(''))