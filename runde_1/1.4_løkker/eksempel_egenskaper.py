from random import randint

# Definerer en funksjon som returnerer resultatet av et vanlig terningkast
def kast():
    return randint(1, 6)

egenskaper = []

for i in range(6):
    resultater = [kast() for i in range(4)] # Fyller en ny liste med 4 terningkast
    resultater.sort(reverse=True)
    egenskaper.append(sum(resultater[:3]))  # Legger til summen av de tre første resultatene

print(egenskaper)


