class Turgåer:
    def __init__(self, erfaring, vær):
        self.erfaring = erfaring
        self.vær = vær

    def få_råd(self):
        if self.erfaring == "nybegynner" and (self.vær == "regn" or self.vær == "storm"):
            print("Ikke anbefalt nybegynnere i dårlig vær.")
        elif self.erfaring == "ekspert" and self.vær == "klart":
            print("Klar til å dra!")
        else:
            print("Vær forsiktig og planlegg nøye.")

# Tester
t1 = Turgåer("nybegynner", "regn")
t2 = Turgåer("ekspert", "klart")
t3 = Turgåer("erfaren", "storm")

t1.få_råd()
t2.få_råd()
t3.få_råd()