navn1 = input('Skriv inn det første navnet: ')
navn2 = input('Skriv inn det andre navnet: ')

if navn1 > navn2:
    print(navn1 + ' er større enn ' + navn2)
else:
    print(navn2 + ' er større eller lik ' + navn1)

# Når man sorterer strenger, eller tekst, gjør datamaskinen hvert symbole i teksten
# om til et tall etter et system som heter ASCII. I dette systemet er grupper med
# symboler sortert fra minst til størst slik: spesialtegn, sifre, store bokstaver,
# og små bokstaver. Tegn med lavest verdi kommer alfabetisk først, hvilket gjøre at
# strengen 'Fredrik' kommer før 'fredrik'.