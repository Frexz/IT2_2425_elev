import pygame as pg
from pygame.locals import *
from Spritesheet import SpriteSheet

FRAMES = 6

class Player(pg.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        super().__init__()
        self.window_width, self.window_height = WIDTH, HEIGHT
        self.sprite_sheet = SpriteSheet("player.png")

        self.idle_down = self.sprite_sheet.get_animation(0, 32, 32, FRAMES)
        self.idle_right = self.sprite_sheet.get_animation(1, 32, 32, FRAMES)
        self.idle_left = [pg.transform.flip(x, True, False) for x in self.idle_right]
        self.idle_up = self.sprite_sheet.get_animation(2, 32, 32, FRAMES)
    
        self.move_down = self.sprite_sheet.get_animation(3, 32, 32, FRAMES)
        self.move_right = self.sprite_sheet.get_animation(4, 32, 32, FRAMES)
        self.move_left = [pg.transform.flip(x, True, False) for x in self.move_right]
        self.move_up = self.sprite_sheet.get_animation(5, 32, 32, FRAMES)

        self.image = self.idle_down[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.window_width / 2, self.window_height / 2)

        self.is_moving = False
        self.current_frame = 0
        self.animation_speed = 0.1
        self.timer = 0
        self.direction = "down"

    def update(self):
        keys = pg.key.get_pressed()
        self.is_moving = False

        if keys[K_w]:
            self.rect.y -= 2
            self.is_moving = True
            self.direction = "up"
        elif keys[K_s]:
            self.rect.y += 2
            self.is_moving = True
            self.direction = "down"
        elif keys[K_d]:
            self.rect.x += 2
            self.is_moving = True
            self.direction = "right"
        elif keys[K_a]:
            self.rect.x -= 2
            self.is_moving = True
            self.direction = "left"


        if self.rect.top <= 0 or self.rect.bottom >= self.window_height:
            self.rect.y = max(0, min(self.rect.y, self.window_height - self.rect.height))
        
        if self.rect.left <= 0 or self.rect.right >= self.window_width:
            self.rect.x = max(0, min(self.rect.x, self.window_width - self.rect.width))
        
        if self.is_moving:
            if self.direction == "down":
                self.animate(self.move_down)
            elif self.direction == "up":
                self.animate(self.move_up)
            elif self.direction == "right":
                self.animate(self.move_right)
            elif self.direction == "left":
                self.animate(self.move_left)
        else:
            if self.direction == "down":
                self.animate(self.idle_down)
            elif self.direction == "up":
                self.animate(self.idle_up)
            elif self.direction == "right":
                self.animate(self.idle_right)
            elif self.direction == "left":
                self.animate(self.idle_left)

    def animate(self, frames):
        if pg.time.get_ticks() - self.timer > self.animation_speed * 1000:
            self.current_frame = (self.current_frame + 1) % 6
            self.image = frames[self.current_frame]
            self.timer = pg.time.get_ticks()