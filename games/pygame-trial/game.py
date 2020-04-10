from enum import Enum

import pygame
import player


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Window:
    def __init__(self, title, width, height, scale=1, flags=0):
        self.title = title
        self.width = width
        self.height = height
        self.scale = scale
        self.widthScaled = self.width // self.scale
        self.heigthScaled = self.height // self.scale
        self.flags = flags
        self.content = None
        self.scaledContent = None
        self.frame = None
        self.create()

    def create(self):
        self.content = pygame.display.set_mode((self.width, self.height), flags=self.flags)
        self.scaledContent = pygame.Surface([self.widthScaled, self.heigthScaled])
        pygame.display.set_caption(self.title)
        return self.scaledContent

    def get(self):
        return self.scaledContent

    def render(self):
        frame = pygame.transform.scale(self.scaledContent, (self.width, self.height))
        self.content.blit(frame, frame.get_rect())
        pygame.display.update()


class Map:
    def __init__(self, window):
        self.window = window
        self.rows = window.ge


class Game:
    def __init__(self):
        pygame.init()
        self.window = Window("Game", 720, 480, 2)
        self.screen = self.window.get()
        self.clock = pygame.time.Clock()
        self.player = player.Player()
        self.isRunning = False

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
        if not self.handleInput():
            return False
        self.player.update()
        return True

    def render(self):
        self.screen.fill((255, 255, 255))
        self.player.render(self.screen)
        self.window.render()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return False
        if keys[pygame.K_LEFT]:
            self.player.x -= self.player.dv
        if keys[pygame.K_RIGHT]:
            self.player.x += self.player.dv
        if keys[pygame.K_UP]:
            self.player.y -= self.player.dv
        if keys[pygame.K_DOWN]:
            self.player.y += self.player.dv

        return True

def main():
    game = Game()
    game.gameLoop()


main()
