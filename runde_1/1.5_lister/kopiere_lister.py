### Kopiere lister - når man lager en liste lager man egentlig bare en 'peker' på det objektet i minnet
# til datamaskinen. Dette gjør at man må tenke seg om når man kopierer en liste.

a = ['Ole', 'Dole', 'Doffen']
b = a                        
print(f'Liste a: {a}')
print(f'Liste b: {b}')

# b er lik a, men disse er ikke kopier: både a og b peker på samme objekt. Dette kan medføre
# følgende problem.
a.remove('Dole')
print(f'Liste a: {a}')
print(f'Liste b: {b}')

# 'Dole' fjernes fra både a og b, selvom remove() bare ble brukt på a, fordi a og b peker på samme
# objekt.

# Så for å lage en ordentlig kopi kan vi bruke følgende metoder

# for-løkke - bygge en ny liste med å fylle på elementer fra den forrige
c = []
for navn in a:
    c.append(navn)

# copy() - lager en kopi av listen i stedet for en peker til samme liste
c = a.copy()

# Bruker vi '==' til å sammenligne lister er to lister like hvis innholdet er likt
print(f'a == b: {a == b}')
print(f'a == c: {a == c}')

# Bruker vi is-operatoren til å sammenligner er to lister like hvis det er samme listen
print(f'a is b: {a is b}')
print(f'a is c: {a is c}')

# id() - Returnerer listens id. To lister er den samme listen hvis den har lik id
print(f'id(a): {id(a)}')
print(f'id(b): {id(b)}')
print(f'id(c): {id(c)}')