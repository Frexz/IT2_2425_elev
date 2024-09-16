import csv
from operator import itemgetter
import requests

url = 'https://hotell.difi.no/download/statens-satser/utland/2019'

# Legger en liste med hver linje inn i et csv.reader-objekt
csv_reader = csv.reader(requests.get(url).text.splitlines(), delimiter=';')
# Hver rad i tabellen er hver linje fra csv-filen som har en verdi i kost-klonnen
tabell = [x for x in list(csv_reader) if x[3].isnumeric()]
for rad in tabell:
    rad[3] = int(rad[3])
# itemgetter-funksjonen henter verdier fra indeks 3 i hvert element, [:5] betyr bare de fem første
# og * før sorted() betyr at vi tar tabellen som returneres og pakker den ut, separert med et linjeskifte.
print(*sorted(tabell, reverse=True, key=itemgetter(3))[:5], sep='\n')