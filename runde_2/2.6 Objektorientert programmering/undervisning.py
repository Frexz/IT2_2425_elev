class Dyr():
    antall = 0

    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
        Dyr.antall += 1

    def introduser(self):
        print(f"Jeg heter {self.navn} og er {self.alder} år gammel.")

    @classmethod
    def gi_antall(cls):
        print(f"Det er {cls.antall} dyr i dyrehagen.")

class Katt(Dyr):
    def __init__(self, navn, alder):
        super().__init__(navn, alder)
        self.antall_liv = 9

    def introduser(self):
        print("Mjau!", end=" ")
        super().introduser()

class Hund(Dyr):
    def __init__(self, navn, alder):
        super().__init__(navn, alder)

    def introduser(self):
        print("Voff!", end=" ")
        super().introduser()

hund = Hund("Fido", 7)
Dyr.gi_antall()

