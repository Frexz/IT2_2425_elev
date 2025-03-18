liste = [3, 4, 2, 3, 1, 1, 1, 0, 2]
ordbok = {"fornavn": "Fredrik", "etternavn": "Pettersen", "alder": 32}
tuppel = (3, 4, 5)
sett = {"Fredrik", "Ariana", "Christine", "Sivert", "Kristine", "Ariana", "Sigvart"}


A = {2, 3, 5}
B = {1, 2, 4, 5}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))