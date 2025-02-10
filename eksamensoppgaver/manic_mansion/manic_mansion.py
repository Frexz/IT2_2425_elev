import pygame as pg
from pygame.locals import *
from random import randint
from numpy import radians, sin, cos

WIDTH, HEIGHT = 700, 400
FREE_ZONE = 75
FPS = 60

print()
class Human(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20, 20))
        self.rect = self.image.get_rect()
        pg.draw.rect(self.image, "darksalmon", (0, 0, 20, 20))
        self.rect.center = (FREE_ZONE / 2, HEIGHT / 2)

        self.speed = 3
        self.is_carrying = False
    
    def update(self):
        if self.is_carrying:
            self.speed = 1
        else:
            self.speed = 3

        keys = pg.key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        
        if keys[K_s]:
            self.rect.y += self.speed
        
        if keys[K_d]:
            self.rect.x += self.speed
        
        if keys[K_a]:
            self.rect.x -= self.speed
        
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

class Block(pg.sprite.Sprite):
    def __init__(self, sprites):
        super().__init__()
        self.image = pg.image.load("assets/brick.png")
        self.rect = self.image.get_rect()

        while True:
            self.rect.x = randint(FREE_ZONE, WIDTH - FREE_ZONE - self.rect.width)
            self.rect.y = randint(0, HEIGHT - self.rect.height)

            if not any(self.rect.colliderect(block.rect) for block in sprites if isinstance(block, Block)):
                break

class Sheep(pg.sprite.Sprite):
    def __init__(self, sprites):
        super().__init__()
        self.image = pg.image.load("assets/sheep.png").convert_alpha()
        self.rect = self.image.get_rect()

        while True:
            self.rect.x = randint(WIDTH - FREE_ZONE, WIDTH - self.rect.width)
            self.rect.y = randint(0, HEIGHT - self.rect.height)

            if not any(self.rect.colliderect(sheep.rect) for sheep in sprites if isinstance(sheep, Sheep)):
                break
        
        self.is_carried = False
    
    def update(self):
        if self.is_carried:
            self.rect.left = app.human.rect.left
            self.rect.bottom = app.human.rect.top
            
        if self.is_carried and self.rect.right <= FREE_ZONE:
            app.score += 1
            app.human.is_carrying = False
            self.kill()
            app.all_sprites.add(Block(app.all_sprites), Sheep(app.all_sprites), Ghost())

class Ghost(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("assets/ghost.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = randint(FREE_ZONE, WIDTH - FREE_ZONE - self.rect.width)
        self.rect.y = randint(0, HEIGHT - self.rect.height)

        self.angle = randint(0, 360)
        self.speed = 2
        self.vx = cos(radians(self.angle))
        self.vy = sin(radians(self.angle))

        if self.vx < 0:
            self.image = pg.transform.flip(self.image, True, False)
    
    def update(self):
        self.rect.x += self.speed * self.vx
        self.rect.y += self.speed * self.vy

        if self.rect.left <= FREE_ZONE or self.rect.right >= WIDTH - FREE_ZONE:
            self.rect.x = max(0, min(self.rect.x, WIDTH - FREE_ZONE - self.rect.width))
            self.vx *= -1
            self.image = pg.transform.flip(self.image, True, False)
        
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))
            self.vy *= -1

                    

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Manic Mansion")
        self.running = True
        self.gameOver = False
        self.score = 0
        self.all_sprites = pg.sprite.Group()

        self.human = Human()
        self.all_sprites.add(self.human)

        for _ in range(3):
            self.all_sprites.add(Block(self.all_sprites))
            self.all_sprites.add(Sheep(self.all_sprites))
            self.all_sprites.add(Ghost())
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def update(self):
        prev_x, prev_y = self.human.rect.x, self.human.rect.y

        self.all_sprites.update()

        collisions = pg.sprite.spritecollide(self.human, self.all_sprites, False)
        for c in collisions:
            if isinstance(c, Block):
                self.human.rect.x, self.human.rect.y = prev_x, prev_y
            elif isinstance(c, Ghost):
                self.gameOver = True
            elif isinstance(c, Sheep) and self.human.is_carrying:
                self.gameOver = True
            elif isinstance(c, Sheep):
                c.is_carried = True
                self.human.is_carrying = True
            
        
    
    def draw(self):
        self.screen.fill("black")
        pg.draw.line(self.screen, "white", (FREE_ZONE, 0), (FREE_ZONE, HEIGHT))
        pg.draw.line(self.screen, "white", (WIDTH - FREE_ZONE, 0), (WIDTH - FREE_ZONE, HEIGHT))
        self.all_sprites.draw(self.screen)

        font = pg.font.SysFont("Consolas", 14)
        text_surface = font.render(f"Score: {self.score}", True, "white")
        self.screen.blit(text_surface, (5, 5))

        if self.gameOver:
            font = pg.font.SysFont("Consolas", 40)
            text_surface = font.render("GAME OVER", True, "green")
            self.screen.blit(text_surface, ((WIDTH - text_surface.get_width()) / 2, (HEIGHT - text_surface.get_height()) / 2))

            font = pg.font.SysFont("Consolas", 14)
            text_surface = font.render(f"Score: {self.score}", True, "green")
            self.screen.blit(text_surface, ((WIDTH - text_surface.get_width()) / 2, (HEIGHT - text_surface.get_height() + 50) / 2))
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