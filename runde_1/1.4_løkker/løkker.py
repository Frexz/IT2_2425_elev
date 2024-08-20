# for-løkke
# Variabelen runde er ikke nødvendig for at løkken kjører, men måte å holde styr på
# hvor langt gjennomkjøringen har kommet.
runde = 0

for tall in range(10, 1, -2):
    runde += 1
    print(f'Tallet i {runde}. er {tall}')

# while-løkke
# I while-løkker er det viktig å oppdatere variabler, som er en del av betingelsen, inni løkke.
# Slik unngår man evige løkker.
teller = 10
while teller > 1:
    print(teller)
    teller -= 2

# Merk at hvis man endrer rekkefølgen på koden inni while-løkken
# man oppdatere startverdien og løkkas betingelse.
teller = 12
while teller > 2:
    teller -= 2
    print(teller)