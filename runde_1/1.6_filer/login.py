brukernavn = input('Skriv inn brukernavnet ditt: ')
passord = input('Skriv inn passordet ditt: ')

with open('brukernavn.txt', encoding='utf-8') as fil:
    brukere = eval(fil.read())

    if brukernavn in brukere:
        if brukere[brukernavn] == passord:
            print(f'Velkommen tilbake, {brukernavn}!')
        else:
            print('Feil passord.')
    else:
        print('Brukernavnet eksisterer ikke.')
        