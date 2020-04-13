import pygame
from window import Window
import sprites

TILE_SIZE = 16


class Map:
    def __init__(self, window: Window, textures: pygame.image, spriteBank: dict):
        self.window = window
        self.textures = textures
        self.rows = window.height // TILE_SIZE
        self.cols = window.width // TILE_SIZE
        self.tilesBank = spriteBank['tiles']

    def update(self):
        pass

    def render(self):
        self.window.get().fill(self.tilesBank['grass'].get_at((0, 0)))
