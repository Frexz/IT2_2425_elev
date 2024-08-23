bruker_input = input('Skriv inn et heltall, eller "slutt" for å avslutte: ')

# Kjører kodeblokken så lenge bruker_input ikke er lik slutt. Hvis bruker_input blir lik slutt avsluttes løkka og programmet.
while bruker_input != 'slutt':

    if bruker_input.isnumeric():
        print(f'{bruker_input} i titallssystemet er {int(bruker_input):b} binært.')
    else:
        print(f'{bruker_input} er ikke et heltall.')
    
    # Må spørre etter bruker_input på slutten av løkka slik at den har mulighet for å avslutte, og skrive inn flere tall.
    bruker_input = input('Skriv inn et heltall, eller "slutt" for å avslutte: ')