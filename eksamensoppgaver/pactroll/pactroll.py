import pygame as pg
from pygame.locals import *
from random import randint

WIDTH, HEIGHT = 800, 600
FPS = 60

class Troll(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20, 20))
        self.rect = self.image.get_rect()
        pg.draw.rect(self.image, "darkolivegreen4", (0, 0, 20, 20))
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.vx = 0
        self.vy = 0
        self.speed = 2

    def update(self):
        self.rect.x += self.vx * self.speed
        self.rect.y += self.vy * self.speed

        if self.rect.left <= 0:
            self.rect.left = 0
        
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        
        if self.rect.top <= 0:
            self.rect.top = 0
        
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("assets/coin.png")
        self.image = pg.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, WIDTH - self.rect.width)
        self.rect.y = randint(0, HEIGHT - self.rect.height)


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Pactroll")
        self.running = True
        self.all_sprites = pg.sprite.Group()

        self.troll = Troll()
        self.all_sprites.add(self.troll)

        for _ in range(3):
            self.all_sprites.add(Coin())
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.troll.vx = 0
                    self.troll.vy = -1
                elif event.key == pg.K_s:
                    self.troll.vx = 0
                    self.troll.vy = 1
                elif event.key == pg.K_a:
                    self.troll.vx = -1
                    self.troll.vy = 0
                elif event.key == pg.K_d:
                    self.troll.vx = 1
                    self.troll.vy = 0
                    
    
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