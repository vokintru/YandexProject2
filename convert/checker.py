import sys
import time
import threading
import pygame
from pygame import mixer
import get_lvl
#import pyautogui

pygame.init()
mixer.init()
mixer.music.load("33787.mp3")
screen = pygame.display.set_mode((1000, 1000))
tempo = round(get_lvl.fps("33787.json") / 60 / 16 * 1000)
print(tempo)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Consolas', 30)



if __name__ == '__main__':
    running = True
    counter = 0
    text = str(counter)
    out = get_lvl.get_lvl("33787.json")
    print(out)
    screen.fill((255, 255, 255))
    otsr = 0
    mixer.music.play()
    prev_time = time.time()
    #pyautogui.click()
    while running:
        if otsr != 0:
            otsr -= 1
        else:
            screen.fill((255, 255, 255))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False

        current_time = time.time()
        elapsed_time = current_time - prev_time

        # Ваш код обработки таймера с точностью до миллисекунды
        if elapsed_time >= 123 / 1000:  # 1 миллисекунда в секундах
            counter += 1
            text = str(counter)
            if any(x[0] == counter for x in out):
                pygame.draw.circle(screen, (255, 0, 0), (500, 500), 200)
                otsr = 10

            # Сброс предыдущего времени
            prev_time = current_time

        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()
