print('   |   1   2   3   4   5   6   7   8   9  10')
print('--------------------------------------------', end='')
for rad in range(1, 11):
    print()
    print(f'{rad:<3}|', end='')
    for kolonne in range(1, 11):
        print(f'{rad*kolonne:4}', end='')
        