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
        self.vy = 5
    
    # Håndterer kontinuerlig trykk
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 5
        if keys[pg.K_RIGHT]:
            self.rect.x += 5
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.ball = Ball()
        self.all_sprites.add(self.ball)
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            # Håndterer enkle trykk
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.ball.rect.x -= 10
                elif event.key == pg.K_RIGHT:
                    self.ball.rect.x += 10
    
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