"""
Brettet nullstilles med BACKSPACE og neste generasjon fås med HØYRE PILTAST
"""

import pygame as pg
from pygame.locals import *
from random import random

SQUARE = 30
ROWS, KOLS = 20, 20
WIDTH, HEIGHT = KOLS*SQUARE, ROWS*SQUARE
FPS = 60

class Cell(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.Surface((SQUARE, SQUARE))
        self.rect = self.image.get_rect()
        self.color = "cyan"
        pg.draw.rect(self.image, self.color, (0, 0, SQUARE, SQUARE))
        self.rect.topleft = (x, y)
        self.status = True if random() < 1/3 else False
    
    def update(self):
        if self.status:
            self.color = "cyan"
        else:
            self.color = "white"

        pg.draw.rect(self.image, self.color, (0, 0, SQUARE, SQUARE))

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Game of Life")
        self.running = True
        self.all_sprites = pg.sprite.Group()

        self.grid = []

        for i in range(ROWS):
            row = []
            for j in range(KOLS):
                row.append(Cell(j*SQUARE, i*SQUARE))
            self.grid.append(row)
            self.all_sprites.add(row)
    
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    self.reset()
                elif event.key == pg.K_RIGHT:
                    self.next_generation()
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos[0] // SQUARE, event.pos[1] // SQUARE
                self.grid[y][x].status = not self.grid[y][x].status
    
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

    def reset(self):
        for i in range(ROWS):
            for j in range(KOLS):
                self.grid[i][j].status = False

    def next_generation(self):
        to_live = []
        to_die = []

        for i in range(ROWS):
            for j in range(KOLS):
                cell = self.grid[i][j]
                status = self.get_neighbors(i, j)

                if cell.status and status.count(True) < 2:
                    to_die.append(cell)
                
                if cell.status and status.count(True) > 3:
                    to_die.append(cell)
                
                if not cell.status and status.count(True) == 3:
                    to_live.append(cell)
        
        for cell in to_die:
            cell.status = False

        for cell in to_live:
            cell.status = True
    
    def get_neighbors(self, i, j):
        status = []
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < ROWS and 0 <= nj < KOLS:
                status.append(self.grid[ni][nj].status)
        
        return status
    
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