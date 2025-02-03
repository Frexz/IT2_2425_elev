import pygame as pg
from pygame.locals import *
from random import randint, choice

WIDTH, HEIGHT = 400, 600
FPS = 60

class Ball(pg.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pg.Surface((20, 20), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.color = color
        pg.draw.circle(self.image, self.color, (10, 10), 10)
        self.rect.centerx = randint(0, WIDTH)
        self.rect.centery = randint(0, HEIGHT)
        self.vx = choice([-1, 1])
        self.vy = choice([-1, 1])
    
    def update(self):
        self.rect.centerx += self.vx
        self.rect.centery += self.vy

        if self.rect.left <= 0:
            self.vx *= -1
            self.rect.left = 0
        
        if self.rect.right >= WIDTH:
            self.vx *= -1
            self.rect.right = WIDTH
        
        if self.rect.top <= 0:
            self.vy *= -1
            self.rect.top = 0

        if self.rect.bottom >= HEIGHT:
            self.vy *= -1
            self.rect.bottom = HEIGHT

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
        self.running = True
        self.red_balls = pg.sprite.Group()
        self.green_balls = pg.sprite.Group()

        for i in range(10):
            if i % 2 == 0:
                self.green_balls.add(Ball("green"))
            else:
                self.red_balls.add(Ball("red"))
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        self.red_balls.update()
        self.green_balls.update()
    
    def draw(self):
        self.screen.fill("black")
        self.red_balls.draw(self.screen)
        self.green_balls.draw(self.screen)
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