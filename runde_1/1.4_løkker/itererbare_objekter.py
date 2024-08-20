# Et itererbart objekt i Python er et objekt som kan levere ett og ett av sine elementer om gangen.
# for-løkker brukes for å iterer/gå gjennom itererbare objekter. Slik objekter er tekststrenger (str),
# lister (list) og tallrekker (range).

# Iterer over en streng
for bokstav in 'ord':
    print(bokstav)

# Iterer over en liste
elever = ['Lise', 'Torill', 'Knut', 'Per', 'Oscar']
for navn in elever:
    print(navn)

# range-eksempler
# Funksjonen range tar tre argumenter: start, stop og step. start er tallet sekvensen starter med, stop er tallet
# sekvensen går opp til, men ikke inkludert, og step er hvor mye tallet økes eller minskes med hver gang. 
# Bruker man ingen argumenter for start er start = 0 og hvis ingen argumenter for step blir oppgit er step = 1
# I eksemplene brukes list() kun for å visualisere tallsekvensen fra range-funksjonen
print(list(range(10)))
print(list(range(1, 10)))
print(list(range(10, 1)))
print(list(range(1, 10, 2)))
print(list(range(10, 1, -2)))

