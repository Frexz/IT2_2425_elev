# sort()-funksjonen sorterer strenger alfabetisk som standard. 
farger = ['oransje', 'gul', 'grønn']
farger.sort()
print(farger)

# Det er derimot mulig å sortere på andre måter hvis vi angir sorteringsmåten som en funksjon.
# Vi kan f.eks sortere ut fra lengden på ordet.

# Tar inn et ord og returnerer lengden på ordet
def ordlengde(ord):
    return len(ord)

# For å sortere på andre måter bruker man parameteren 'key' og angir måten å sortere på
# ved å oppgi navnet på en funksjon.
farger.sort(key=ordlengde)
print(farger)

# Men man trenger heller ikke definere en funksjon for å angi en funksjon. Man kan bruke
# anonyme funksjoner. Anonyme funksjoner eksisterer kun når de brukes og er deretter borte fra minnet.
# Anonyme funksjoner har følgende syntaks: lambda <parameter>: <uttrykk>, der parameteren er lik elementene som skal sorteres og uttrykket er en funksjon
# som forteller hva det skal sorteres etter.
farger.sort(reverse=True, key=lambda x: len(x))
print(farger) 
