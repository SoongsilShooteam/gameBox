from source.scene import sceneManager, titleScene
from pygame import mixer as Mixer
from source.object.object import Object
import pygame

class howToPlayScene():
    def __init__(self, screen):
        print("********** Init howToPlayScene **********")
        self.img = 'assets/images/howToPlayScene.png'
        self.image = pygame.transform.scale(pygame.image.load(self.img), (480, 800))
        self.rect = self.image.get_rect()
        self.x = self.image.get_width()
        self.y = self.image.get_height()
        self.player = None
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        self.sceneManager = sceneManager.SceneManager()
        self.screen = screen

        self.buttonImage = 'assets/images/buttonBack.png'
        self.menu = (Object(0, 0, self.buttonImage))
        self.menu.x = 0.5 * self.screenX
        self.menu.y = 0.55 * self.screenY + 150
        self.menu.update()

        Mixer.init()
        Mixer.music.load("assets/sounds/title.mp3")
        Mixer.music.play()

    def update(self):
        if self.image is not None:
            self.rect = self.image.get_rect()
            self.rect.center = (self.x * 0.5, self.y * 0.5)

        self.mousePos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 173 < self.mousePos[0] < 307 and 555 < self.mousePos[1] < 625:
            self.menu = (Object(0, 0, 'assets/images/buttonBackHover.png'))
        else:
            self.menu = (Object(0, 0, self.buttonImage))
        self.menu.x = 0.5 * self.screenX
        self.menu.y = 0.55 * self.screenY + 150
        self.menu.update()

        if 173 < self.mousePos[0] < 307 and 555 < self.mousePos[1] < 625 and click[0] == 1:
            self.sceneManager.setScene(titleScene.TitleScene(self.screen))

    def render(self):
        self.screen.blit(self.image, self.rect)

        self.menu.render(self.screen)
