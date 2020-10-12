from source.scene import stageOneScene, sceneManager, howToPlayScene
from pygame import mixer as Mixer
from source.object.object import Object
import pygame


class TitleScene:
    def __init__(self, screen):
        print("********** Init TitleScene **********")
        self.img = 'assets/images/title.png'
        self.image = pygame.transform.scale(pygame.image.load(self.img), (480, 800))
        self.rect = self.image.get_rect()
        self.x = self.image.get_width()
        self.y = self.image.get_height()
        self.player = None
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        self.sceneManager = sceneManager.SceneManager()
        self.screen = screen
        self.buttonImage1 = "assets/images/buttonPlay.png"
        self.buttonImage2 = "assets/images/buttonHowToPlay.png"
        self.buttonImage3 = "assets/images/buttonQuit.png"
        self.menu = ["Play", "HowToPlay", "Quit"]
        for i in range(3):
            if i == 0:
                self.menu[i] = (Object(0, 0, self.buttonImage1))
            elif i == 1:
                self.menu[i] = (Object(0, 0, self.buttonImage2))
            else:
                self.menu[i] = (Object(0, 0, self.buttonImage3))
            self.menu[i].x = 0.5 * self.screenX
            self.menu[i].y = 0.55 * self.screenY + i * 110
            self.menu[i].update()

        Mixer.init()
        Mixer.music.load("assets/sounds/title.mp3")
        Mixer.music.play()

    def update(self):
        if self.image is not None:
            self.rect = self.image.get_rect()
            self.rect.center = (self.x * 0.5, self.y * 0.5)

        # key = pygame.key.get_pressed()
        # if key[pygame.K_SPACE]:
        #     self.sceneManager.setScene(stageOneScene.StageOneScene(self.screen))

        self.mousePos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for i in range(3):
            if i == 0:
                if 155 < self.mousePos[0] < 325 and 405 < self.mousePos[1] < 475:
                    self.menu[i] = (Object(0, 0, "assets/images/buttonPlayHover.png"))
                else:
                    self.menu[i] = (Object(0, 0, self.buttonImage1))
            elif i == 1:
                if 57 < self.mousePos[0] < 423 and 515 < self.mousePos[1] < 585:
                    self.menu[i] = (Object(0, 0, "assets/images/buttonHowToPlayHover.png"))
                else:
                    self.menu[i] = (Object(0, 0, self.buttonImage2))
            else:
                if 173 < self.mousePos[0] < 307 and 625 < self.mousePos[1] < 695:
                    self.menu[i] = (Object(0, 0, "assets/images/buttonQuitHover.png"))
                else:
                    self.menu[i] = (Object(0, 0, self.buttonImage3))
            self.menu[i].x = 0.5 * self.screenX
            self.menu[i].y = 0.55 * self.screenY + i * 110
            self.menu[i].update()

        if 155 < self.mousePos[0] < 325 and 405 < self.mousePos[1] < 475 and click[0] == 1:
            self.sceneManager.setScene(stageOneScene.StageOneScene(self.screen))

        if 57 < self.mousePos[0] < 423 and 515 < self.mousePos[1] < 585 and click[0] == 1:
            self.sceneManager.setScene(howToPlayScene.HowToPlayScene(self.screen))

        if 173 < self.mousePos[0] < 307 and 625 < self.mousePos[1] < 695 and click[0] == 1:
            exit()

    def render(self):
        self.screen.blit(self.image, self.rect)

        for i in range(3):
            self.menu[i].render(self.screen)

