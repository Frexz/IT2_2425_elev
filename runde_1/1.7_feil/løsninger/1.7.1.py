bruker_input = input('Skriv inn et tall mellom 1 og 7: ')
farger = ['rød', 'oransje', 'gul', 'grønn', 'blå', 'indigo', 'lilla']

try:
    print(f'Flott! Du valgte {farger[int(bruker_input) - 1]}')
except IndexError:
    print(f'{bruker_input} er ikke mellom 1 og 7.')