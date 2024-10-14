# Ordbøker, eller dictionaries, er en samling av nøkkel-verdi-par, der hver
# nøkkel må være unik. Dette er en datastruktur forskjellig fra lister der man
# bruker en nøkkel, i stedet for en indeks, for å få tilgang til en verdi.
# Rekkefølgen på nøkkel-verdi-par i en ordbok har da ingenting å si.

# Ordbøker opprettes med krøllparenteser etterfulgt av "nøkkel": verdi.
# En nøkkel er alltid en streng og er unik.
ordbok = {"fornavn": "Fredrik", "alder": 32, "poststed": "Mandal"}

print(type(ordbok)) # type: dict
print(ordbok)
print(ordbok["poststed"]) # Verdier hentes ved hjelp av nøkler
ordbok["fornavn"] = "Knut" # Endrer verdien til fornavn
print(ordbok)
ordbok["fødselsår"] = 1992 # Legger til en ny verdi hvis nøkkelen ikke finnes allerede
print(ordbok)
del ordbok["poststed"] # Slette nøkkel-verdi-paret med "poststed" som nøkkel
print(ordbok)

print(*ordbok.keys()) # keys() gir en samling med nøklene i ordboken
print(*ordbok.values()) # values() gir en samling med verdiene i ordboken
print(*ordbok.items()) # items() gir en samling med nøkkel-verdi-par fra ordboken
