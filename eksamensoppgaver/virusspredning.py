import pygame as pg
from pygame.locals import *
from random import random

ROWS, KOLS = 30, 30
SQUARE_LENGTH = 20
WIDTH, HEIGHT = KOLS*SQUARE_LENGTH, ROWS*SQUARE_LENGTH
FPS = 60

# Tilstander: "frisk uten immunitet", "smittet", "syk", "død", "frisk med immunitet"
class Person(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((SQUARE_LENGTH, SQUARE_LENGTH))
        self.rect = self.image.get_rect()
        pg.draw.rect(self.image, "lightgrey", (0, 0, SQUARE_LENGTH, SQUARE_LENGTH))
        self.rect.x = x * SQUARE_LENGTH
        self.rect.y = y * SQUARE_LENGTH
        self.condition = "frisk uten"
        # Attributtet holder styr på sykdomsforløpet og holder styr på antall dager siden smitte.
        self.days = 0 
    
    def update(self):
        # Øker sykdomsforløpet for smittede og syke
        if self.condition == "smittet" or self.condition == "syk":
            self.days += 1
        
        # Gjør smittede syke etter tre dager
        if self.days == 4:
            self.condition = "syk"
        
        # Sjekker død for syke personer på dag 5, 6, 7, og 8
        if self.days in [5, 6, 7, 8] and self.condition == "syk":
            self.kill()
        
        # Gjør sykes personer friske etter 8 dager
        if self.days == 8 and self.condition == "syk":
            self.condition = "frisk med"
        
        # Tegner riktig symbol ut fra tilstand
        if self.condition == "frisk uten":
            pg.draw.rect(self.image, "lightgrey", (0, 0, SQUARE_LENGTH, SQUARE_LENGTH))
        elif self.condition == "smittet":
            pg.draw.rect(self.image, "pink", (0, 0, SQUARE_LENGTH, SQUARE_LENGTH))
            pg.draw.line(self.image, "black", (2, 2), (18, 18), 1)
        elif self.condition == "syk":
            pg.draw.rect(self.image, "red", (0, 0, SQUARE_LENGTH, SQUARE_LENGTH))
            pg.draw.line(self.image, "white", (2, 18), (18, 2), 1)
        elif self.condition == "død":
            pg.draw.rect(self.image, "black", (0, 0, SQUARE_LENGTH, SQUARE_LENGTH))
            pg.draw.circle(self.image, "white", (SQUARE_LENGTH/2, SQUARE_LENGTH/2), 2)
        elif self.condition == "frisk med":
            pg.draw.rect(self.image, "darkslategrey", (0, 0, SQUARE_LENGTH, SQUARE_LENGTH))
            pg.draw.circle(self.image, "black", (SQUARE_LENGTH/2, SQUARE_LENGTH/2), 2)
        
        
    
    # Sjekker alle friske personer om de blir smittet
    def infect(self):
        if random() < 0.3 and self.condition == "frisk uten":
            return True
        else:
            return False
    
    # Sjekker død
    def kill(self):
        if random() < 0.01 and self.condition == "syk":
            self.condition = "død"


class Populasjon:
    def __init__(self):
        self.population = []

        for i in range(ROWS):
            rad = []
            for j in range(KOLS):
                # Lager person og plasserer dem i rutenettet.
                # Personen i midten er syk og de rundt er smittet
                middle_x, middle_y = int(ROWS/2) - 1, int(KOLS/2) - 1
                person = Person(i, j)
                if i == middle_x and j == middle_y:
                    person.condition = "syk"
                    person.days = 3
                elif (
                    i == middle_x and j == middle_y - 1 or
                    i == middle_x and j == middle_y + 1 or
                    i == middle_x - 1 and j == middle_y or
                    i == middle_x + 1 and j == middle_y
                ):
                    person.condition = "smittet"
                person.update()
                rad.append(person)
            self.population.append(rad)
    
    # Sprer smitte
    def spread(self):
        # Liste over personer som skal smittes
        infected = []

        # Går gjennom alle personer i rutenettet
        for i in range(ROWS):
            for j in range(KOLS):
                person = self.population[i][j]
                # Hvis personen er syk eller smittet skal alle naboer muligens smittes
                if person.condition == "smittet" or person.condition == "syk":
                    # Sjekker nabo til venstre
                    if j > 0 and self.population[i][j - 1].infect():
                        infected.append(self.population[i][j - 1])
                    
                    # Sjekker nabo til høyre
                    if j < KOLS - 1 and self.population[i][j + 1].infect():
                        infected.append(self.population[i][j + 1])
                    
                    # Sjekker nabo over
                    if i > 0 and self.population[i - 1][j].infect():
                        infected.append(self.population[i - 1][j])
                    
                    # Sjekker nabo under
                    if i < ROWS - 1 and self.population[i + 1][j].infect():
                        infected.append(self.population[i + 1][j])
        
        # Smitter alle personer som er blitt smittet
        for person in infected:
            person.condition = "smittet"
        

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Virusspredning")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.pop = Populasjon() # Endret navn
        self.timer = pg.time.get_ticks() 

        # Legger til alle personer i sprites-gruppen
        for personer in self.pop.population:
            self.all_sprites.add(personer)
        
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        # Oppdateres hvert sekund. Først spres smitten med spread() og deretter oppdateres personene.
        if pg.time.get_ticks() - self.timer > 1000:
            self.timer = pg.time.get_ticks()
            self.pop.spread()
            self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("white")
        self.all_sprites.draw(self.screen)

        # Rutenett, tegnes over Person-objektene.
        for x in range(0, WIDTH, SQUARE_LENGTH):
            pg.draw.line(self.screen, "white", (x, 0), (x, HEIGHT))

        for y in range(0, HEIGHT, SQUARE_LENGTH):
            pg.draw.line(self.screen, "white", (0, y), (WIDTH, y))

        pg.display.update()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()

if __name__ == "__main__":
    app = App()
    app.run()