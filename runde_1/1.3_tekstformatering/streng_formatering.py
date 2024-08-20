navn = 'Fredrik'
alder = 32

# Med konkatenering/skjøting
# Legg merke til at alder må gjøre om til typen string for at dette skal fungere
print('Jasså ' + navn + ', du er ' + str(alder) + ' år.')

# Med komma
# Her får man inn et mellom etter hvert komma
print('Jasså', navn, ', du er', alder, 'år.')

# Med %-operatoren (brukes ikke lengre)
print('Jasså %s, du er %s år.' % (navn, alder))

# Med str.format() (brukes ikke lengre)
print('Jasså {}, du er {} år.'.format(navn, alder))

# Med f-string (denne formen skal vi bruke)
print(f'Jasså {navn}, du er {alder} år.')