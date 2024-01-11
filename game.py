import pygame
from pygame.locals import *

pygame.init()
infoObject = pygame.display.Info()
gameDisplay = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))  # Полный экран
pygame.display.set_caption('Ритм Игра')
FPS = 100
clock = pygame.time.Clock()


class MainMenu:
    def __init__(self):
        pass

    def MainMenu(self):
        img = pygame.image.load('gameFiles/img/MainMenu.png')
        rect = img.get_rect()
        rect.center = (infoObject.current_w/2, infoObject.current_h/2)
        gameDisplay.blit(img, rect)
        pygame.display.flip()

    def game_init(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse = pygame.mouse.get_pos()
                    # print(mouse)
                    game.check_buttons()

            clock.tick(FPS)

    def exit(self):
        sys.exit(0)


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
            x = self.settings.get(f"keyboard{track}")
            return x.upper()
        elif int(self.settings.get("input")) == 1:
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


if __name__ == '__main__':
    if pygame.joystick.get_count() >= 2:
        print("Disconnect second joystick")
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
    game = MainMenu()
    game.MainMenu()
    game.game_init()

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
            text = self.font.render("Keyboard", True, (0, 0, 0))
            screen.blit(text, (1015, 165))
        elif Settings.input_device(self.self_settings) == 1:
            text = self.font.render("Gamepad", True, (0, 0, 0))
            screen.blit(text, (1015, 165))

        # track 1

        if Settings.input_device(self.self_settings) == 0:
            text = self.font.render(Settings.get(self.self_settings, 1), True, (0, 0, 0))
            screen.blit(text, (1024, 252))
        elif Settings.input_device(self.self_settings) == 1:
            img = pygame.image.load(f"gameFiles/img/GamepadKeys/{Settings.get(self.self_settings, 1)}.png")
            screen.blit(img, (1060, 235))

        # track 2

        if Settings.input_device(self.self_settings) == 0:
            text = self.font.render(Settings.get(self.self_settings, 2), True, (0, 0, 0))
            screen.blit(text, (1024, 330))
        elif Settings.input_device(self.self_settings) == 1:
            img = pygame.image.load(f"gameFiles/img/GamepadKeys/{Settings.get(self.self_settings, 2)}.png")
            screen.blit(img, (1060, 305))

        # track 3

        if Settings.input_device(self.self_settings) == 0:
            text = self.font.render(Settings.get(self.self_settings, 3), True, (0, 0, 0))
            screen.blit(text, (1024, 400))
        elif Settings.input_device(self.self_settings) == 1:
            img = pygame.image.load(f"gameFiles/img/GamepadKeys/{Settings.get(self.self_settings, 3)}.png")
            screen.blit(img, (1060, 380))

        # track 4

        if Settings.input_device(self.self_settings) == 0:
            text = self.font.render(Settings.get(self.self_settings, 4), True, (0, 0, 0))
            screen.blit(text, (1024, 460))
        elif Settings.input_device(self.self_settings) == 1:
            img = pygame.image.load(f"gameFiles/img/GamepadKeys/{Settings.get(self.self_settings, 4)}.png")
            screen.blit(img, (1060, 445))

        # Overdrive

        if Settings.input_device(self.self_settings) == 0:
            text = self.font.render(Settings.get(self.self_settings, "Over"), True, (0, 0, 0))
            screen.blit(text, (1024, 522))
        elif Settings.input_device(self.self_settings) == 1:
            img = pygame.image.load(f"gameFiles/img/GamepadKeys/{Settings.get(self.self_settings, 'Over')}.png")
            screen.blit(img, (1060, 505))

        # pygame.display.update()
        pygame.display.flip()

    def check_buttons(self):
        if self.scene == 0:  # MainMenu
            if 805 <= mouse[0] <= 1115 and 595 <= mouse[1] <= 720:  # ChoiceMenu
                self.ChoiceMenu()
            if 1640 <= mouse[0] <= 1910 and 35 <= mouse[1] <= 90:  # SettingsMenu
                self.SettingsMenu()
            if 70 <= mouse[0] <= 335 and 40 <= mouse[1] <= 108:  # Exit
                self.exit()
        elif self.scene == 1:  # ChoiceMenu
            if 57 <= mouse[0] <= 345 and 45 <= mouse[1] <= 110:  # MainMenu
                self.MainMenu()
            if 725 <= mouse[0] <= 1065 and 410 <= mouse[1] <= 475:  # LvL1
                print("LvL1 Start")
                game = Game(self.self_settings, 1, [100, 500])
                game.start()
            if 725 <= mouse[0] <= 1065 and 485 <= mouse[1] <= 555:  # LvL2
                print("LvL2 Start")
                game = Game(self.self_settings, 2, [100, 500])
                game.start()
            if 725 <= mouse[0] <= 1065 and 565 <= mouse[1] <= 635:  # Custom LvL
                print("Custom LvL Start")
                game = Game(self.self_settings, 3, [100, 500])
                game.start()
        elif self.scene == 2:
            if 48 <= mouse[0] <= 290 and 15 <= mouse[1] <= 80:  # MainMenu
                self.MainMenu()
            if 950 <= mouse[0] <= 1245 and 140 <= mouse[1] <= 215:  # Change Input
                print(pygame.joystick.get_count())
                if pygame.joystick.get_count() != 0:
                    Settings.input_device(self.self_settings, 1)
                    self.SettingsMenu()
                else:
                    Settings.input_device(self.self_settings, 1, 0)
                    self.SettingsMenu()

            # change
            if 950 <= mouse[0] <= 1245 and 235 <= mouse[1] <= 565:
                img = pygame.image.load(f"gameFiles/img/wait_for_input.png")
                if 235 <= mouse[1] <= 300:
                    screen.blit(img, (954, 235))
                    pygame.display.flip()
                    if Settings.change_key(self.self_settings, 1):
                        self.SettingsMenu()
                elif 305 <= mouse[1] <= 368:
                    screen.blit(img, (954, 305))
                    pygame.display.flip()
                    if Settings.change_key(self.self_settings, 2):
                        self.SettingsMenu()
                elif 375 <= mouse[1] <= 440:
                    screen.blit(img, (954, 375))
                    pygame.display.flip()
                    if Settings.change_key(self.self_settings, 3):
                        self.SettingsMenu()
                elif 445 <= mouse[1] <= 500:
                    screen.blit(img, (954, 445))
                    pygame.display.flip()
                    if Settings.change_key(self.self_settings, 4):
                        self.SettingsMenu()
                elif 505 <= mouse[1] <= 565:
                    screen.blit(img, (954, 505))
                    pygame.display.flip()
                    if Settings.change_key(self.self_settings, "Over"):
                        self.SettingsMenu()

    def exit(self):
        sys.exit(0)


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
            x = self.settings.get(f"keyboard{track}")
            return x.upper()
        elif int(self.settings.get("input")) == 1:
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
    def __init__(self, game, track):
        super().__init__(game.all_sprites)
        self.image = pygame.image.load('gameFiles/img/note1.png')
        self.rect = self.image.get_rect()
        if track == 1:
            self.rect.x = 325
            self.rect.y = 5
        elif track == 2:
            self.rect.x = 729
            self.rect.y = 5
        elif track == 3:
            self.rect.x = 1133
            self.rect.y = 5
        elif track == 4:
            self.rect.x = 1535
            self.rect.y = 5

    def update(self):
        self.rect.y += 3


class Game(Window):
    def __init__(self, setting: Settings, lvl_number, notes_t: list):

        super().__init__()
        self.colors = ['#00ff00', '#00ff00', '#00ff00', '#00ff00']
        self.setting = setting
        self.lvl_n = lvl_number
        self.notes_t = notes_t
        self.all_sprites = pygame.sprite.Group()
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

        pygame.draw.rect(screen, pygame.Color(self.colors[0]), (304, 1000, 100, 1080))
        pygame.draw.rect(screen, pygame.Color(self.colors[1]), (708, 1000, 100, 1080))
        pygame.draw.rect(screen, pygame.Color(self.colors[2]), (1112, 1000, 100, 1080))
        pygame.draw.rect(screen, pygame.Color(self.colors[3]), (1516, 1000, 100, 1080))

    def start(self):
        s = 199
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        running = False
                    for i in range(1, 5):
                        if pygame.key.name(event.key).upper() == self.setting.get(i):
                            self.status_track[i - 1] = True
                if event.type == pygame.KEYUP:
                    for i in range(1, 5):
                        if pygame.key.name(event.key).upper() == self.setting.get(i):
                            #self.colors[i - 1] = '#00ff00'
                            self.status_track[i - 1] = False
            s += 1
            if s == 200:
                s = 0
                Note(self, 1)
                Note(self, 2)
                Note(self, 3)
                Note(self, 4)
            pygame.display.flip()
            clock.tick(FPS)
            screen.fill(pygame.Color('black'))
            self.draw()
            self.all_sprites.draw(screen)
            self.all_sprites.update()
        self.ChoiceMenu()


    def on_click(self, track):
        pass


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
    window = Window()
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
