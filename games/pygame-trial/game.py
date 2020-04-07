import pygame
import window
import bonus
import player

class Game:
    def __init__(self):
        self.win = window.createWindow("Game", 720, 480)
        self.isRunning = True
        self.clock = pygame.time.Clock()
        self.player = player.Player()

    def gameLoop(self):
        while self.isRunning:
            self.clock.tick(60)
            self.update()
            self.render()
        pygame.quit()

    def update(self):
        self.handleInput()
        self.player.update()

    def render(self):
        self.win.fill((255, 255, 255))
        self.player.render(self.win)
        pygame.display.update()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.x -= self.player.dv
        if keys[pygame.K_RIGHT]:
            self.player.x += self.player.dv
        if keys[pygame.K_UP]:
            self.player.y -= self.player.dv
        if keys[pygame.K_DOWN]:
            self.player.y += self.player.dv

def main():
    game = Game()
    game.gameLoop()

main()