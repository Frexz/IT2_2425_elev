import requests
import pandas as pd
url = 'https://hotell.difi.no/download/statens-satser/utland/2019'
df = pd.read_csv(url, sep=';')
print(df.sort_values(by='kost', ascending=False).head(5).fillna(''))
