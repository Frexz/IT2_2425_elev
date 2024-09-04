bruker_input = input('Skriv inn et heltall, eller "slutt" for å avslutte: ')

while bruker_input != 'slutt':

    try:
        print(f'{bruker_input} i titallssystemet er {int(bruker_input):b} binært.')
    except ValueError:
        print('Skriv inn et heltall.')
    finally:
        bruker_input = input('Skriv inn et heltall, eller "slutt" for å avslutte: ')