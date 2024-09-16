import requests

url = 'https://hotell.difi.no/download/statens-satser/utland/2019'
r = requests.get(url)

# Lager en liste med hver linje
linjer = r.text.split('\r\n')
# Viser de to første linjene
print(linjer[:2])

tabell = []

for linje in linjer:
    # Lager en liste med hver data for hver linje
    liste = linje.split(';')

    # Overskriftsrad og rader uten kost tas ikke med (1 og 113 blir utelatt)
    if liste[3].isnumeric():
        liste[3] = int(liste[3])
        tabell.append(liste)

# Viser to første rader i tabellen
print(tabell[:2])

# Sorterer hver rad i tabellen etter 'kost' fra høyest til lavest
sortert_tabell = sorted(tabell, reverse=True, key=lambda x: x[3])
for i in range(5):
    print(sortert_tabell[i])

print('\n***   De 5 dyreste stedene   ***')
print('Sted                        Kost')
print('--------------------------------')
# Skriver ut de 5 første radene (dyreste steder)
for rad in sortert_tabell[:5]:
    # Sted angis med by og land hvis raden har en by, hvis ikke bare med land.
    sted = f'{rad[2]}, {rad[1]}' if rad[2] != '' else rad[1]
    print(f'{sted:25}{rad[3]:7}')