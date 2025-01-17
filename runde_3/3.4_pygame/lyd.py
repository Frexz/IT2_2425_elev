import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 600, 200
FPS = 60

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Last inn lydfiler
        self.PING = pg.mixer.Sound("lib/ping.mp3")
        self.PONG = pg.mixer.Sound("lib/pong.mp3")

        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = (HEIGHT - self.rect.height)/2
        pg.draw.circle(self.image, pg.Color(158, 81, 196), (25, 25), 25)
        self.vx = 5

    def update(self):
        self.rect.x += self.vx
        # Sjekker om ballen treffer kanten
        if self.rect.left < 0 or self.rect.right > WIDTH:
            # Snu fartsretning
            self.vx *= -1

            # Spill av lyd
            if self.vx < 0:
                self.PING.play() # Traff høyre kant
            else:
                self.PONG.play() # Traff venstre kant

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