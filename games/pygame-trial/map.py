from enum import Enum

from window import Window
from texture import Texture

TILE_SIZE = 16

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Map:
    def __init__(self, window: Window, textures: Texture):
        self.window = window
        self.textures = textures
        self.rows = window.height // TILE_SIZE
        self.cols = window.width // TILE_SIZE

    def update(self):
        pass

    def render(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x, y = (col * TILE_SIZE, row * TILE_SIZE)
                cropData = (0, 0, TILE_SIZE, TILE_SIZE)
                self.textures.render(self.window.get(), x, y, cropData)
                # pygame.draw.aaline(self.window.get(), (0, 0, 0), (x, y), (x + TILE_SIZE, y))
                # pygame.draw.aaline(self.window.get(), (0, 0, 0), (x, y), (x, y + TILE_SIZE))
                # pygame.draw.aaline(self.window.get(), (0, 0, 0), (x + TILE_SIZE, y), (x + TILE_SIZE, y + TILE_SIZE))
                # pygame.draw.aaline(self.window.get(), (0, 0, 0), (x, y + TILE_SIZE), (x + TILE_SIZE, y + TILE_SIZE))