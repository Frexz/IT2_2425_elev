import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 800, 200
FPS = 60

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("pygame mal")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.lerp_percentage = 0
        self.lerp_dir = 0.01
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        self.all_sprites.update()

        self.lerp_percentage += self.lerp_dir
        if self.lerp_percentage >= 1:
            self.lerp_percentage = 1
            self.lerp_dir = -0.01
        elif self.lerp_percentage <= 0:
            self.lerp_percentage = 0
            self.lerp_dir = 0.01
    
    def draw(self):
        self.screen.fill("lightgrey")
        self.all_sprites.draw(self.screen)

        # Angir standardfarge
        pg.draw.circle(self.screen, "red", (100, 100), 50)
        # Angir farge fra pygame-liste: https://www.pygame.org/docs/ref/color_list.html
        pg.draw.circle(self.screen, "lightpink3", (250, 100), 50)
        # Angir egendefinert farge med rgba
        pg.draw.circle(self.screen, pg.Color(33, 180, 78, 50), (400, 100), 50)
        # Tegner figuren med gjennomsiktig farge
        gjennomsiktig = pg.Surface((100, 100), SRCALPHA)
        pg.draw.circle(gjennomsiktig, pg.Color(170, 180, 78, 230), (50, 50), 50)
        self.screen.blit(gjennomsiktig, (425, 50))
        # lerp-metoden gir en fargeovergang mellom to farger. Her er fargen 70% rødt og 30% gult.
        # Dette kan brukes i animasjoner ved å gradvis endre prosenten slik at man får en myk overgang mellom
        # gult og rødt.
        lerp_color = pg.Color("yellow").lerp(pg.Color("red"), self.lerp_percentage)
        pg.draw.circle(self.screen, lerp_color, (700, 100), 50)
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