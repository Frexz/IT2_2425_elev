# Med arv trenger man ikke lage fullstendig nye klasser for hvert eneste type objekt.
# Vi kan samle felles attributter og metoder i en samleklasse (Dyr) og arve fra den.
# Når man arver, så arver man alle metoder og attributter. Disse blir alstå tilgjengelige for klassen som arver.
class Dyr:
    def __init__(self, navn):
        self.navn = navn

    def hils(self):
        print(f"Hei, jeg heter {self.navn} og er en {self.__class__.__name__.lower()}.")

# For å arve fra en klasse putter man klassenavnet man ønsker å arve fra i parentesene når man definerer klassen
class Hund(Dyr):
    # Alle klasse skal ha en konstruktør. For å kalle på konstrukøren til klassen man arver fra (superklassen) bruker
    # man funksjonen super() etterfulgt av metoden man ønsker å kalle. Konstruktøren til superklassen må kalles på
    # for at denne klassen skal få dens attributter og metoder.
    def __init__(self, navn):
        super().__init__(navn)

class Katt(Dyr):
    def __init__(self, navn):
        super().__init__(navn)

dyreliste = [Hund("Hans")]
dyreliste.append(Katt("Kristin"))

for dyr in dyreliste:
    dyr.hils()

# Objekter fra klassen Hund er først fremst av typen Hund, men også av typen Dyr pga. arv,
# men er ikke av typen Katt.
# Objekter fra klassen Katt er først fremst av typen Katt, men også av typen Dyr pga. arv,
# mer er ikke avv typen Hund.