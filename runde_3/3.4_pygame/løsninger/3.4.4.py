import pygame as pg
from pygame.locals import *
from random import randint

WIDTH, HEIGHT = 200, 200
FPS = 60

class Tekst(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.tekst = str(randint(1, 3))
        self.font = pg.font.SysFont("Arial", 100)
        self.image = self.font.render(self.tekst, True, "green")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.timer = pg.time.get_ticks()
        self.flag = False
    
    def update(self):
        if pg.time.get_ticks() - self.timer > 750:
            self.timer = pg.time.get_ticks()

            if self.flag:
                self.tekst = str(randint(1, 3))
                self.image = self.font.render(self.tekst, True, "green")
            else:
                self.tekst = ""
                self.image = self.font.render(self.tekst, True, "green")

            self.flag = not self.flag


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(Tekst())
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("black")
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