import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 600, 200
FPS = 60

class Ball(pg.sprite.Sprite):
    def __init__(self, x, y, color, vx):
        super().__init__()
        self.image = pg.Surface((20, 20), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        self.radius = 10
        pg.draw.circle(self.image, color, (self.radius, self.radius), self.radius)
        self.rect.center = (x, y)
        self.vx = vx
        
    
    def update(self):
        self.rect.x += self.vx

        if self.rect.left <= 0:
            self.vx *= -1
            self.rect.left = 0
        
        if self.rect.right >= WIDTH:
            self.vx *= -1
            self.rect.right = WIDTH
    
    def collide(self):
        self.vx *= -1
        self.rect.x += self.vx

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.ball1 = Ball(100, HEIGHT/2, "blue", 1)
        self.ball2 = Ball(500, HEIGHT/2, "red", -1)
        self.all_sprites.add(self.ball1)
        self.all_sprites.add(self.ball2)
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        if pg.sprite.collide_circle(self.ball1, self.ball2):
            self.ball1.collide()
            self.ball2.collide()

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