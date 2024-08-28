from statistics import mean

bruker_input = input('Skriv inn et heltall: ')
heltall = []

while bruker_input != '':
    if bruker_input.isnumeric():
        heltall.append(int(bruker_input))
        print(f'Summen er nå {sum(heltall)}')
    else:
        print(f'{bruker_input} er ikke et heltall.')
    
    bruker_input = input('Skriv inn et heltall: ')

print(heltall)
heltall.remove(max(heltall))
heltall.remove(min(heltall))
print(heltall)
print(f'Gjennomsnitt: {mean(heltall)}')