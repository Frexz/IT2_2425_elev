import pygame as pg
from pygame.locals import *
from math import sin, cos

WIDTH, HEIGHT = 800, 800
FPS = 60

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((40, 40), SRCALPHA)
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, "darkgreen", self.rect.center, self.rect.width/2)
        self.angle = 0
        self.orbit_radius = WIDTH/2 - 100
        self.rect.center = (WIDTH/2 + self.orbit_radius*cos(self.angle), HEIGHT/2 + self.orbit_radius*sin(self.angle))
    
    def update(self):
        self.angle += 0.01
        self.rect.center = (WIDTH/2 + self.orbit_radius*cos(self.angle), HEIGHT/2 - self.orbit_radius*sin(self.angle))

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(Ball())
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("#EAE2C6")
        self.all_sprites.draw(self.screen)
        pg.draw.circle(self.screen, "black", (WIDTH/2, HEIGHT/2), WIDTH/2 - 100, 1)
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