# break og continue kan brukes for å endre flyten i en løkke.
# break gjør at løkka avsluttes tidlig og alle variabler beholder verdiene de hadde
# da løkka ble avbrutt.
# continue avbryter kun gjeldene gjennomkjøring/runde og går videre til neste.

# break
teller = 10
while True: # dette er i utgangspunktet en evig løkke
    print(teller)
    teller -= 2
    if teller < 2:
        break # men vi kan komme oss ut av den ved å bruke break

# continue
# Skriv ut alle partall mellom 1 og 10 bortsett fra 6.
for i in range(10, 1, -2):
    if i == 6:
        continue # hopper over resten hvis tallet er 6
    print(i)
else:
    print('Ferdig!')    # else-blokken på slutten av en løkke utføres når løkken er slutt

