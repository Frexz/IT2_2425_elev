# Tupler (og all andre datetyper av type Iterable som lister, strenger osv.) støtter
# tilordning av verdier til flere variabler samtidig.
farger = ("rød", "grønn", "blå")
r, g, b = farger
print(r)
print(g)
print(b)

# Vi sier at tuppelet pakkes ut.

# Eksempel - Bytt verdi på variabler uten midlertidig variabel
a = 4
b = 5
print(f'a = {a} og b = {b}')
b, a = a, b
print(f'a = {a} og b = {b}')