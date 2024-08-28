# Sletting i for-løkker - siden sletting fører til at de andre elementene i listen
# skifter indeks kan sletting i for-løkker skape problemet slik som vist i eksempelet under.

# FEIL - hver gang 3 fjernes flytter alle elementene etter det fjernede elementet seg mot venstre
# men for-løkken fortsetter som før så noen av tallene hoppes over.
tall = [1, 2, 3, 3, 3, 4, 3, 3, 3, 5, 3, 3, 6, 3]
for t in tall:
    if t == 3:
        tall.remove(t)
print(tall)

# FEIL - IndexError: list index out of range. Oppstår fordi når vi fjerner elementer blir listen 
# mindre, mens for-løkken fortsetter like langt som listens opprinnelige lengde.
# tall = [1, 2, 3, 3, 3, 4, 3, 3, 3, 5, 3, 3, 6, 3]
# for i in range(len(tall)):
#     if tall[i] == 3:
#         tall.pop(i)
# print(tall)

# Man kan unngå disse feilene ved å fjerne elementer ved å gå gjennom listen bakfra, listebygging,
# eller while-løkker

# RIKTIG - går gjennom listen bakfra. Mer at len(tall) - 1 gir indeksen til siste element.
tall = [1, 2, 3, 3, 3, 4, 3, 3, 3, 5, 3, 3, 6, 3]
for i in range(len(tall) - 1, -1, -1):
    if tall[i] == 3:
        tall.pop(i)
print(tall)

# RIKTIG - listebygging. Filtrerer ut alle tall som er 3
tall = [1, 2, 3, 3, 3, 4, 3, 3, 3, 5, 3, 3, 6, 3]
tall = [x for x in tall if x != 3]
print(tall)

# RIKTIG - while-løkke. Fjerner 3 fra listen så lenge 3 eksisterer i listen
tall = [1, 2, 3, 3, 3, 4, 3, 3, 3, 5, 3, 3, 6, 3]
while 3 in tall:
    tall.remove(3)
print(tall)
