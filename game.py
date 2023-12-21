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

        # pygame.display.update()
        pygame.display.flip()

    def ChoiceMenu(self):
        img = pygame.image.load('gameFiles/img/ChoiceMenu.png')
        screen.blit(img, (0, 0))
        self.scene = 1

        # pygame.display.update()
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
                #print(mouse)
                if game.scene == 0:
                    if 805 <= mouse[0] <= 1115 and 595 <= mouse[1] <= 720:  # MainMenu --> ChoiceMenu
                        game.ChoiceMenu()
                elif game.scene == 1:
                    if 57 <= mouse[0] <= 345 and 45 <= mouse[1] <= 110:  # ChoiceMenu --> MainMenu
                        game.MainMenu()
                    if 725 <= mouse[0] <= 1065 and 410 <= mouse[1] <= 475:  # ChoiceMenu --> LvL1
                        print("LvL1 Start")
                    if 725 <= mouse[0] <= 1065 and 485 <= mouse[1] <= 555:  # ChoiceMenu --> LvL2
                        print("LvL2 Start")
                    if 725 <= mouse[0] <= 1065 and 565 <= mouse[1] <= 635:  # ChoiceMenu --> Custom LvL
                        print("Custom LvL Start")
        clock.tick(FPS)
    pygame.quit()
