def kvadrer_siffer(tall):
    resultat = ''
    for siffer in str(tall):
        kvadrat = int(siffer)**2
        resultat += str(kvadrat)
    return int(resultat)

assert kvadrer_siffer(9119) == 811181
assert kvadrer_siffer(765) == 493625
assert kvadrer_siffer(444) == 161616

print("Programmet kjørte uten problemer.")