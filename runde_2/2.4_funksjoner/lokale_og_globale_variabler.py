# Variabler som opprettes innenfor en kodeblokk, som i for
# eksempel en funskjon, er lokale, og eksisterer bare inni
# kode-blokken.
def eksempel1():
    lokal_var = "Jeg er lokal"
    print(f'Inni funksjonen, lokal_var: {lokal_var}')
    print(f'Inni funksjonen, global_var: {global_var}')

# Variabler definert utenfor en kode-blokk, i hovedprogrammet,
# er globale variabler og kan referes til både utenfor og innenfor
# andre kode-blokker.
global_var = "Jeg er global"
print(f"Utenfor, før funksjonskallet, global_var: {global_var}")
eksempel1()
# print(lokal_var) <- Denne linjen gir feilmelding da den lokale variabelekn, lokal_var, bare finnen i kode-blokken for funksjonen.

input()

# Hvis man gir en global variabel en ny verdi innenfor en
# kode-blokk, lages det en kopi av variabelen som er lokal.
# Ingen endringen skjer med den opprinnelige globale variablen.
def eksempel2():
    global_var = "Jeg er nå lokal"
    print(f"Inne funksjonen: {global_var}")

global_var = "Jeg er global"
print(f"Utenfor, før funksjonskallet: {global_var}")
eksempel2()
print(f"Utenfor, etter funksjonskallet: {global_var}")

input()

# For å endre en global variabel fra en kode-blokk bruker man
# det reserverte ordet 'global' etterfulgt av navnet på den
# globale variabelen man ønsker å endre
def eksempel3():
    global global_var
    global_var = "Jeg er har blitt endret"
    print(f"Inne funksjonen: {global_var}")

global_var = "Jeg er global"
print(f"Utenfor, før funksjonskallet: {global_var}")
eksempel3()
print(f"Utenfor, etter funksjonskallet: {global_var}")

