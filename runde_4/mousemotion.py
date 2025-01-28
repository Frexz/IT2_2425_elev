import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 400, 400
FPS = 60

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Mousemotion")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.pos = (WIDTH/2, HEIGHT/2)
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEMOTION:
                self.pos = event.pos
    
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("darkgrey")
        self.all_sprites.draw(self.screen)
        pg.draw.line(self.screen, "black", (WIDTH/2, HEIGHT/2), self.pos, 3)
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