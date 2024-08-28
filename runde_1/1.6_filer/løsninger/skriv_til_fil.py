with open('heltall.txt', mode='w') as fil:
    bruker_input = input('Skriv inn et heltall: ')

    while bruker_input != '':
        fil.write(f'{bruker_input}\n')
        bruker_input = input('Skriv inn et heltall: ')