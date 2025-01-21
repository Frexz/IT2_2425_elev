import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 400, 600
FPS = 24

class Bilde(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Leser inn bilde og omgjør til samme format som self.screen
        self.image = pg.image.load("lib/ninja.png").convert_alpha()
        # Skalerer bildet om nødvendig
        self.image = pg.transform.scale(
            self.image, (self.image.get_width(),
                         self.image.get_height()))
        # Sprite-objektet må ha et rect-attributt
        self.rect = self.image.get_rect()
        # Plasseres i midten på skjermen
        self.rect.x = (WIDTH - self.rect.width) / 2
        self.rect.y = (HEIGHT - self.rect.height) / 2

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.bilde = Bilde()
        self.all_sprites.add(self.bilde)
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("white")
        self.all_sprites.draw(self.screen)
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