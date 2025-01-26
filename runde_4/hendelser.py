import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 600, 400
FPS = 60

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.tast = ""
        self.klikk = 0
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                self.tast = pg.key.name(event.key)
            elif event.type == pg.MOUSEBUTTONUP:
                self.klikk += 1
    
    def update(self):
        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("darkgrey")
        self.all_sprites.draw(self.screen)

        font = pg.font.SysFont("Arial", 20)
        text1 = font.render("Klikk på musa eller trykk en tast", True, "black")
        text2 = font.render(f"Du trykket på en tast: {self.tast}", True, "black")
        text3 = font.render(f"Du har klikket på musa {self.klikk} ganger.", True, "black")

        self.screen.blit(text1, (100, 50))
        self.screen.blit(text2, (100, 150))
        self.screen.blit(text3, (100, 250))

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