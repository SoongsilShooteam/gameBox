from source.scene.sceneManager import *
from source.object.object import Object
import pygame

class StageOneScene(SceneManager, Object):
    def __init__(self, screen):
        Object.__init__(self, 0, 0, 'images/bg.png')

        self.speed = 3 # 배경이 움직이는 속도

    def process(self, events):
        pass

    def update(self):
        key = pygame.key.get_pressed() # 키 방향 반대로 배경이 움직이도록 설정

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        if key[pygame.K_LEFT]:
            self.x += self.speed

        elif key[pygame.K_RIGHT]:
            self.x -= self.speed

        elif key[pygame.K_UP]:
            self.y += self.speed

        elif key[pygame.K_DOWN]:
            self.y -= self.speed

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y)) # 배경화면 지정

# 배경은 추가하였으나 배경을 더 넓게 설정하는 방법을 모르겠음...
