tabell = range(1, 101, 2) # Alle oddetall mellom 1 og 100
antall_kolonner = 15
teller = 0

for tall in tabell:
    # Hvis runden på løkken er lik antall kolonner lages en ny rad
    if teller % antall_kolonner == 0:
        print() # ny rad
    teller += 1
    # Formateringen :4 etter tall betyr at for hvert tall skal width=4
    # Verdien til end for print-funksjonen er vanligvis '\n' altså ny linje. Her overstyres den til tom streng.
    # Det vil si at hver gang vi printer får vi ikke ny linje, men skriver bare ut neste tall med width=4.
    print(f'{tall:4}', end='')