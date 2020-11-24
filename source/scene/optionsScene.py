from source.scene import sceneManager, titleScene
from pygame import mixer as Mixer
from source.object.object import Object
import pygame

class OptionsScene():
    def __init__(self, screen):
        print("********** Init OptionsScene **********")
        self.img = 'assets/images/buttonOptions.png'
        self.image = pygame.transform.scale(pygame.image.load(self.img), (480, 200))
        self.rect = self.image.get_rect()
        self.x = self.image.get_width()
        self.y = self.image.get_height()
        self.screen = screen
        self.player = None
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        self.sceneManager = sceneManager.SceneManager()
        # self.buttonImage = 'assets/images/b.png'
        # self.menu = (Object(0, 0, self.buttonImage))
        #self.menu.x = 0.5 * self.screenX
        #self.menu.y = 0.55 * self.screenY + 150
       #self.menu.update()
        self.buttonImage1 = "assets/images/buttonOptionsEasy.png"
        self.buttonImage2 = "assets/images/buttonOptionsNormal.png"
        self.buttonImage3 = "assets/images/buttonOptionsHard.png"
        self.buttonImage4 = "assets/images/buttonQuit.png"
        self.selectOptionImage = "assets/images/bullet01.png"
        self.menu = ["Easy", "Normal", "Hard", "Quit"]

        self.selectOption = (Object(0,0, self.selectOptionImage))
        #self.selectOption = pygame.transform.scale(pygame.image.load(self.img), (480, 200))

        for i in range(4):
            if i == 0:
                self.menu[i] = (Object(0, 0, self.buttonImage1))
            elif i == 1:
                self.menu[i] = (Object(0, 0, self.buttonImage2))
            elif i == 2:
                self.menu[i] = (Object(0, 0, self.buttonImage3))
            else :
                self.menu[i] = (Object(0, 0, self.buttonImage4))
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

        self.mousePos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.sceneManager.gameLevel == 1 :
            self.selectOption.x = self.menu[0].x + 150
            self.selectOption.y = self.menu[0].y
        elif  self.sceneManager.gameLevel == 2 :
            self.selectOption.x = self.menu[1].x + 150
            self.selectOption.y = self.menu[1].y
        elif  self.sceneManager.gameLevel == 3 :
            self.selectOption.x = self.menu[2].x + 150
            self.selectOption.y = self.menu[2].y
        self.selectOption.update()

        for i in range(4):
            if i == 0:
                if 155 < self.mousePos[0] < 325 and 260 < self.mousePos[1] < 310 :
                    self.menu[i] = (Object(0, 0, "assets/images/buttonOptionsEasyHover.png"))

                    if click[0] == 1:
                        self.sceneManager.gameLevel = 1
                else:
                    self.menu[i] = (Object(0, 0, self.buttonImage1))
            elif i == 1:
                if 57 < self.mousePos[0] < 423 and 370 < self.mousePos[1] < 420:
                    self.menu[i] = (Object(0, 0, "assets/images/buttonOptionsNormalHover.png"))

                    if click[0] == 1:
                        self.sceneManager.gameLevel = 2
                else:
                    self.menu[i] = (Object(0, 0, self.buttonImage2))
            elif i == 2:
                if 173 < self.mousePos[0] < 307 and 480 < self.mousePos[1] < 530:
                    self.menu[i] = (Object(0, 0, "assets/images/buttonOptionsHardHover.png"))

                    if click[0] == 1:
                        self.sceneManager.gameLevel = 3
                else:
                    self.menu[i] = (Object(0, 0, self.buttonImage3))
            else :
                if 173 < self.mousePos[0] < 307 and 580 < self.mousePos[1] < 630 :
                    self.menu[i] = (Object(0, 0, "assets/images/buttonQuitHover.png"))

                    if click[0] == 1 :
                        self.sceneManager.setScene(titleScene.TitleScene(self.screen))
                else:
                    self.menu[i] = (Object(0, 0, self.buttonImage4))

            self.menu[i].x = 0.5 * self.screenX
            self.menu[i].y = 0.35 * self.screenY + i * 110
            self.menu[i].update()

           #if 173 < self.mousePos[0] < 307 and 580 < self.mousePos[1] < 640 and click[0] == 1:


        # if 173 < self.mousePos[0] < 307 and 555 < self.mousePos[1] < 625:
        #     self.menu = (Object(0, 0, 'assets/images/buttonBackHover.png'))
        # else:
        #     self.menu = (Object(0, 0, self.buttonImage))
        #self.menu.x = 0.5 * self.screenX
        #self.menu.y = 0.55 * self.screenY + 150
        #self.menu.update()


    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.image, self.rect)
        self.selectOption.render(self.screen)
        # self.menu.render(self.screen)
        for i in range(4):
            self.menu[i].render(self.screen)
