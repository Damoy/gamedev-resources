import os

import pygame
from player import Player
from texture import Texture
from window import Window
from map import Map


class Game:
    def __init__(self):
        # to center window
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.window = Window("Game", 898, 576, 4, flags=0)
        self.screen = self.window.get()
        self.clock = pygame.time.Clock()
        self.isRunning = False
        self.textures = Texture("./res/textures.png")
        self.map = Map(self.window, self.textures)
        self.player = Player(self.window.get(), self.textures, 1, 1)

    def gameLoop(self):
        self.isRunning = True
        while self.isRunning:
            self.clock.tick(60)
            if not self.update():
                self.isRunning = False
                break
            self.render()
        pygame.quit()

    def update(self):
        if not self.player.update():
            return False
        return True

    def render(self):
        self.screen.fill((255, 255, 255))
        self.map.render()
        self.player.render()
        self.window.render()

def main():
    game = Game()
    game.gameLoop()


main()
