import pygame as pg
from pygame.locals import *

SQUARE = 50
OFFSET = 10
WIDTH, HEIGHT = 15*(SQUARE + OFFSET), 10*(SQUARE + OFFSET)
FPS = 60

class Mudkip(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("mudkip.png")
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.timer = pg.time.get_ticks()
    
    def update(self):
        if pg.time.get_ticks() - self.timer > 1000:
            self.rect.y += 5
            self.timer = pg.time.get_ticks()

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Sprite-rutenett")
        self.running = True
        self.all_sprites = pg.sprite.Group()

        startx = 2*(SQUARE + OFFSET)
        starty = HEIGHT / 10

        for row in range(5):
            for col in range(11):
                mudkip = Mudkip(startx + col*(SQUARE + OFFSET), starty + row*(SQUARE + OFFSET))
                self.all_sprites.add(mudkip)
    
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