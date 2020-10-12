from pygame import mixer as Mixer
from source.object import enemy
from source.object import player
from source.object.object import Object
import pygame
import random

class StageOneNormalEnemy(enemy.NormalEnemy):
    def update(self):
        super().update()

class BackgroundSprite(Object):
    def __init__(self):
        super().__init__(0, 0, "assets/images/stageOne.png")
        self.rect.center = (self.image.get_width() / 2, self.image.get_height() / 2)
        self.backgroundMoveSpeed = 2 # 배경이 움직이는 속도

    def update(self):
        self.rect.centery = self.rect.centery + 1
        if self.rect.top == 1:  # 백그라운드가 일정 y좌표가 되면 원래의 위치로 되돌려준다.
            self.rect.top = -800

class StageOneScene():
    def __init__(self, screen):
        print("********** Init StageOneScene **********")
        self.allSprites = pygame.sprite.Group() #allSprites 객체 생성
        self.now = "stageOne"
        self.screen = screen
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        self.enemyList = []
        self.stageStartTime = pygame.time.get_ticks() # 스테이지 시작 시간

        # 일반 적이 출현하는 정보를 적어놓는 리스트
        # Tuple 값 해석
        # 튜플 요소 0번째: 적이 출현하는 시간대 (초 단위)
        # 튜플 요소 1번째: 적의 Type (0: 일반 적, 1: 보스)
        # 튜플 요소 2번째: 적이 출현하는 x 좌표
        # 튜플 요소 3번째: 적이 출현하는 y 좌표
        self.enemyGenInfoList = [
            (1.0, 0, random.randrange(0.0, self.screenX), -15.0),
            (1.0, 0, random.randrange(0.0, self.screenX), -15.0),
            (5.0, 0, random.randrange(0.0, self.screenX), -15.0),
            (8.0, 0, random.randrange(0.0, self.screenX), -15.0),
            (9.0, 0, random.randrange(0.0, self.screenX), -15.0),
            (9.0, 0, random.randrange(0.0, self.screenX), -15.0),
            (12.0, 0, random.randrange(0.0, self.screenX), -15.0),
            (14.0, 0, random.randrange(0.0, self.screenX), -15.0),
            (20.0, 1, self.screenX / 2.0, -15.0),
        ]

        self.initializeBackground()
        self.initializeBGM()
        self.initializePlayer()

    def initializeBackground(self):
        self.allSprites.add(BackgroundSprite())

    def initializeBGM(self):
        Mixer.init()
        Mixer.music.load("assets/sounds/stageOne.mp3")
        Mixer.music.play()

    def initializePlayer(self):
        self.player = player.Player(self.screen, self.allSprites)  # 플레이어 객체 생성
        self.allSprites.add(self.player)  # allSprites 객체에 player 추가

    def addEnemy(self, enemy):
        self.allSprites.add(enemy)
        self.enemyList.append(enemy)

    def removeEnemy(self, enemy):
        self.allSprites.remove(enemy)
        self.enemyList.remove(enemy)

    def update(self):
        self.allSprites.update()  # allSprites의 등록된 모든 객체를 업데이트

        stageElapsedTime = (pygame.time.get_ticks() - self.stageStartTime) / 1000.0

        while len(self.enemyGenInfoList) is not 0:
            enemyGenInfo = self.enemyGenInfoList[0]
            if enemyGenInfo[0] <= stageElapsedTime:
                self.generateEnemyByInfo(enemyGenInfo)
                del self.enemyGenInfoList[0]
            else:
                break

    def generateEnemyByInfo(self, enemyGenInfo):
        (x, y) = enemyGenInfo[2], enemyGenInfo[3]

        if enemyGenInfo[1] == 0:
            self.addEnemy(enemy.NormalEnemy(self.allSprites, x, y))
        elif enemyGenInfo[1] == 1:
            self.addEnemy(enemy.NWayBentSpiralEnemy(self.allSprites, x, y, 3))

    def render(self):
        self.allSprites.draw(self.screen)  # allSprites의 등록된 모든 객체를 화면에 그림.
