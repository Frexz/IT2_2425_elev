import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 600, 600
FPS = 60

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - self.rect.width) / 2
        self.rect.y = (HEIGHT - self.rect.height) / 2
        pg.draw.circle(self.image, "green", (25, 25), 25)
        self.vy = 3
        self.vx = 2
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        # Bunn
        if self.rect.y + self.rect.height >= HEIGHT:
            self.rect.y = HEIGHT - self.rect.height
            self.vy *= -1
        # Topp
        elif self.rect.y <= 0:
            self.rect.y = 0
            self.vy *= -1
        # Venstre
        elif self.rect.x <= 0:
            self.rect.x = 0
            self.vx *= -1
        # Høyre
        elif self.rect.x + self.rect.width >= WIDTH:
            self.rect.x = WIDTH - self.rect.width
            self.vx *= -1
        


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