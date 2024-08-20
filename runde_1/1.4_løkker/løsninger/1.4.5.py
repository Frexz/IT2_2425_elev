print('Fibonaccitallene under 1000'.center(40, '-'), end='')
antall_kolonner = 5
teller = 0
første = 0
andre = 1
fibonacci = første + andre

while fibonacci < 1000:
    if teller % antall_kolonner == 0:
        print()
    
    if teller == 0:
        print(f'{første:8}', end='')
        teller += 1
        continue

    if teller == 1:
        print(f'{andre:8}', end='')
        teller += 1
        continue
    
    print(f'{fibonacci:8}', end='')
    første = andre
    andre = fibonacci
    fibonacci = første + andre
    teller += 1
