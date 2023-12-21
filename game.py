import pygame
from pygame.locals import *

pygame.init()
infoObject = pygame.display.Info()
gameDisplay = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))  # Полный экран
pygame.display.set_caption('Ритм Игра')
FPS = 100
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        pass

    def MainMenu(self):
        img = pygame.image.load('gameFiles/img/MainMenu.png')
        rect = img.get_rect()
        rect.center = (infoObject.current_w/2, infoObject.current_h/2)
        gameDisplay.blit(img, rect)
        pygame.display.flip()


if __name__ == '__main__':
    running = True
    game = Game()
    game.MainMenu()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(FPS)
    pygame.quit()
