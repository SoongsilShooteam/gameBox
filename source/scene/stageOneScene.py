from pygame import mixer as Mixer
from source.scene import stageTwoScene, sceneManager
from source.object import enemy
from source.object import player
from source.object.object import Object
import pygame
import random

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
    def __init__(self, screen, gameLevel=1):
        print("********** Init StageOneScene **********")
        self.allSprites = pygame.sprite.Group() #allSprites 객체 생성
        self.now = "stageOne"
        self.screen = screen
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        self.enemyList = []
        self.stageStartTime = pygame.time.get_ticks() # 스테이지 시작 시간
        self.gameClear = Object(self.screenX/2, self.screenY/2, "assets/images/gameClear.png")
        self.stageClearYn = False
        self.gameLevel = gameLevel
        self.sceneManager = sceneManager.SceneManager()

        # 일반 적이 출현하는 정보를 적어놓는 리스트
        # Tuple 값 해석
        # 튜플 요소 0번째: 적이 출현하는 시간대 (초 단위)
        # 튜플 요소 1번째: 적의 Type (0: 일반 적, 1: 보스)
        # 튜플 요소 2번째: 적이 출현하는 x 좌표
        # 튜플 요소 3번째: 적이 출현하는 y 좌표
        self.enemyGenInfoList = [
            (1.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (1.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (5.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (8.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (9.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (9.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (12.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (14.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (15.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (15.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (17.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (18.5, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (20.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (22.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (22.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (23.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (28.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (31.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (32.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (32.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (35.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (37.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (38.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (38.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (40.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (41.5, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (43.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (45.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (45.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (46.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (49.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (50.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (50.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (52.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (55.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (56.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (56.0, 1, self.screenX / 2.0, -15.0),
            (60.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (65.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (67.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (70.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (75.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (75.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (78.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (80.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (86.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (88.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
            (90.0, 0, random.randrange(50.0, self.screenX - 50.0), -15.0),
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

    def addEnemy(self, enemy):
        self.enemyList.append(enemy)

    def removeEnemy(self, enemy):
        enemy.kill()
        self.enemyList.remove(enemy)

    def addScore(self):
        self.sceneManager.score += 50
        print(self.sceneManager.score)

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
            e = enemy.NormalEnemy(self.allSprites, x, y)
            e.onEnemyDead = lambda : self.addScore()
            self.addEnemy(e)
        elif enemyGenInfo[1] == 1:
            boss = enemy.NWayBentSpiralEnemy(self.allSprites, x, y, 3)
            boss.onEnemyDead = self.stageClear
            self.addEnemy(boss)

    def stageClear(self):
        self.stageClearYn = True
        self.sceneManager.score += 200
        print(self.sceneManager.score)
        for enemy in self.enemyList:
            enemy.kill()
        self.enemyGenInfoList = []
        self.enemyList = []
        return True

    def render(self):
        self.allSprites.draw(self.screen)  # allSprites의 등록된 모든 객체를 화면에 그림.

        #if len(self.enemyGenInfoList) == 0 and len(self.enemyList) == 0:
        if self.stageClearYn is True:
            self.sceneManager.setScene(stageTwoScene.StageTwoScene(self.screen, self.gameLevel + 1))
