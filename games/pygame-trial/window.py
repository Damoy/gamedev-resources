import pygame

def init():
    pygame.init()

def createWindow(title, width, height):
    init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return win