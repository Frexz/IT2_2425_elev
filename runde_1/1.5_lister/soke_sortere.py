### Søke i lister
venner = ['Ole', 'Dole', 'Doffen', 'Dole', 'Dolly']

# index() - returnerer indeksen til et bestemt element i listen
navn = 'Doffen'
indeks = venner.index(navn)
print(f'{navn} finnes på indeks {indeks} i listen.')

# count() - teller hvor mange forekomster av et element det er i listen
navn = 'Dole'
antall = venner.count(navn)
print(f'{navn} finnes {antall} ganger i listen.')

## Sortere
venner = ['Ole', 'Dole', 'Doffen']

# sort() - sorterer elementene i listen
print('sort(): ')
print(venner)
venner.sort()
print(venner)

# sorted() - sorterer elementene i listen til en ny liste, beholder den gamle
print('sorted(): ')
venner = ['Ole', 'Dole', 'Doffen']
print(venner)
print(sorted(venner))
print(venner)

# reverse() - snur rekkefølgen på elementene i listen
venner = ['Ole', 'Dole', 'Doffen']
print('reverse(): ')
print(venner)
venner.reverse()
print(venner)