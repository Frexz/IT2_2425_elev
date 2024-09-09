fortsette = 'ja'
brukere = {}
with open('brukernavn.txt', mode='w', encoding='utf-8') as fil:
    while fortsette == 'ja':
        brukernavn = input('Skriv inn et brukernavn: ')
        passord = input('Skriv inn et passord: ')

        brukere[brukernavn] = passord

        fortsette = input('Vil du fortsette? ')
    
    fil.write(str(brukere))
