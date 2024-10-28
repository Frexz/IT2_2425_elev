# Vi definerer en klasse ved å bruke det reserverte ordet 'class' etterfulgt av et navn, parenteser og kolon.
# Dette navnet bør beskrive tingen klassen representerer og det er god praksis å ha stor forbokstav på dette navnet.
# Alt som er innfrykket etter dette tilhører klassedefinisjonen.
class Hund():
    # Alle klasser har en metode som kalles konstruktøren. Konstruktøren er funksjonen som oppretter klassen
    # og spesielt setter verdiene til klassens attributter.
    def __init__(self, navn, alder):
        # En klasse har attributter, eller variabler, som knyttes til et objekt av den klassen.
        # Disse får en verdi i konstruktøren.
        self.navn = navn
        self.alder = alder
    
    # En klasse har også metoder, eller funksjoner, som knyttes til et objekt av den klassen.
    # Alle metoder, inkludert konstruktøren, må ha en parameter som heter self. Alle attributter må også begynne med
    # self etterfulgt av punktum og et variabelnavn.
    def bjeff(self):
        return f"{self.navn} sier Voff!"
    
    def info(self):
        return f"{self.navn} er en {self.alder}-år gammel {self.__class__.__name__.lower()}"

# For å opprette et objekt av en klasse, også kalt en instans, lager man en variabel som refererer til dette objektet
# og setter det lik klassenavnet med nødvendig parametere inni parenteser. Hvordan konstruktøren er skrevet avgjør
# hvilke parametere som skal med.

# Nedenfor er hund1 og hund2 fra samme klasse, men to forskjellige objekter.
hund1 = Hund("Trofast", 5)
hund2 = Hund("Kira", 10)

# For å referere til attributter og kalle på metoder bruker man punktum-notasjon.
print(hund1.navn)
print(hund1.alder)
print(hund1.bjeff())
print(hund1.info())

# Man kan også endre på attributter ved å sette attributtet lik en ny verdi, men vi skal se senere
# en bedre måte å gjøre dette på.
print(hund2.bjeff())
hund2.navn = "Max"
print(hund2.bjeff())