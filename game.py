import pygame
from pygame.locals import *

pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((1920, 1080))  # Полный экран
pygame.display.set_caption('Ритм Игра')
FPS = 100
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.scene = 0

    def MainMenu(self):
        img = pygame.image.load('gameFiles/img/MainMenu.png')
        screen.blit(img, (0, 0))
        self.scene = 0

        #pygame.display.update()
        pygame.display.flip()


if __name__ == '__main__':
    running = True
    game = Game()
    game.MainMenu()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 805 <= mouse[0] <= 1115 and 595 <= mouse[1] <= 720:
                    print("CLICKED")
        clock.tick(FPS)
    pygame.quit()
