print('Når du er ferdig med å skrive inn tall,')
print('kan du trykke på ENTER uten å skrive noe for å avslutte.')

antall_tall = 0

while True:
    tekst_inn = input('Skriv inn et heltall: ')

    # Avslutter løkka
    if tekst_inn == '':
        break
    
    # Sjekker om input fra bruker er et tall.
    # Hvis det er et tall skrives du ut og antall_tall økes med 1
    # Hvis det ikke er tall gis det beskjed og løkka starter på nytt
    if tekst_inn.isnumeric():
        tall = int(tekst_inn)
        print(f'Du skrev inn {tall}.')
        antall_tall += 1
    else:
        print(f'{tekst_inn} er ikke et heltall.')

print(f'Du skrev inn {antall_tall} tall.')
print('Takk for nå.')