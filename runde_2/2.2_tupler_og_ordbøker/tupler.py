# Dette er et tuppel. En tuppel er forskjellig fra en liste da en tuppel
# ikke kan forandres, men en liste kan. Et tuppel skrives med parenteser
# i stedet for klammer.
farger = ('rød', 'grønn', 'blå')
print(type(farger))
print(farger)

for farge in farger:
    print(f'{farge.upper()}', end='')
print('\n' + farger[1].capitalize())

# Tupler har mange av de samme egenskapene og metodene som lister,
# men man kan ikke på noen som helst måte endre på dem.
# Koden under, for eksempel, gir en feilmelding.
farger[1] = 'gul'