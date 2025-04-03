import pygame as pg
from pygame.locals import *
import numpy as np
from random import randint

WIDTH, HEIGHT = 1000, 600
NULLNIVÅ = 500
MAX_POWER = 20
HOLE = [800, 830]
GRAVITY = 9.81
FPS = 60

BOUNCE_FACTOR = 0.7
MIN_VY = 2
FRICTION = 0.8

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
        if not app.is_moving:
            self.vx = self.power*np.cos(self.angle)
            self.vy = -self.power*np.sin(self.angle)
        else:
            self.rect.centerx += self.vx
            self.rect.centery += self.vy

            self.vy += GRAVITY * (1/FPS)

            if self.rect.centery >= NULLNIVÅ:
                self.rect.centery = NULLNIVÅ
                self.vy = -self.vy * BOUNCE_FACTOR
                self.vx = self.vx * FRICTION

                if abs(self.vy) < MIN_VY:
                    self.vy = 0
                    self.vx = 0
                    self.power = 0
                    app.is_moving = False
                
                if self.rect.centerx > HOLE[0] and self.rect.centerx < HOLE[1]:
                    app.game_over = True
                    self.kill()

            if self.rect.centerx < 0 and not app.is_moving:
                self.rect.center = (10, NULLNIVÅ)
            elif self.rect.centerx > WIDTH and not app.is_moving:
                self.rect.center = (WIDTH - 10, NULLNIVÅ)

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
        self.count = 0
        self.game_over = False
        self.holding_power = False
    
    def handle_events(self):
        global HOLE
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    self.ball.kill()
                    self.count = 0
                    self.ball = Ball()
                    self.all_sprites.add(self.ball)
                    self.game_over = False

                    hole = randint(100, WIDTH - 30)
                    HOLE = [hole, hole + 30]
            elif event.type == pg.MOUSEMOTION and not self.is_moving and not self.holding_power:
                x, y = event.pos
                dx, dy = x - self.ball.rect.centerx, self.ball.rect.centery - y
                angle = np.arctan2(dy, dx)

                if angle < 0:
                    if dx > 0:
                        angle = 0
                    else:
                        angle = np.pi

                self.ball.angle = min(max(angle, 0), np.pi)
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and not self.is_moving:
                self.holding_power = True
                self.ball.power = 0

            elif event.type == pg.MOUSEBUTTONUP and event.button == 1 and not self.is_moving:
                self.holding_power = False
                self.count += 1
                self.is_moving = True
    
    def update(self):
        if self.holding_power:
            self.ball.power = min(self.ball.power + 0.2, MAX_POWER)
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("lightblue")
        pg.draw.rect(self.screen, "darkgreen", (0, NULLNIVÅ, WIDTH, HEIGHT - NULLNIVÅ))

        # Flag with hole
        pg.draw.ellipse(self.screen, "gray21", (HOLE[0], NULLNIVÅ + 4, HOLE[1] - HOLE[0], 7))
        pg.draw.polygon(self.screen, "firebrick2", [
            (HOLE[1] - 5, NULLNIVÅ - 200),
            (HOLE[1] - 5, NULLNIVÅ - 170),
            (HOLE[1] - 60, NULLNIVÅ - 185)
            ])
        pg.draw.rect(self.screen, "white", (HOLE[1] - 5, NULLNIVÅ - 200, 5, 208))


        if not self.game_over:
            if not self.is_moving:
                pg.draw.line(self.screen, "firebrick2", self.ball.rect.center, (self.ball.rect.centerx + 50*np.cos(self.ball.angle), self.ball.rect.centery - 50*np.sin(self.ball.angle)), 3)
        
        # Power bar
        pg.draw.rect(self.screen, "orange", (200, NULLNIVÅ + 40, (self.ball.power/MAX_POWER) * 200, 30))
        pg.draw.rect(self.screen, "black", (200, NULLNIVÅ + 40, 200, 30), 2)

        # Text
        text = f"Angle: {round(np.degrees(self.ball.angle))}{chr(176)}"
        font = pg.font.SysFont("Arial", 30)
        text_surface = font.render(text, True, "black")
        self.screen.blit(text_surface, (50, NULLNIVÅ + 35))

        text = "POWER"
        font = pg.font.SysFont("Arial", 18)
        text_surface = font.render(text, True, "black")
        self.screen.blit(text_surface, (300 - (text_surface.get_rect().width/2), NULLNIVÅ + 20))

        text = f"{round(self.ball.power, 1)}"
        text_surface = font.render(text, True, "black")
        self.screen.blit(text_surface, (300 - (text_surface.get_rect().width/2), NULLNIVÅ + 45))

        text = f"Shots: {self.count}"
        font = pg.font.SysFont("Arial", 18)
        text_surface = font.render(text, True, "black")
        self.screen.blit(text_surface, (10, 10))

        if self.game_over:
            text = f"CONGRATULATIONS"
            font = pg.font.SysFont("Arial", 48)
            text_surface = font.render(text, True, "tan1")
            self.screen.blit(text_surface, ((WIDTH - text_surface.get_width())/2, (HEIGHT - text_surface.get_height())/2 - 100))

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