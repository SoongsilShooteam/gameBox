from source.scene import stageOneScene, sceneManager
from pygame import mixer as Mixer
from source.object.object import Object
import pygame


class TitleScene:
    def __init__(self, screen):
        print("********** Init TitleScene **********")
        self.img = 'assets/images/title.png'
        self.image = pygame.transform.scale(pygame.image.load(self.img), (480, 800))
        self.rect = self.image.get_rect()
        self.x = 0.5 * self.image.get_width()
        self.y = 0.5 * self.image.get_height()
        self.player = None
        self.sceneManager = sceneManager.SceneManager()
        self.screen = screen
        self.menu = ["Play", "HowToPlay", "Quit"]
        for i in range(0, 3):
            if i == 0:
                self.menu[i] = (Object(0, 0, "assets/images/buttonPlay.png"))
            elif i == 1:
                self.menu[i] = (Object(0, 0, "assets/images/buttonHowToPlay.png"))
            else:
                self.menu[i] = (Object(0, 0, "assets/images/buttonQuit.png"))
            self.menu[i].x = 0.5 * screen.get_width()
            self.menu[i].y = 0.55 * screen.get_height() + i * 110
            self.menu[i].update()


        Mixer.init()
        Mixer.music.load("assets/sounds/title.mp3")
        Mixer.music.play()

    def update(self):
        if self.image is not None:
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.sceneManager.setScene(stageOneScene.StageOneScene(self.screen))

    def render(self):
        self.screen.blit(self.image, self.rect)

        for i in range(3):
            self.menu[i].render(self.screen)