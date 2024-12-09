"""
Endret filnavn til youtube.csv for enklere referanse. Endret kolonnenavn til henholdsvis "land", "subs" og "views".
Fjernet rader med veriden 'NaN' i kolonnen "land".
"""
import pandas as pd

pd.options.display.float_format = '{:.0f}'.format
df = pd.read_csv('youtube.csv', encoding='unicode_escape')
df = df[["Country", "subscribers", "video views"]]
df.columns = ["land", "subs", "views"]
df = df.dropna()

topp_10 = pd.DataFrame(df.value_counts(subset=["land"])).head(10)
topp_10.columns = ["antall_kanaler"]
print(topp_10)

gjennomsnitt = df.groupby(by="land").mean()
print(gjennomsnitt)

topp_10 = pd.merge(topp_10, gjennomsnitt, on="land")
print(topp_10)

