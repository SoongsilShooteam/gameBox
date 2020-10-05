from source.scene.sceneManager import *
from source.object.object import Object
import pygame

class StageOneScene(SceneManager):
    def __init__(self):
        #super().__init__(self, 0, 0, 'images/bg.png')
        super().__init__()
        #self.spriteGroup = spriteGroup
        self.now = "stageOne"
        self.img = "assets/images/stageOne.png"
        self.image = pygame.image.load(self.img)
        self.x = 0.3 * self.image.get_width()
        self.y = 0.3 * self.image.get_height()
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        self.speed = 0.5 # 배경이 움직이는 속도
        #self.spriteGroup.add(self)

    def process(self, events):
        pass

    def update(self):
        super().update()
        key = pygame.key.get_pressed()

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        if key[pygame.K_LEFT]:
            if (self.x - self.speed) > 550:
                self.x -= self.speed

        elif key[pygame.K_RIGHT]:
            if (self.x + self.speed) < 650:
                self.x += self.speed

        elif key[pygame.K_UP]:
            if (self.y - self.speed) > 400:
                self.y -= self.speed

        elif key[pygame.K_DOWN]:
            if (self.y + self.speed) < 500:
                self.y += self.speed

# 배경은 추가하였으나 배경을 더 넓게 설정하는 방법을 모르겠음...
# 구조 바꾸고 배경좀 손봤어요.