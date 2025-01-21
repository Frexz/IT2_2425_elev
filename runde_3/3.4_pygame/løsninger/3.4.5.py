import pygame as pg
from pygame.locals import *
from random import randint, choice

WIDTH, HEIGHT = 300, 600
FPS = 60

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20, 20), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, [randint(0, 255) for _ in range(3)], (self.rect.width/2, self.rect.height/2), self.rect.width/2)
        self.rect.x = (WIDTH - self.rect.width/2) / 2
        self.rect.y = self.rect.height * 2
        self.vx = choice((-1, 1)) * 3
        self.vy = 1
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.left <= 0:
            self.rect.x = 0
            self.vx *= -1
        
        if self.rect.right >= WIDTH:
            self.rect.x = WIDTH - self.rect.width
            self.vx *= -1

        if self.rect.bottom >= HEIGHT:
            self.kill()

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Multipong")
        self.running = True
        self.timer = pg.time.get_ticks()
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(Ball())
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        if pg.time.get_ticks() - self.timer > 1000:
            self.timer = pg.time.get_ticks()
            self.all_sprites.add(Ball())
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