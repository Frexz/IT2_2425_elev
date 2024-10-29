# Magiske metoder er spesielle metoder som klasser har.
# Disse kalles ikke på direkte, men kalles på når man utfører bestemte operasjoner på objekter av klassen.
# Magiske metoder starter og slutter med __

class Person():
    # Konstruktøren er en magisk metoder som kalles automatisk når et objekt av klassen opprettes.
    # Konstruktøren lager objektet ved å opprette attributter med verdier og definere metoder.
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    # Streng-metoden kalles automatisk hvis man prøver å bruke print() eller str() på et objekt.
    # Metoden må returnere en streng, som blir strengen som printes.
    def __str__(self):
        return f"Navn: {self.navn}\nAlder: {self.alder}\n"
    
    
    def __eq__(self, value):
        pass
