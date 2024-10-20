import pandas as pd
import os

personer = [
    {'fornavn': 'Kari', 'etternavn': 'Hansen', 'fødselsår': 2001},
    {'fornavn': 'Gustav', 'etternavn': 'Monsen', 'fødselsår': 1995},
    {'fornavn': 'Anette', 'etternavn': 'Ås', 'fødselsår': 1998},
    {'fornavn': 'Marius', 'etternavn': 'Lie', 'fødselsår': 2002},
    {'fornavn': 'Wenche', 'etternavn': 'Hovland', 'fødselsår': 1999},
]

def gi_valg():
    print("\nSorter etter følgende rekkefølge: ")
    print("F=fornavn, E=etternavn, A=fødselsår, S=slutt")
    valg = input("Velg F, E, A eller S: ").upper()

    while valg not in "FEAS":
        print("Det forstod jeg ikke. Prøv igjen.\n")
        print("Sorter etter følgende rekkefølge: ")
        print("F=fornavn, E=etternavn, A=fødselsår, S=slutt")
        valg = input("Velg F, E, A eller S: ").upper()
    return valg

df = pd.DataFrame(personer)
sorter = gi_valg()

while sorter != "S":
    os.system("cls")
    if sorter == "F":
        df = df.sort_values(by="fornavn")
    elif sorter == "E":
        df = df.sort_values(by="etternavn")
    elif sorter == "A":
        df = df.sort_values(by="fødselsår")
    
    print(df)

    sorter = gi_valg()