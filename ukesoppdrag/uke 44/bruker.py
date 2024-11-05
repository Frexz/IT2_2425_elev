class Bruker():
    def __init__(self, brukernavn, passord):
        self.brukernavn = brukernavn
        self.passord = passord
    
    def bytt_passord(self, gammelt, nytt):
        if gammelt == self.passord:
            self.passord = nytt
        else:
            print("Passordet du oppga er feil.")

    def __str__(self):
        return f"Brukernavn: {self.brukernavn}\nPassord: {self.passord}\n"
    

brukere = {}
brukere["bruker123"] = Bruker("bruker123", "passord")
brukere["kiwi_lover_93"] = Bruker("kiwi_lover_93", "123456789")
brukere["admin"] = Bruker("admin", "admin")

brukernavn = "admin"
print(brukere[brukernavn])
brukere[brukernavn].bytt_passord("admin", "nyttOgSikrerePassord123!")
print(brukere[brukernavn])


