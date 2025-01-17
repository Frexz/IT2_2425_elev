import pygame as pg
from pygame.locals import *
import pytweening as tween

WIDTH, HEIGHT = 200, 600
FPS = 60

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, "green", (25, 25), 25)
        self.rect.x = (WIDTH - self.rect.width)/2
        self.rect.y = self.rect.height 
        self.bilder = 2*FPS
        self.teller = 0
    
    def update(self):
        self.teller += 1
        avstand = HEIGHT - self.rect.height

        # Tween i 2 sekunder
        if self.teller <= self.bilder:
            y = avstand * tween.easeOutBounce(self.teller / self.bilder)
        # La ballen ligge nede i 1 sekund
        elif self.teller <= FPS * 3:
            y = avstand
        # Start på nytt etter 3 sekunder
        else:
            y = 0
            self.teller = 0
        
        self.rect.y = y

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