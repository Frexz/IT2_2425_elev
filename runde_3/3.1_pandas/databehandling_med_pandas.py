import pandas as pd

# Last inn et datasett med read_csv(). Det blir gjort om til en pandas DataFrame.
# En DataFrame er en tabell med rader og kolonner.
df = pd.read_csv("student_lifestyle_dataset.csv")

# DataFrame-objekter kan printes som en tabell. head()-metoden gir oss kun de første antall radene.
print("\n", "1".center(40, "-"))
print(df.head(5))

# Kolonnenavn kan ofte være lange, på engelsk, eller inneholde tegn vi ikke ønsker.
# For å endre kolonnenavn kan vi gi attributtetet columns en ny verdi. Verdien må være en liste med
# like mange strenger som det er kolonner.
print("\n", "2".center(40, "-"))
df.columns = ["ID", "Studere", "Aktiviteter", "Søvn", "Sosialt", "Fysisk", "Karaktersnitt", "Stress"]
print(df.head(5))

# info() gir oss informasjon om DataFrame-objektet slik som hvor mange rader og kolonner den har, navn på kolonner, datatyper i kolonnene, osv.
# describe() kan gi oss gjennomsnitt, standardavvik, median osv. per kolonne, men bare hvis hele DataFrame-objektet inneholder tall.
print("\n", "3".center(40, "-"))
df.info()
df.describe()

# Man kan plukke ut bestemte kolonner fra tabellen, eller plukke ut kolonner med rader som oppfyller et bestem kriterie.
print("\n", "4".center(40, "-"))
print(df[["Søvn"]])                     # Gir alle rader i kolonnen "Søvn"
print(df[df["Søvn"] < 6])               # Gir alle rader der "Søvn" er mindre enn 6 timer
print(df[df["Søvn"]<6][["Søvn"]])       # Gir alle rader kun i kolonnen "Søvn" der "Søvn" er mindre enn 6 timer

# Man kan legge til nye kolonner og fjerne kolonner med drop(columns=). Nye kolonner kan også være basert på utregninger med eksisterende kolonner
print("\n", "5".center(40, "-"))
df["Studere, prosent"] = df["Studere"] / 24 * 100
print(df.head(5))
df = df.drop(columns="Studere, prosent")
print(df.head(5))

# Man kan også legge til rader med pd.concat() og fjerne med drop(index=)
ny_rad = pd.DataFrame([[2001, 7, 6.5, 3, 6, 2, 3.5, "Moderate"]],
                      columns=["ID", "Studere", "Aktiviteter", "Søvn", "Sosialt", "Fysisk", "Karaktersnitt", "Stress"],
                      index=[2000])
df = pd.concat([df, ny_rad])
print("\n", "6".center(40, "-"))
print(df)

# For å sortere bruker man df.sort_values() og i kombinasjon med head() kan man plukke ut topp 3, topp 5, topp 10 osv.
print("\n", "7".center(40, "-"))
print(df.sort_values(by="Karaktersnitt", ascending=False).head(5))

# For å finne karaktergjennomsnittet til elevene gruppert etter stress-nivå bruker vi df.groupby() og df.mean()
print("\n", "8".center(40, "-"))
print(df.groupby(df["Stress"]).mean())
