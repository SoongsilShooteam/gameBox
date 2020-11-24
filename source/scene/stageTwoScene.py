from pygame import mixer as Mixer
from source.object import enemy
from source.object import player
from source.object.object import Object
from source.scene import sceneManager, stageThreeScene
import pygame
import random

class BackgroundSprite(Object):
    def __init__(self):
        super().__init__(0, 0, "assets/images/stageTwo.png")
        self.rect.center = (self.image.get_width() / 2, self.image.get_height() / 2)
        self.backgroundMoveSpeed = 2 # 배경이 움직이는 속도

    def update(self):
        self.rect.centery = self.rect.centery + 1
        if self.rect.top == 1:  # 백그라운드가 일정 y좌표가 되면 원래의 위치로 되돌려준다.
            self.rect.top = -800

class StageTwoScene():
    def __init__(self, screen, gameLevel=1):
        print("********** Init StageTwoScene **********")
        self.allSprites = pygame.sprite.Group() #allSprites 객체 생성
        self.now = "stageTwo"
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
            (1.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (1.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (5.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (5.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (7.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (9.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (9.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (11.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (12.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (12.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (15.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (17.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (19.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (22.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (24.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (26.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (26.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (28.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (29.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (30.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (33.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (36.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (37.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (37.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (39.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (42.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (45.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (46.0, random.randrange(0, 3), random.randrange(50.0, self.screenX - 50.0), -15.0),
            (50.0, 3, self.screenX / 2.0, -15.0),
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
        self.allSprites.update()

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
            self.addEnemy(e)
            e.onEnemyDead = lambda : self.addScore()
        elif enemyGenInfo[1] == 1:
            e = enemy.NormalEnemy2(self.allSprites, x, y)
            self.addEnemy(e)
            e.onEnemyDead = lambda : self.addScore()
        elif enemyGenInfo[1] == 2:
            e = enemy.NormalEnemy3(self.allSprites, x, y)
            self.addEnemy(e)
            e.onEnemyDead = lambda : self.addScore()
        elif enemyGenInfo[1] == 3:
            boss = enemy.StageTwoBossEnemy(self.allSprites, x, y)
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
        self.allSprites.draw(self.screen)

        self.sceneManager.viewScore(self.screen, self.sceneManager.score, 30, self.screenX / 3, 10)

        if self.stageClearYn is True:
            self.player.x = self.screen.get_width() / 2
            self.player.y -= 6
            if self.player.y <= 0:
                self.sceneManager.setScene(stageThreeScene.StageThreeScene(self.screen, self.gameLevel + 1))
