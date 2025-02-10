import pygame as pg

class SpriteSheet:
    def __init__(self, path):
        self.sprite_sheet = pg.image.load(path).convert_alpha()

    def get_sprite(self, x, y, w, h):
        sprite = pg.Surface((w, h), pg.SRCALPHA)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    def get_animation(self, row, w, h, count):
        sprites = []
        for i in range(count):
            sprite = self.get_sprite(i*w, row*h, w, h)
            sprites.append(sprite)
        return sprites
