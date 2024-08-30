# try-except - Dette programmet ville ha gitt en kjøretidsfeil om brukeren hadde skrevet inn
# noe som ikke var et heltall. Dette fordi ingenting annet enn tall kan brukes i int()-funksjonen.
# Med en try-except blokk kan vi bestemme hva som skjer når en slik feil oppstår i stedet for at
# programmet avbrytes. Hvis det oppstår en slik feil i koden nedenfor får brukeren beskjed om at
# det den skrev inn ikke er et heltall.
bruker_input = input('Skriv inn et heltall: ')

try:
    tall = int(bruker_input)
    print(f'Du skrev inn {str(tall)}')
except ValueError:
    print(f'{bruker_input} er ikke et heltall')