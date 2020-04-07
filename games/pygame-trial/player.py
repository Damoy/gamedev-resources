import pygame

class Player:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.w = 40
        self.h = 40
        self.dv = 10

    def update(self):
        pass

    def render(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.w, self.h))