def main():
    kart = [['.' for x in range(10)] for x in range(10)]
    skriv_ut(kart)
    hent_input(kart)
    skriv_ut(kart)

def skriv_ut(kart):
    for rad in kart:
        for kol in rad:
            print(kol, end='   ')
        print()

def hent_input(k):
    try:
        x = int(input('Skriv inn x-koordinatet til skatten (1 - 10): '))
        y = int(input('Skriv inn y-koordinatet til skatten (1 - 10): '))

        k[x - 1][y - 1] = 'X'
    except IndexError:
        print('Vennligst skriv inn heltall mellom 1 og 10')
        hent_input(k)
    except ValueError:
        print('Vennligst skriv inn heltall mellom 1 og 10')
        hent_input(k)

main()