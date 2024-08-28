with open('heltall.txt') as fil:
    tall = [int(x) for x in fil]
    print(f'Sum: {sum(tall)}')
    print(f'Antall: {len(tall)}')

    for x in tall:
        print(f'{x}', end=' ')