from pygame import mixer as Mixer
import pygame

class SceneManager(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = None
        self.y = None
        self.next = self
        self.bgm = None
        self.now = None
        self.image = None
        self.isTitleBGM = False
        self.isStageOneBGM = False

        Mixer.init()

    def process(self, events):   #필요성 검토 중
        pass

    def update(self):
        print(self.now)
        if self.image is not None:
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)

        if self.isTitleBGM == False and self.now == "title":
            Mixer.music.load("assets/sounds/title.mp3")
            self.isTitleBGM = True
            self.isStageOneBGM = False
            Mixer.music.play()
        elif self.isStageOneBGM == False and self.now == "stageOne":
            Mixer.music.load("assets/sounds/stageOne.mp3")
            self.isTitleBGM = False
            self.isStageOneBGM = True
            Mixer.music.play()

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def nextScene(self, scene):
        self.next = scene
