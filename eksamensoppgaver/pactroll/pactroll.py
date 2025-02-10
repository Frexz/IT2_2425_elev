import pygame as pg
from pygame.locals import *
from random import randint
from numpy import radians


WIDTH, HEIGHT = 800, 600
FPS = 60

class Troll(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprite1 = pg.image.load("assets/pac1.png")
        self.sprite1 = pg.transform.scale(self.sprite1, (20, 20))
        self.sprite2 = pg.image.load("assets/pac2.png")
        self.sprite2 = pg.transform.scale(self.sprite2, (20, 20))
        self.sprite3 = pg.image.load("assets/pac3.png")
        self.sprite3 = pg.transform.scale(self.sprite3, (20, 20))
        self.sprites = [self.sprite2, self.sprite3, self.sprite2, self.sprite1]
        self.image_counter = 0
        self.angle = 0
        self.image = self.sprites[self.image_counter]
        self.timer = pg.time.get_ticks()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.vx = 0
        self.vy = 0
        self.speed = 2

    def update(self):
        self.rect.x += self.vx * self.speed
        self.rect.y += self.vy * self.speed

        if pg.time.get_ticks() - self.timer > 200:
            self.timer = pg.time.get_ticks()
            self.image_counter = (self.image_counter + 1) % 4
            self.image = self.sprites[self.image_counter]
            self.image = pg.transform.rotate(self.image, self.angle)

        if self.rect.left <= 0:
            self.rect.left = 0
            app.gameOver = True
        
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            app.gameOver = True
        
        if self.rect.top <= 0:
            self.rect.top = 0
            app.gameOver = True
        
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            app.gameOver = True

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("assets/coin.png")
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, WIDTH - self.rect.width)
        self.rect.y = randint(0, HEIGHT - self.rect.height)

class Block(pg.sprite.Sprite):
    def __init__(self, topleft):
        super().__init__()
        self.image = pg.image.load("assets/block.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Pactroll")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.score = 0
        self.gameOver = False
        self.udødelig = False
        self.timer = pg.time.get_ticks()

        self.troll = Troll()
        self.all_sprites.add(self.troll)

        for _ in range(3):
            coin = Coin()
            self.all_sprites.add(coin)
            collisions = pg.sprite.spritecollide(self.troll, self.all_sprites, False)
            while len(collisions) > 1:
                coin.kill()
                coin = Coin()
                self.all_sprites.add(coin)
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    self.troll.vx = 0
                    self.troll.vy = -1
                    self.troll.angle = 90
                elif event.key == pg.K_s:
                    self.troll.vx = 0
                    self.troll.vy = 1
                    self.troll.angle = 270
                elif event.key == pg.K_a:
                    self.troll.vx = -1
                    self.troll.vy = 0
                    self.troll.angle = 180
                elif event.key == pg.K_d:
                    self.troll.vx = 1
                    self.troll.vy = 0
                    self.troll.angle = 0
                
                    
    
    def update(self):
        collisions = pg.sprite.spritecollide(self.troll, self.all_sprites, False)
        for c in collisions:
            if isinstance(c, Coin):
                self.score += 1
                block = Block(c.rect.topleft)
                c.kill()
                self.all_sprites.add(block)
                self.all_sprites.add(Coin())
                self.udødelig = True
                self.timer = pg.time.get_ticks()
                self.troll.speed += 0.1
            elif isinstance(c, Block) and not self.udødelig:
                self.gameOver = True
        
        for coin in self.all_sprites:
            if isinstance(coin, Coin):
                collisions = pg.sprite.spritecollide(coin, self.all_sprites, False)
                for c in collisions:
                    if (isinstance(c, Coin) or isinstance(c, Block)) and coin != c:
                        coin.kill()
                        self.all_sprites.add(Coin())

        if pg.time.get_ticks() - self.timer > 500:
            self.udødelig = False

        self.all_sprites.update()
    
    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)

        font = pg.font.SysFont("Consolas", 14)
        text_surface = font.render(f"Score: {self.score}", True, "white")
        self.screen.blit(text_surface, (10, 10))

        if self.gameOver:
            font = pg.font.SysFont("Consolas", 40)
            text_surface = font.render("GAME OVER", True, "red")
            self.screen.blit(text_surface, ((WIDTH - text_surface.get_width())/2, (HEIGHT - text_surface.get_height())/2))

            font = pg.font.SysFont("Consolas", 20)
            text_surface = font.render(f"Score: {self.score}", True, "red")
            self.screen.blit(text_surface, ((WIDTH - text_surface.get_width())/2, (HEIGHT - text_surface.get_height() + 50)/2))
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