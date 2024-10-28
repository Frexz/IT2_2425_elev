# I en klasse i Python må vi alltid ha med en metode som kalles konstruktøren (__init__). Denne metoden
# kalles automatisk når et objekt fra en klasse opprettes og sørger for at objektet får verdier til sine attributter
# og at alle metoder blir definert.
class Person:
    # Her har kontruktøren tre parametere: obligatoriske parameteren self, i tillegg til navn og bosted.
    # Argumenter som puttes inn i kontruktøren blir verdiene til objektvariablene navn og bosted.
    def __init__(self, navn: str, bosted: str) -> None:
        self.navn = navn
        self.bosted = bosted
    
    def hils(self):
        print(f"Hei, jeg er {self.navn} og kommer fra {self.bosted}.")

# Her opprettes Person-objekter og legges til en liste. Person-objektene opprettes med argumenter for navn og bosted
# som sendes til konstruktøren. Objektene legges til en liste og er tre unike objekter. Alle har de samme attributtene og metodene
# men verdiene deres er forskjellige.
personer = []
personer.append(Person("Elise", "Bergen"))
personer.append(Person("Frida", "Stavanger"))
personer.append(Person("Gustav", "Oslo"))

# Dette gjør at vi kan få en unik personlig hilsen for hvert objekt.
for person in personer:
    person.hils()
    print(person.navn, person.bosted)