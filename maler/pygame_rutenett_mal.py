import pygame as pg
from pygame.locals import *

SQUARE = 30
ROWS, KOLS = 20, 20
WIDTH, HEIGHT = KOLS*SQUARE, ROWS*SQUARE
FPS = 60

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Rutenett-mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()

        self.grid = []
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("white")
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        pg.display.update()
    
    def draw_grid(self):
        for i in range(KOLS):
            pg.draw.line(self.screen, "black", (i*SQUARE, 0), (i*SQUARE, HEIGHT))

        for i in range(ROWS):
            pg.draw.line(self.screen, "black", (0, i*SQUARE), (WIDTH, i*SQUARE))

        pg.draw.line(self.screen, "black", (WIDTH, 0), (WIDTH, HEIGHT))

    
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