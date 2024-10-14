# zip-funksjonen kan hente informasjon fra to eller flere lister samtidig, og binder
# elementene samme som tuppel-par.

planeter = ["Merkur", "Venus", "Jorden", "Mars"]
fra_solen = [1, 2, 3, 4]

kombinert = zip(planeter, fra_solen)
print(kombinert)
print(*kombinert)

# Dette brukes ofte i løkker der vi ønsker å håndtere informasjon fra flere lister samtidig
for planet, nummer in zip(planeter, fra_solen):
    print(f'{planet} er den {nummer}. planeten fra solen.')