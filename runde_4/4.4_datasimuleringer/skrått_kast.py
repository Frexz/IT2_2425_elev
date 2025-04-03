import pygame as pg
from pygame.locals import *
import numpy as np

WIDTH, HEIGHT = 1000, 600
NULLNIVÅ = 500
MAX_POWER = 20
GRAVITY = 9.81
FPS = 60

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20, 20), pg.SRCALPHA)
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, "white", (10, 10), 10)
        self.rect.center = (50, NULLNIVÅ)
        self.angle = np.radians(45)
        self.power = 0
        self.vx = 0
        self.vy = 0
    
    def update(self):
        if app.is_moving:
            self.rect.centerx += self.vx
            self.rect.centery -= self.vy

            self.vy = self.vy - GRAVITY*(1/FPS)

            if self.rect.centery > NULLNIVÅ:
                app.is_moving = False
            
            if self.rect.centerx > WIDTH:
                app.is_moving = False
                self.rect.center = (50, NULLNIVÅ)
        else:
            keys = pg.key.get_pressed()
            if keys[pg.K_UP]:
                self.angle = min(np.radians(90), self.angle + np.radians(0.3))
            elif keys[pg.K_DOWN]:
                self.angle = max(0, self.angle - np.radians(0.3))
            elif keys[pg.K_LEFT]:
                self.power = max(0, self.power - 0.3)
            elif keys[pg.K_RIGHT]:
                self.power = min(MAX_POWER, self.power + 0.3)
            
            self.vx = self.power*np.cos(self.angle)
            self.vy = self.power*np.sin(self.angle)
        
        

        

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Golf")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.ball = Ball()
        self.all_sprites.add(self.ball)
        self.is_moving = False
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.is_moving = True
    
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("lightblue")
        pg.draw.rect(self.screen, "darkgreen", (0, NULLNIVÅ, WIDTH, HEIGHT - NULLNIVÅ))
        
        if not self.is_moving:
            pg.draw.line(self.screen, "red", self.ball.rect.center, (self.ball.rect.centerx + 50*np.cos(self.ball.angle), self.ball.rect.centery - 50*np.sin(self.ball.angle)), 3)
        
        text = f"Angle: {round(np.degrees(self.ball.angle))}{chr(176)}"
        font = pg.font.SysFont("Arial", 30)
        text_surface = font.render(text, True, "black")
        self.screen.blit(text_surface, (25, HEIGHT - 65)) 

        pg.draw.rect(self.screen, "red", (200, HEIGHT - 65, (self.ball.power/MAX_POWER)*200, 30))
        pg.draw.rect(self.screen, "black", (200, HEIGHT - 65, 200, 30), 3)       

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