import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 400, 400
FPS = 60

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((16, 16))
        self.rect = self.image.get_rect()
        pg.draw.rect(self.image, "red", (0, 0, 16, 16))
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    
    def update(self):
        keys = pg.key.get_pressed()

        if keys[K_w]:
            self.rect.y -= 2
        
        elif keys[K_s]:
            self.rect.y += 2
        
        elif keys[K_d]:
            self.rect.x += 2
        
        elif keys[K_a]:
            self.rect.x -= 2


        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))
        
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Sprite Sheet")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("cadetblue3")
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