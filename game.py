import sys
import time
import os
import webbrowser
import pickledb
import pygame
from pygame import mixer
import get_lvl

pygame.init()
mixer.init()
pygame.joystick.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((1920, 1080))  # Full Hd экран
pygame.display.set_caption('Rhythm Rampage')
pygame.display.set_icon(pygame.image.load('gameFiles/img/icon.png'))
FPS = 100
clock = pygame.time.Clock()


class MainMenu:
    def __init__(self):
        self.scene = 0
        self.font = pygame.font.Font("gameFiles\Inter-Bold.otf", 44)
        self.self_settings = Settings()
        self.savestat = LastGame()

    def MainMenu(self):
        img = pygame.image.load('gameFiles/img/Menu/Main.png')
        screen.blit(img, (0, 0))
        self.scene = 0

        if self.savestat.is_game_was() is True:
            total, max_streak, over_claim = self.savestat.load()
            text = self.font.render("Last Game:", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_width, text_height = text_rect.size
            text_center = 1300 + (470 // 2) - (text_width // 2), 775 - (text_height // 2)
            screen.blit(text, text_center)

            text = self.font.render(f"Total: {total}", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_width, text_height = text_rect.size
            text_center = 1300 + (470 // 2) - (text_width // 2), 850 - (text_height // 2)
            screen.blit(text, text_center)

            text = self.font.render(f"Max. Streak: x{max_streak}", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_width, text_height = text_rect.size
            text_center = 1300 + (470 // 2) - (text_width // 2), 925 - (text_height // 2)
            screen.blit(text, text_center)

            text = self.font.render(f"Overdrive notes climed: {max_streak}", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_width, text_height = text_rect.size
            text_center = 1300 + (470 // 2) - (text_width // 2), 1000 - (text_height // 2)
            screen.blit(text, text_center)

        # pygame.display.update()
        pygame.display.flip()

    def ChoiceMenu(self):
        img = pygame.image.load('gameFiles/img/Menu/Choice.png')
        screen.blit(img, (0, 0))
        self.scene = 1

        # pygame.display.update()
        pygame.display.flip()

    def SettingsMenu(self):
        img = pygame.image.load('gameFiles/img/Menu/Settings.png')
        screen.blit(img, (0, 0))
        self.scene = 2

        # input
        if Settings.input_device(self.self_settings) == 0:
            InputTypeIco = pygame.image.load('gameFiles/img/InputType/Keyboard.png')
            text = self.font.render("Keyboard", True, (255, 255, 255))
            screen.blit(InputTypeIco, (1768, 78))
        elif Settings.input_device(self.self_settings) == 1:
            InputTypeIco = pygame.image.load('gameFiles/img/InputType/Gamepad.png')
            text = self.font.render("Gamepad", True, (0, 0, 0))
            screen.blit(InputTypeIco, (1768, 70))

        # track 1

        if Settings.input_device(self.self_settings) == 0:
            text = self.font.render(Settings.get(self.self_settings, 1), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_width, text_height = text_rect.size
            text_center = 1012 + (246 // 2) - (text_width // 2), 228 + (102 // 2) - (text_height // 2)
            screen.blit(text, text_center)
        elif Settings.input_device(self.self_settings) == 1:
            img = pygame.image.load(f"gameFiles/img/GamepadKeys/{Settings.get(self.self_settings, 1)}.png")
            screen.blit(img, (1100, 248))

        # track 2

        if Settings.input_device(self.self_settings) == 0:
            text = self.font.render(Settings.get(self.self_settings, 2), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_width, text_height = text_rect.size
            text_center = 1012 + (246 // 2) - (text_width // 2), 329 + (102 // 2) - (text_height // 2)
            screen.blit(text, text_center)
        elif Settings.input_device(self.self_settings) == 1:
            img = pygame.image.load(f"gameFiles/img/GamepadKeys/{Settings.get(self.self_settings, 2)}.png")
            screen.blit(img, (1100, 350))

        # track 3

        if Settings.input_device(self.self_settings) == 0:
            text = self.font.render(Settings.get(self.self_settings, 3), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_width, text_height = text_rect.size
            text_center = 1012 + (246 // 2) - (text_width // 2), 434 + (102 // 2) - (text_height // 2)
            screen.blit(text, text_center)
        elif Settings.input_device(self.self_settings) == 1:
            img = pygame.image.load(f"gameFiles/img/GamepadKeys/{Settings.get(self.self_settings, 3)}.png")
            screen.blit(img, (1100, 455))

        # track 4

        if Settings.input_device(self.self_settings) == 0:
            text = self.font.render(Settings.get(self.self_settings, 4), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_width, text_height = text_rect.size
            text_center = 1012 + (246 // 2) - (text_width // 2), 539 + (102 // 2) - (text_height // 2)
            screen.blit(text, text_center)
        elif Settings.input_device(self.self_settings) == 1:
            img = pygame.image.load(f"gameFiles/img/GamepadKeys/{Settings.get(self.self_settings, 4)}.png")
            screen.blit(img, (1100, 560))

        # Overdrive

        if Settings.input_device(self.self_settings) == 0:
            text = self.font.render(Settings.get(self.self_settings, "Over"), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_width, text_height = text_rect.size
            text_center = 1012 + (246 // 2) - (text_width // 2), 645 + (102 // 2) - (text_height // 2)
            screen.blit(text, text_center)
        elif Settings.input_device(self.self_settings) == 1:
            img = pygame.image.load(f"gameFiles/img/GamepadKeys/{Settings.get(self.self_settings, 'Over')}.png")
            screen.blit(img, (1100, 665))

        # pygame.display.update()
        pygame.display.flip()

    def check_buttons(self):
        if self.scene == 0:  # MainMenu
            if 810 <= mouse[0] <= 1109 and 540 <= mouse[1] <= 651:  # Game
                game = Game(self.self_settings, "levels/lvl1", [100, 500])
                game.start()
            if 1635 <= mouse[0] <= 1859 and 59 <= mouse[1] <= 132:  # Settings
                self.SettingsMenu()
            if 31 <= mouse[0] <= 219 and 982 <= mouse[1] <= 1056:  # Authors
                webbrowser.open("https://github.com/vokintru/YandexProject2?tab=readme-ov-file"
                                "#%D0%B0%D0%B2%D1%82%D0%BE%D1%80%D1%8B")
                pass
            if 60 <= mouse[0] <= 134 and 59 <= mouse[1] <= 132:  # Exit
                self.exit()
        # elif self.scene == 1:  # ChoiceMenu
        #    if 52 <= mouse[0] <= 150 and 56 <= mouse[1] <= 130:  # Back
        #        self.MainMenu()
        #    if 660 <= mouse[0] <= 1258 and 342 <= mouse[1] <= 452:  # LvL1
        #        print("LvL1 Start")
        #        game = Game(self.self_settings, "levels/lvl1", [100, 500])
        #        game.start()
        #    if 660 <= mouse[0] <= 1258 and 484 <= mouse[1] <= 595:  # LvL2
        #        print("LvL2 Start")
        #        game = Game(self.self_settings, "levels/lvl2", [100, 500])
        #        game.start()
        #    if 660 <= mouse[0] <= 1258 and 627 <= mouse[1] <= 737:  # Custom LvL
        #        print("Custom LvL Start")
        elif self.scene == 2:
            if 52 <= mouse[0] <= 151 and 56 <= mouse[1] <= 130:  # Back
                self.MainMenu()
            if 1752 <= mouse[0] <= 1879 and 41 <= mouse[1] <= 168:  # Change Input
                print(pygame.joystick.get_count())
                if pygame.joystick.get_count() != 0:
                    Settings.input_device(self.self_settings, 1)
                    self.SettingsMenu()
                else:
                    Settings.input_device(self.self_settings, 1, 0)
                    self.SettingsMenu()

            # change
            if 1012 <= mouse[0] <= 1259 and 225 <= mouse[1] <= 749:
                img = pygame.image.load(f"gameFiles/img/wait_for_input.png")
                if 225 <= mouse[1] <= 329:
                    screen.blit(img, (1012, 225))
                    pygame.display.flip()
                    if Settings.change_key(self.self_settings, 1):
                        self.SettingsMenu()
                elif 330 <= mouse[1] <= 434:
                    screen.blit(img, (1012, 330))
                    pygame.display.flip()
                    if Settings.change_key(self.self_settings, 2):
                        self.SettingsMenu()
                elif 435 <= mouse[1] <= 539:
                    screen.blit(img, (1012, 435))
                    pygame.display.flip()
                    if Settings.change_key(self.self_settings, 3):
                        self.SettingsMenu()
                elif 540 <= mouse[1] <= 664:
                    screen.blit(img, (1012, 540))
                    pygame.display.flip()
                    if Settings.change_key(self.self_settings, 4):
                        self.SettingsMenu()
                elif 665 <= mouse[1] <= 749:
                    screen.blit(img, (1012, 665))
                    pygame.display.flip()
                    if Settings.change_key(self.self_settings, "Over"):
                        self.SettingsMenu()

    def exit(self):
        sys.exit(0)


class LastGame:
    def __init__(self):
        self.file = pickledb.load('gameFiles/lastgame.json', True)

    def save(self, total, max_streak, over_claimed):
        self.file.set("total", total)
        self.file.set("max_streak", max_streak)
        self.file.set("over_claimed", over_claimed)

    def load(self):
        total = self.file.get("total")
        max_streak = self.file.get("max_streak")
        over_claimed = self.file.get("over_claimed")
        return total, max_streak, over_claimed

    def is_game_was(self):
        return os.path.exists("gameFiles/lastgame.json")


class Settings:
    def __init__(self):
        self.settings = pickledb.load('gameFiles/settings.json', True)

    def input_device(self, do=0, device=None):
        if do == 0:
            return int(self.settings.get("input"))
        elif do == 1:
            if device is None:
                now = int(self.settings.get("input"))
                if now == 1:
                    self.settings.set("input", "0")
                elif now == 0:
                    self.settings.set("input", "1")
                return int(self.settings.get("input"))
            else:
                self.settings.set("input", f"{device}")

    def get(self, track):
        if int(self.settings.get("input")) == 0:
            if track == 5:
                x = self.settings.get(f"keyboardOver")
                return x.upper()
            else:
                x = self.settings.get(f"keyboard{track}")
                return x.upper()
        elif int(self.settings.get("input")) == 1:
            if track == 5:
                x = self.settings.get(f"gamepadOver")
                return x.upper()
            else:
                x = self.settings.get(f"gamepad{track}")
                return x.upper()

    def change_key(self, track):
        if int(self.settings.get("input")) == 0:
            key = 0
            while key == 0:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        key = pygame.key.name(event.key)
            self.settings.set(f"keyboard{track}", key)
        elif int(self.settings.get("input")) == 1:
            key = None
            while key is None:
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.JOYBUTTONDOWN:
                        key = event.button
                    if event.type == pygame.JOYAXISMOTION:
                        if event.axis == 4 or event.axis == 5:
                            if event.axis == 4:
                                key = "LT"
                            elif event.axis == 5:
                                key = "RT"
                    if event.type == pygame.JOYHATMOTION:
                        if event.value == (0, -1):
                            key = "DOWN"
                        elif event.value == (1, 0):
                            key = "RIGHT"
                        elif event.value == (-1, 0):
                            key = "LEFT"
                        elif event.value == (0, 1):
                            key = "UP"
            if key == 0:
                key = "A"
            elif key == 1:
                key = "B"
            elif key == 2:
                key = "X"
            elif key == 3:
                key = "Y"
            elif key == 4:
                key = "LB"
            elif key == 5:
                key = "RB"
            self.settings.set(f"gamepad{track}", key)
        return True


class Note(pygame.sprite.Sprite):
    def __init__(self, game, track, index, time, i):
        super().__init__(game.all_sprites, game.notes_group)
        self.otl = 0
        if len(i[2]) > 1:
            self.image = pygame.image.load('gameFiles/img/note2.png')
            self.over = True
        else:
            self.image = pygame.image.load('gameFiles/img/note1.png')
            self.over = False
        self.rect = self.image.get_rect()
        if track == 1:
            self.rect.x = 329
        elif track == 2:
            self.rect.x = 733
        elif track == 3:
            self.rect.x = 1136
        elif track == 4:
            self.rect.x = 1539

        self.rect.y = 1000 - (index * 1200 + time * 75)
        self.tochno = self.rect.y
        # print(self.rect.y)

    def update(self, dt):
        self.tochno += float(5.9 * dt / 10)
        self.rect.y = self.tochno
        # if self.otl < 4:
        #    self.rect.y += 6
        #    self.otl += 1
        # else:
        #    self.rect.y += 7
        #    self.otl = 0


class Points:
    def __init__(self):
        self.over = False
        self.over_power = 0
        self.streak = [1, 0]

        self.total = 0
        self.over_claim = 0
        self.max_streak = 1

    def claim(self, overx=False):
        if overx is True and self.over_power < 2000:
            self.over_power += 200

        if overx is True:
            self.over_claim += 1

        if self.over is True:
            self.total += 50 * (self.streak[0] * 2)
        else:
            self.total += 50 * self.streak[0]

        if self.streak[1] == 7 and self.streak[0] < 6:
            self.streak[0] += 1
            if self.streak[0] == 6:
                self.streak[1] = 8
            else:
                self.streak[1] = 0
            if self.max_streak < self.streak[0]:
                self.max_streak = self.streak[0]
        elif self.streak[0] == 6:
            pass
        else:
            self.streak[1] += 1

        return


class Game(MainMenu):
    def __init__(self, setting: Settings, lvl_number, notes_t: list):

        super().__init__()
        self.counter = Points()
        self.colors = ['#00ff00', '#00ff00', '#00ff00', '#00ff00']
        self.setting = setting
        self.lvl_n = lvl_number
        self.notes_t = notes_t
        self.font = pygame.font.Font("gameFiles\Inter-Bold.otf", 44)
        self.all_sprites = pygame.sprite.Group()
        self.notes_group = pygame.sprite.Group()
        self.status_track = [False, False, False, False]

    def draw(self):
        for i in range(4):
            if self.status_track[i]:
                self.colors[i] = '#ff0000'
            else:
                self.colors[i] = '#00ff00'

        pygame.draw.rect(screen, pygame.Color('#ffffff'), (304, 0, 100, 1080))
        pygame.draw.rect(screen, pygame.Color('#ffffff'), (708, 0, 100, 1080))
        pygame.draw.rect(screen, pygame.Color('#ffffff'), (1112, 0, 100, 1080))
        pygame.draw.rect(screen, pygame.Color('#ffffff'), (1516, 0, 100, 1080))

        pygame.draw.rect(screen, pygame.Color(self.colors[0]), (304, 1000, 100, 100))
        pygame.draw.rect(screen, pygame.Color(self.colors[1]), (708, 1000, 100, 100))
        pygame.draw.rect(screen, pygame.Color(self.colors[2]), (1112, 1000, 100, 100))
        pygame.draw.rect(screen, pygame.Color(self.colors[3]), (1516, 1000, 100, 100))

        if self.counter.over is True:
            text = self.font.render("x" + str(self.counter.streak[0] * 2), True, (255, 255, 0))
        else:
            text = self.font.render("x" + str(self.counter.streak[0]), True, (255, 255, 255))
        screen.blit(text, (20, 936))

        text = self.font.render(f"Total: {self.counter.total}", True, (255, 255, 255))
        screen.blit(text, (20, 834))

        start_cord = 886
        for i in range(self.counter.streak[1]):
            if self.counter.over is True:
                col = pygame.Color('#ffff00')
            else:
                col = pygame.Color('#00ffff')
            pygame.draw.rect(screen, col, (110, start_cord + 20 * i, 40, 10))
        pygame.draw.rect(screen, pygame.Color('#FFA500'), (170, 886, 40, (7.5 * (self.counter.over_power / 100))))

    def start(self):
        running = True
        lvl = get_lvl.get_lvl(self.lvl_n + "/lvl.json")
        mixer.music.load(self.lvl_n + "/lvl.mp3")
        for i in lvl:
            Note(self, int(i[2][0][4:]), i[0], i[1], i)
            # print(i)
        # no = Note(self, 3, 5, 8, ["line3", "1", ["line1"]])
        if int(self.setting.input_device()) == 0:
            input_d = 0
        elif int(self.setting.input_device()) == 1:
            input_d = 1
        otsr = 0
        key = None
        gamepad_rtlt = 0
        mixer.music.play()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        running = False
                    if input_d == 0:
                        # print(pygame.key.name(event.key).upper())
                        for i in range(1, 6):
                            if pygame.key.name(event.key).upper() == self.setting.get(i):
                                if 1 <= i <= 4:
                                    self.status_track[i - 1] = True
                                    self.on_click(i)
                                elif i == 5:
                                    self.counter.over = True
                if input_d == 0:
                    if event.type == pygame.KEYUP:
                        for i in range(1, 5):
                            if pygame.key.name(event.key).upper() == self.setting.get(i):
                                # self.colors[i - 1] = '#00ff00'
                                self.status_track[i - 1] = False

                elif input_d == 1:
                    if event.type == pygame.JOYBUTTONDOWN:
                        key = event.button
                    if event.type == pygame.JOYAXISMOTION:
                        if event.axis == 4 and event.value >= 0 or event.axis == 5 and event.value >= 0:
                            if gamepad_rtlt == 0:
                                if event.axis == 4:
                                    key = "LT"
                                elif event.axis == 5:
                                    key = "RT"
                                gamepad_rtlt = 1
                            else:
                                key = None
                        else:
                            gamepad_rtlt = 0
                    if event.type == pygame.JOYHATMOTION:
                        if event.value == (0, -1):
                            key = "DOWN"
                        elif event.value == (1, 0):
                            key = "RIGHT"
                        elif event.value == (-1, 0):
                            key = "LEFT"
                        elif event.value == (0, 1):
                            key = "UP"
                    if key == 0:
                        key = "A"
                    elif key == 1:
                        key = "B"
                    elif key == 2:
                        key = "X"
                    elif key == 3:
                        key = "Y"
                    elif key == 4:
                        key = "LB"
                    elif key == 5:
                        key = "RB"
                    for i in range(1, 5):
                        self.status_track[i - 1] = False
                    for i in range(1, 6):
                        if key == self.setting.get(i):
                            if 1 <= i <= 4:
                                self.status_track[i - 1] = True
                                self.on_click(i)
                            elif i == 5:
                                self.counter.over = True
                            # self.status_track[i - 1] = True
                            # self.on_click(i)
                key = None

            if not pygame.mixer.music.get_busy():
                running = False
            if self.counter.over is True and self.counter.over_power > 0:
                self.counter.over_power -= 1
            else:
                self.counter.over = False

            for note in self.notes_group:
                if note.rect.y > 1100:
                    note.kill()
                    self.counter.streak = [1, 0]

            pygame.display.flip()

            dt = clock.tick(100)
            # print(dt)
            self.all_sprites.update(dt)

            screen.fill(pygame.Color('black'))

            self.draw()
            self.all_sprites.draw(screen)
            # print(5.9 * dt / 10)
            # print(no.rect.y)
        mixer.music.stop()
        self.savestat.save(self.counter.total, self.counter.max_streak, self.counter.over_claim)
        self.MainMenu()

    def on_click(self, track):
        for note in self.notes_group:
            if track == 1:
                if note.rect.y > 925 and note.rect.x == 329:
                    note.kill()
                    self.counter.claim(note.over)
                    return
            elif track == 2:
                if note.rect.y > 925 and note.rect.x == 733:
                    note.kill()
                    self.counter.claim(note.over)
                    return
            elif track == 3:
                if note.rect.y > 925 and note.rect.x == 1136:
                    note.kill()
                    self.counter.claim(note.over)
                    return
            elif track == 4:
                if note.rect.y > 925 and note.rect.x == 1539:
                    note.kill()
                    self.counter.claim(note.over)
                    return
        self.counter.streak = [1, 0]


if __name__ == '__main__':
    if pygame.joystick.get_count() >= 2:
        print("Disconnect secont joystick")
        time.sleep(5)
        exit(0)
    else:
        try:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
        except Exception:
            s = Settings()
            Settings.input_device(s, 1, 0)
            print("Джостик не найден")
    running = True
    window = MainMenu()
    window.MainMenu()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                # print(mouse)
                window.check_buttons()

        clock.tick(FPS)
    pygame.quit()
