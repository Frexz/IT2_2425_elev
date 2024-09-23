# Øvingsoppgaver 1.9

## 1.9.1
I denne oppgaven skal du analysere samlivsformer i Norge. Gifter flere eller færre seg nå enn tidligere? Lag et program som laster ned csv-filen fra

[Personer 18 år og over, etter smlivsform, i prosent. Hele landet, 2005 - siste år](https://data.ssb.no/api/v0/dataset/86813?lang=no)

Forklar hvor du finner lenken til csv-filen: [https://data.ssb.no/api/v0/dataset/86813.csv](https://data.ssb.no/api/v0/dataset/86813.csv)

Utforsk [seaborn.lineplot](https://seaborn.pydata.org/generated/seaborn.lineplot.html) og lag et linjediagram med år langs x-aksen. De ulike samlivsformene skal vises i prosent langs y-akse. Diagrammet skal ha tre linjer; en for hver av samlivsformene.

### Tips
Denne filen bruker ikke ```utf-8```-encoding, en ```windows-1251```, og vi bør oppgi at komma brukes som desimaltegn i stedet for punktum:

```
df = pd.read_csv(url, sep=';', decimal=',', encoding='windows-1252')
```

Vi får tak i en kolonne gjennom kolonnenavnet som hentes fra overskriftraden. Hvis denne teksten er svært lang, som i dette datasettet, kan vi endre på kolonnenanvnet eller angi kolonnen ved indeks:

```
df.iloc[:, 4]
```

eller slik

```
df.columns.values[4] = "prosent"
df["prosent"]
```

Hvis årstallene blir gjort om til desimaltall i grafen, er det flere måter å løse det på. Et alternativ er å gjøre årene, som er heltall, om til ```Timestamp```-objekter.

```
df["år"] = pd.to_datetime(df["år"].astype(str), format="%Y")
```

## 1.9.2
Ta utgangspunkt i datasettet `bear_attacks.csv`. 

a) Lag et søylediagram som viser antall bjørneangrep fordelt på månedene i året.

b) Lag et sektordiagram som viser prosentfordelingen av angrepene på de ulike bjørnetypene.