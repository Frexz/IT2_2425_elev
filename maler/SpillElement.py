import pygame as pg

# Alle elementer som arver fra Sprite må ha attributtene image og rect, i tillegg til en update-metode
# Lurt å endre klassenavn så det er mer naturlig i programmet ditt.
# self.image - skal være et Surface-objekt som man kan tegne på.
# self.rect - posisjonsinformasjon Surface-objectet (som er et rektangel). Rect-objektet har
# x og y attributter, width og heigh, i tillegg til center, top, bottom, left og right.
# update-metodene skal fortelle hvordan objektet skal endre seg når update kalles.
# Man må også tegne elementet i kontruktøren med pg.draw der self.image er tegneflaten.
class SpillElement(pg.sprite.Sprite):
    def __init__(self):
        super.__init__()
        self.image = pg.Surface((40, 40), pg.SRCALPHA)
        self.rect = self.image.get_rect()
    
    def update(self):
        pass