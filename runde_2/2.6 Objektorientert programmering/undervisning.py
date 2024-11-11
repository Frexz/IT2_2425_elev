class Bibliotek():
    def __init__(self):
        self.bøker = []

    def legg_til(self, bok):
        self.bøker.append(bok)
    
    def fjern_bok(self, bok):
        self.bøker.remove(bok)

class Bok():
    def __init__(self, tittel, forfatter):
        self.tittel = tittel
        self.forfatter = forfatter

bib = Bibliotek()
bib.legg_til(Bok("Ringenes Herre: Atter en konge", "J.R.R. Tolkien"))
