# Polymorfi betyr at ting kan opptre i flere former.
# Nedenfor er fire klasser der alle har en metode 'hils', men innholdet i hver metode er forskjellig.
# Hund, Katt og Sau arver fra klassen Dyr. Hvis man har et Hund-objekt, hvordan vet jeg hvilken av 'hils' metodene
# som kjører når man kaller på den?
# Det er metoden i objektets subklasse som blir kalt på. 

class Dyr:
    def __init__(self, navn):
        self.navn = navn
    
    def hils(self):
        print(f"Jeg heter {self.navn} og er en {self.__class__.__name__.lower()}")

class Hund(Dyr):
    def __init__(self, navn):
        super().__init__(navn)
    
    # super().hils() kaller på hils-metoden i superklassen, men vi har lagt til "Voff!" for denne subklassen.
    def hils(self):
        print(f"Voff! ", end="")
        super().hils()

class Katt(Dyr):
    def __init__(self, navn):
        super().__init__(navn)
    
    # super().hils() kaller på hils-metoden i superklassen, men vi har lagt til "Mjau!" for denne subklassen.
    def hils(self):
        print(f"Mjau! ", end="")
        super().hils()

class Sau(Dyr):
    def __init__(self, navn):
        super().__init__(navn)

    # super().hils() kaller på hils-metoden i superklassen, men vi har lagt til "Bæ!" for denne subklassen.
    def hils(self):
        print("Bæ! ", end="")
        super().hils()

dyreliste = []
dyreliste.append(Hund("Hans"))
dyreliste.append(Katt("Kristin"))
dyreliste.append(Sau("Shaun"))

# hils-metoden kalles på for hvert dyr, men siden hvert dyr er en forskjellig subklasse, blir innholdet i hils-metoden
# annerledes for hvert dyr.
for dyr in dyreliste:
    dyr.hils()