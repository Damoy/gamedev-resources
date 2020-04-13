import os
import pygame

from player import Player
from window import Window
from map import Map
import sprites


class Game:
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1' # to center window
        pygame.init()
        self.window = Window("Game", 898, 576, 4, flags=0)
        self.screen = self.window.get()
        self.clock = pygame.time.Clock()
        self.isRunning = False
        self.textures = sprites.load(os.path.join('res', 'graphics', 'textures.png'))
        self.spriteBank = sprites.loadSpriteBank(self.textures)
        self.map = Map(self.window, self.textures, self.spriteBank)
        self.allSprites = sprites.GameSpriteGroup()
        self.player = Player(self.window.get(), self.textures, 100, 100, self.allSprites)

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
        self.allSprites.clear(self.screen, self.screen)
        self.allSprites.update()
        self.allSprites.draw(self.screen)
        self.window.render()

def main():
    game = Game()
    game.gameLoop()


main()
