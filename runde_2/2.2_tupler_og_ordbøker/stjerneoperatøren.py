# Stjerneoperatøren lar oss blant annet pakke ut Iterables, som tupler, lister, strenger osv.
# når som helst.

# Eksempel - Skrive ut elementene i en liste
planeter = ["Merkur", "Venus", "Jorden", "Mars"]
print(*planeter)

# Med stjerneoperatøren kan man skrive ut hvert element i listen uten
# å bruke en for-løkke.

# Eksempel - Tilordning av variabler
farger = ["rød", "oransje", "gul", "grønn", "blå", "indigo", "fiolett"]
a, b, *c, d = farger
print(a)
print(b)
print(c)
print(d)

# Eksempel - Parametere
def pluss_sammen(*tall):
    print(sum(tall))

# Funksjonen tar ikke imot et bestemt antall parametere
pluss_sammen(1, 2, 3, 4, 5)