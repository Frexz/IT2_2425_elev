import pygame as pg
from pygame.locals import *
from random import randint, choice

WIDTH, HEIGHT = 400, 600
FPS = 60

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20, 20), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, "red", (10, 10), 10)
        self.rect.center = (WIDTH/2, 50)
        self.vx = choice((-1, 1)) * 3
        self.vy = 1
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.left <= 0:
            self.rect.left = 0
            self.vx *= -1
        
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.vx *= -1

        if self.rect.top <= 0:
            self.rect.top = 0
            self.vy *= -1

        # Game Over
        if self.rect.bottom >= HEIGHT:
            app.gameOver = True

class Padde(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((150, 20))
        self.rect = self.image.get_rect()
        pg.draw.rect(self.image, "blue", (0, 0, 150, 20))
        self.rect.center = (WIDTH/2, HEIGHT - 50)

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 5
        if keys[pg.K_RIGHT]:
            self.rect.x += 5

        if self.rect.left <= 0:
            self.rect.left = 0
        
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
        


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
        self.padde = Padde()
        self.all_sprites.add(self.padde)
        self.poeng = 0
        self.gameOver = False
        self.font = pg.font.SysFont("Comic Sans", 14)
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        hits = pg.sprite.spritecollide(self.padde, self.all_sprites, False)
        for hit in hits:
            if isinstance(hit, Ball):

                # Sjekk topp eller side eller overlapp
                if hit.rect.bottom <= self.padde.rect.top + 5:
                    hit.vy *= -1
                    hit.rect.top = self.padde.rect.top - hit.rect.height
                    self.poeng += 1
                    self.all_sprites.add(Ball())

                elif hit.rect.centerx <= self.padde.rect.left or hit.rect.centerx >= self.padde.rect.right:
                    hit.vx *= -1
                
                else:
                    hit.vy *= -1
                    hit.rect.top = self.padde.rect.top - hit.rect.height
                    self.poeng += 1
                    self.all_sprites.add(Ball())
        
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("lightgrey")

        tekst = f"Poeng: {self.poeng}"
        tekst_surface = self.font.render(tekst, True, "black")
        self.screen.blit(tekst_surface, (10, 10))

        if self.gameOver:
            tekst = "GAME OVER"
            font = pg.font.SysFont("Consolas", 30)
            tekst_surface = font.render(tekst, True, "red")
            self.screen.blit(tekst_surface, ((WIDTH - tekst_surface.get_rect().width)/2, (HEIGHT - tekst_surface.get_rect().height)/2))

        self.all_sprites.draw(self.screen)
        pg.display.update()
    
    def run(self):
        while self.running:
            self.handle_events()
            if not self.gameOver:
                self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()

if __name__ == "__main__":
    app = App()
    app.run()