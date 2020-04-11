import pygame
from texture import Texture
from map import TILE_SIZE

class Player:
    def __init__(self, screen: pygame.Surface, textures: Texture, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.textures = textures

    def update(self):
        return self.handleInput()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return False
        if keys[pygame.K_LEFT]:
            self.x -= TILE_SIZE
        if keys[pygame.K_RIGHT]:
            self.x += TILE_SIZE
        if keys[pygame.K_UP]:
            self.y -= TILE_SIZE
        if keys[pygame.K_DOWN]:
            self.y += TILE_SIZE

        return True

    def render(self):
        self.textures.render(self.screen, self.x, self.y, (1, 17, 14, 14))
        # pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.w, self.h))