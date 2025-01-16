import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 600, 500
FPS = 60

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("darkblue")
        self.all_sprites.draw(self.screen)

        # Gress
        pg.draw.rect(self.screen, "darkgreen", (0, 340, 600, 170))
        # Måne
        pg.draw.circle(self.screen, "floralwhite", (480, 100), 50)
        # Hus
        pg.draw.rect(self.screen, "red", (75, 190, 300, 210))
        pg.draw.rect(self.screen, "black", (75, 190, 300, 210), 1)
        # Dør
        pg.draw.rect(self.screen, "burlywood4", (205, 300, 50, 100))
        # Vindu 2
        pg.draw.rect(self.screen, "black", (285, 250, 50, 50))
        # Vindu 1
        pg.draw.rect(self.screen, "gold", (125, 250, 50, 50))
        pg.draw.rect(self.screen, "black", (125, 250, 50, 50), 2)
        pg.draw.line(self.screen, "black", (150, 250), (150, 299), 2)
        pg.draw.line(self.screen, "black", (125, 275), (174, 275), 2)
        # Tak
        pg.draw.polygon(self.screen, "black", [(65, 190), (385, 190), (225, 80)])
        # Pipe
        pg.draw.rect(self.screen, "black", (275, 80, 50, 100))

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