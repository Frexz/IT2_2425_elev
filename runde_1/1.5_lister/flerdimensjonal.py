### Flerdimensjonale lister - Flerdimensjonale lister er lister som inneholder lister.
# En todimensjonal liste brukes ofte som en tabell-struktur der hvert liste-element i listen
# representerer en rad og hvert element i disse indre listene en kolonne.

# Tabell med kolonnenavn: Oslo, Bergen, Trondheim
# og radnavn: Dag 1, Dag 2, Dag 3.
# Et element i en slik liste refereres til slik: tabell[rad][kolonne]. F.eks:
# temperaturer[1][0] = 21 og er temperaturen i Oslo på Dag 2.
import copy

temperaturer = [
    [22, 20, 18],   # Dag 1
    [21, 20, 20],   # Dag 2
    [17, 17, 17]    # Dag 3
]

# Tabellutskrift
for dag in temperaturer:
    for by in dag:
        print(f'{by:5}', end='')
    print()

# En kopi av en flerdimensjonal liste med copy() gir en ekte kopi av den ytre listen, 
# men der alle de indre listene fortsatt peker på sammme objektene. Dette gjør at endringer
# i en kopi fører til endringer i originalen og kalles en grunn kopi. 
# En ekte kopi, eller en dyp kopi, av en flerdimensjonal
# liste kan lages med funksjonen deepcopy() fra copy-biblioteket.

grunn_kopi = temperaturer.copy()
dyp_kopi = copy.deepcopy(temperaturer)
temperaturer[1][0] = 'Endring'

print(temperaturer) # Endret
print(grunn_kopi)   # Endret
print(dyp_kopi)     # Uendret
