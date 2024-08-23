# Vi kan bruke nøstede for-løkker til å lage gangetabellen. Nøstede for-løkker er for-løkker inni for-løkker.
# Den ytre for-løkken styrer antall rader i tabellen, mens den indre styrer antall kolonner i tabellen.

for rad in range(1, 11):
    print() # ny rad
    for kolonne in range(1, 11):
        print(f'{rad*kolonne:4}', end='') # skriver ut tall for hver kolonne til raden er fylt opp
        
