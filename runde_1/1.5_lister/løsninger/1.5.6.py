sjakkbrett = []
farger = ['hvit', 'svart']


for i in range(8):
    rad = []
    for j in range(8):
        if i % 2 == 0:
            rad.append(farger[j % 2])
        else:
            rad.append(farger[(j + 1) % 2])
    sjakkbrett.append(rad)

for rad in sjakkbrett:
    for rute in rad:
        print(f'{rute:7}', end='')
    print()
    print()