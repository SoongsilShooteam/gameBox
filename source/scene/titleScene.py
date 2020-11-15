from source.scene import stageOneScene, sceneManager, optionsScene
from pygame import mixer as Mixer
from source.object.object import Object
import pygame
import math

class TitleScene:
    def __init__(self, screen):
        print("********** Init TitleScene **********")
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        self.allSprites = pygame.sprite.Group() #allSprites 객체 생성
        self.prevTime = pygame.time.get_ticks()
        self.elapsedTime = 0.0

        self.bg = Object(self.screenX / 2, self.screenY / 2, 'assets/images/titleSceneBg.png')
        self.titleImage = Object(self.screenX / 2, 190, 'assets/images/title.png')

        self.allSprites.add(self.bg)
        self.allSprites.add(self.titleImage)

        self.sceneManager = sceneManager.SceneManager()
        self.screen = screen
        self.buttonImage1 = "assets/images/buttonPlay.png"
        self.buttonImage2 = "assets/images/buttonOptions.png"
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
        self.titleImage.update()

        self.elapsedTime += (pygame.time.get_ticks() - self.prevTime) / 500.0
        self.titleImage.y = 190.0 + math.cos(self.elapsedTime) * 10.0
        self.prevTime = pygame.time.get_ticks()

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
                    self.menu[i] = (Object(0, 0, "assets/images/buttonOptionsHover.png"))
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
            self.sceneManager.setScene(stageOneScene.StageOneScene(self.screen, self.sceneManager.gameLevel))

        if 57 < self.mousePos[0] < 423 and 515 < self.mousePos[1] < 585 and click[0] == 1:
            self.sceneManager.setScene(optionsScene.OptionsScene(self.screen))

        if 173 < self.mousePos[0] < 307 and 625 < self.mousePos[1] < 695 and click[0] == 1:
            exit()

    def render(self):
        self.allSprites.draw(self.screen)

        for i in range(3):
            self.menu[i].render(self.screen)

