import math

class Person():
    # Konstruktøren
    def __init__(self, navn, gatenavn, postkode, by, tlf):
        self.navn = navn
        self.gatenavn = gatenavn
        self.postkode = postkode
        self.by = by
        self.telefonnummer = tlf
    
    def skriv_adresse(self):
        print(self.navn)
        print(self.gatenavn)
        print(f'{self.postkode}\t{self.by}')
        print(self.telefonnummer)

class Sirkel():
    def __init__(self, r):
        self.radius = r
    
    def omkrets(self):
        return round(2*math.pi*self.radius, 2)
    
    def areal(self):
        return round(math.pi*self.radius**2, 2)
    
    def __str__(self):
        return f"Radius: {self.radius}\nOmkrets: {self.omkrets()}\nAreal: {self.areal()}\n"

sirkler = []

for i in range(1, 11):
    sirkler.append(Sirkel(i))

for sirkel in sirkler:
    print(sirkel)
