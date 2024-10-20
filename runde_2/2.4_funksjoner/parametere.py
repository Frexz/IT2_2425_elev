# Parametere er variable som kan ta imot verdier som sendes inn til funksjonen, og dermed brukes 
# inni funksjonen. Rekkefølgen på parameterene angir rekkefølgen verdiene skal sendes inn til funksjonen.
def hils(navn, bosted, år):
    print(f"Hei, {navn} som bor i {bosted} og er født i {år}.")

# Verdien man sender inn til funksjonen kalles argumenter. I Python står man fritt til å velge datatypen
# til argumentene, men dette kan medføre at funksjonen ikke fungere helt slik den skal.
hils("Fredrik", "Mandal", 1992)

# Å bruke stjerneoperatøren foran en parameter gjør at funksjonen kan motta så mange verdier som mulig
# og alle verdiene blir pakket inn i en tuppel.
def hils1(*info):
    print(f"Hei, dette er informasjonen om deg: {info}")

hils1("Fredrik", "Mandal", 1992, 32, "Lærer")

# Å bruke dobbel-stjerne foran en parameter gjør at alle nøkkelordargumenter pakkes inn i en ordbok (dictionary).
def hils2(**key_info):
    if not key_info:
        print("Ingen opplysninger om denne personen.")
    else:
        for nøkkel, verdi in key_info.items():
            print(f'{nøkkel}: {verdi}')

# Alle parameterne oppgis som nøkkelordargummenter (nøkkel-verdi-par)
hils2(navn="Fredrik", bosted="Mandal", år=1992, erLærer = True)

# En funksjon kan også defineres med type hint, der man oppgir datatypen til hver parameter og funksjonen returverdi.
# Dette er bare hint til brukeren og endrer ikke datatypen om brukeren skulle ignorere hintet.
def hils3(navn: str, bosted: str, år: int) -> None:
    print(f"Hei, {navn} som bor i {bosted} og er født i {år}.")

hils3("Fredrik", "Mandal", 1992)

