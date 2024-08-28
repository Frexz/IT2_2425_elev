### Legge til elementer i en liste
venner = ['Ole', 'Dole', 'Doffen']

# append() - legger til element på slutten av listen
venner.append('Hetti')
print(venner, '\n')

# extend() - legger til flere elementer fra en annen liste på slutten av listen
venner.extend(['Netti', 'Donald'])
print(venner, '\n')

# insert() - legger til et element på en bestemt plass i listen
venner.insert(4, 'Letti')
print(venner, '\n')

### Fjerne elementer fra en liste

# remove() - fjerner første forekomst av oppgitt element
venner.remove('Donald')
print(venner, '\n')

# pop() - fjerner element fra en bestemt indeks fra listen og returnerer det fjernede elementet
navn = venner.pop(3)
print(navn)
print(venner, '\n')

# del - fjerner element fra indeks eller utsnitt
del venner[3:]
print(venner, '\n')
