from source.scene.sceneManager import *
#from source.object.player import *
#from source.object.enemy import *
#from source.object import player, enemy
import pygame


def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper

@singleton
class StageOneScene(SceneManager):
    def __init__(self):
        print("생성")
        #super().__init__(self, 0, 0, 'images/bg.png')
        super().__init__()
        self.allSprites = pygame.sprite.Group() #allSprites 객체 생성
        self.now = "stageOne"
        self.img = "assets/images/stageOne.png"
        self.image = pygame.image.load(self.img)
        self.x = 0.3 * self.image.get_width()
        self.y = 0.3 * self.image.get_height()
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        #self.size = [480, 800]
        #self.screen = pygame.display.set_mode(self.size)
        self.speed = 0.5 # 배경이 움직이는 속도

        #self.enemy1 = self.enemy.NWayBentSpiralEnemy(self.player, self.allSprites, self.screenX / 2 - 200, 150, 3)  # 적 객체 생성
        #self.enemy2 = self.enemy.NormalEnemy(self.player, self.allSprites, self.screenY / 2 + 200, 150)  # 적 객체 생성
        # self.allSprites.add(enemy1)  # allSprites 객체에 enemy 추가
        # self.allSprites.add(enemy2)  # allSprites 객체에 enemy 추가


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

        #self.allSprites.update()  # allSprites의 등록된 모든 객체를 업데이트
        #self.allSprites.draw(self.screen)  # allSprites의 등록된 모든 객체를 화면에 그림.

