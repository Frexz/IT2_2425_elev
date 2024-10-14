personer = [
    {"fornavn": "Knut", "alder": 48},
    {"fornavn": "Tiril", "alder": 28},
    {"fornavn": "Eirik", "alder": 62},
    {"fornavn": "Elianne", "alder": 36},
    {"fornavn": "Albert", "alder": 17},
]

# Med itemgetter kan man finne største og minster verdi i en liste
# med ordbøker ut fra hvilken nøkkel man ser på, samt sortere basert på nøkkel

from operator import itemgetter
eldst = max(personer, key=itemgetter("alder"))
print(f"{eldst["fornavn"]} på {eldst["alder"]} er eldst.")
yngst = min(personer, key=itemgetter("alder"))
print(f"{yngst["fornavn"]} på {yngst["alder"]} er yngst.")

print("\nSortert alfabetisk")
for person in sorted(personer, key=itemgetter("fornavn")):
    print(f"{person["fornavn"]:10}{person["alder"]:3} år")

print("\nSortert etter alder")
for person in sorted(personer, key=itemgetter("alder")):
    print(f"{person["fornavn"]:10}{person["alder"]:3} år")

# Man kan også omgjøre en liste med ordbøker om til en pandas DataFrame
import pandas as pd
print("\nDataFrame")
df = pd.DataFrame(personer).sort_values(by="fornavn")
print(df)