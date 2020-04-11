import pygame

class Texture:
    def __init__(self, path):
        self.path = path
        self.image = pygame.image.load(path).convert()

    # cropX, cropY, width, height => cropData
    def render(self, screen: pygame.Surface, x, y, cropData=None):
        if cropData is None:
            screen.blit(self.image, (x, y))
        else:
            screen.blit(self.image, (x, y), cropData)