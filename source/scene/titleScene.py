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
