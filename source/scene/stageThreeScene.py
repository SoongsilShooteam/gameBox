from pygame import mixer as Mixer
from source.object import enemy
from source.object import player
from source.object.object import Object
from source.scene import sceneManager
import pygame
import random

class BackgroundSprite(Object):
    def __init__(self):
        super().__init__(0, 0, "assets/images/stageThree.png")
        self.rect.center = (self.image.get_width() / 2, self.image.get_height() / 2)
        self.backgroundMoveSpeed = 2 # 배경이 움직이는 속도

    def update(self):
        self.rect.centery = self.rect.centery + 1
        if self.rect.top == 1:  # 백그라운드가 일정 y좌표가 되면 원래의 위치로 되돌려준다.
            self.rect.top = -800

class StageThreeScene():
    def __init__(self, screen, gameLevel=1):
        print("********** Init StageThreeScene **********")
        self.allSprites = pygame.sprite.Group() #allSprites 객체 생성
        self.now = "stageThree"
        self.screen = screen
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        self.enemyList = []
        self.stageStartTime = pygame.time.get_ticks() # 스테이지 시작 시간
        self.nextEnemyGenTime = 1.0
        self.gameClear = Object(self.screenX/2, self.screenY/2, "assets/images/gameClear.png")
        self.stageClearYn = False
        self.gameLevel = gameLevel
        self.sceneManager = sceneManager.SceneManager()
        self.enemyGenInfoList = []

        self.initializeEnemyGenInfoList()
        self.initializeBackground()
        self.initializeBGM()
        self.initializePlayer()

    def initializeBackground(self):
        self.allSprites.add(BackgroundSprite())

    def initializeBGM(self):
        Mixer.init()
        Mixer.music.load("assets/sounds/stageThree_2.mp3")
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

    def initializeEnemyGenInfoList(self):
        # 일반 적이 출현하는 정보를 적어놓는 리스트
        # Tuple 값 해석
        # 튜플 요소 0번째: 적이 출현하는 시간대 (초 단위)
        # 튜플 요소 1번째: 적의 Type (0: 일반 적, 1: 보스)
        # 튜플 요소 2번째: 적이 출현하는 x 좌표
        # 튜플 요소 3번째: 적이 출현하는 y 좌표
        # 튜플 요소 4번째: 적의 속도가 고정 속도인지 아닌지. 0이면 랜덤 속도, 그 외는 지정된 고정 속도 값.
        self.enemyGenInfoList = [
            (1.0, 0, 74, -15.0, 0.0),
            (1.255244724293191, 0, 413, -15.0, 0.0),
            (1.4791106264906366, 0, 189, -15.0, 0.0),
            (2.2059144363515357, 0, 401, -15.0, 0.0),
            (2.3572019047559962, 0, 314, -15.0, 0.0),
            (2.672296477344059, 0, 247, -15.0, 0.0),
            (3.5396290764517344, 0, 267, -15.0, 0.0),
            (4.361493718806313, 0, 395, -15.0, 0.0),
            (5.12098509102243, 0, 372, -15.0, 0.0),
            (5.906930500531125, 0, 161, -15.0, 0.0),
            (6.21418782781666, 0, 404, -15.0, 0.0),
            (7.120582795487885, 0, 174, -15.0, 0.0),
            (7.758387930696981, 0, 208, -15.0, 0.0),
            (8.063125872279675, 0, 72, -15.0, 0.0),
            (9.036976091840437, 0, 212, -15.0, 0.0),
            (9.929796048925663, 0, 320, -15.0, 0.0),
            (10.538999293990697, 0, 241, -15.0, 0.0),
            (11.387611593529916, 0, 120, -15.0, 0.0),
            (11.401287540449145, 0, 193, -15.0, 0.0),
            (12.162160254581222, 0, 340, -15.0, 0.0),
            (12.476151110687043, 0, 406, -15.0, 0.0),
            (13.567939393423558, 0, 276, -15.0, 0.0),
            (13.766338605723242, 0, 72, -15.0, 0.0),
            (14.373687700820879, 0, 379, -15.0, 0.0),
            (15.079409329305633, 0, 316, -15.0, 0.0),
            (15.248233345843795, 0, 113, -15.0, 0.0),
            (15.676311784044358, 0, 372, -15.0, 0.0),
            (15.79218557386235, 0, 139, -15.0, 0.0),
            (16.441476718932325, 0, 427, -15.0, 0.0),
            (16.91712979157872, 0, 247, -15.0, 0.0),
            (17.36148709735833, 1, 100.0, -15.0, 4.5),
            (17.36148709735833, 1, 240.0, -15.0, 4.5),
            (17.36148709735833, 1, 380.0, -15.0, 4.5),
            (17.36148709735833, 0, 292, -15.0, 0.0),
            (17.71542834508756, 0, 244, -15.0, 0.0),
            (18.73006931189204, 2, 353, -15.0, 0.0),
            (19.031766996282286, 0, 131, -15.0, 0.0),
            (19.918452771428733, 0, 50, -15.0, 0.0),
            (20.852185283535185, 0, 60, -15.0, 0.0),
            (21.29041660955943, 0, 412, -15.0, 0.0),
            (21.844441252787245, 0, 257, -15.0, 0.0),
            (22.00561273715902, 0, 337, -15.0, 0.0),
            (22.44992945125783, 2, 180, -15.0, 0.0),
            (22.488696562077035, 0, 370, -15.0, 0.0),
            (22.846351633668203, 0, 134, -15.0, 0.0),
            (23.446715937236572, 0, 213, -15.0, 0.0),
            (23.889406575423905, 0, 257, -15.0, 0.0),
            (24.135980919644624, 0, 184, -15.0, 0.0),
            (25.042759234022203, 0, 273, -15.0, 0.0),
            (25.39118356023649, 0, 286, -15.0, 0.0),
            (26.025731874470843, 0, 120, -15.0, 0.0),
            (26.277694644800423, 0, 262, -15.0, 0.0),
            (27.122142951848605, 1, 357, -15.0, 0.0),
            (27.971514623382713, 0, 417, -15.0, 0.0),
            (28.208863574026264, 0, 379, -15.0, 0.0),
            (29.266926312999733, 0, 367, -15.0, 0.0),
            (30.10686511664731, 0, 334, -15.0, 0.0),
            (30.6971818626921, 0, 378, -15.0, 0.0),
            (31.14412941010642, 0, 404, -15.0, 0.0),
            (32.15152139290107, 0, 244, -15.0, 0.0),
            (32.495089866112934, 2, 147, -15.0, 0.0),
            (32.838966000205545, 2, 119, -15.0, 0.0),
            (33.05328772719407, 0, 186, -15.0, 0.0),
            (33.30934191166644, 0, 141, -15.0, 0.0),
            (34.44568927803084, 0, 56, -15.0, 0.0),
            (35.30914142941011, 0, 390, -15.0, 0.0),
            (35.65390503568839, 2, 71, -15.0, 0.0),
            (35.911273604416905, 0, 129, -15.0, 0.0),
            (36.0076118367242, 0, 167, -15.0, 0.0),
            (37.02503119560439, 0, 185, -15.0, 0.0),
            (37.85141758327405, 0, 132, -15.0, 0.0),
            (38.01881039465513, 0, 58, -15.0, 0.0),
            (38.10445839201159, 0, 209, -15.0, 0.0),
            (38.87948965491246, 2, 190.0, -15.0, 4.5),
            (38.87948965491246, 2, 290.0, -15.0, 4.5),
            (39.87948965491246, 2, 140.0, -15.0, 4.5),
            (39.87948965491246, 2, 240.0, -15.0, 4.5),
            (39.87948965491246, 2, 340.0, -15.0, 4.5),
            (40.010439852552516, 0, 311, -15.0, 0.0),
            (40.17230018707039, 0, 333, -15.0, 0.0),
            (40.927359698655486, 0, 134, -15.0, 0.0),
            (42.028147166074696, 2, 218, -15.0, 0.0),
            (43.10463836168073, 0, 125, -15.0, 0.0),
            (43.959743589020185, 0, 62, -15.0, 0.0),
            (44.67949249288893, 0, 192, -15.0, 0.0),
            (45.56385770464033, 2, 317, -15.0, 0.0),
            (46.34622287592581, 0, 158, -15.0, 0.0),
            (47.15901922692464, 0, 172, -15.0, 0.0),
            (47.402908973355714, 0, 218, -15.0, 0.0),
            (47.828317361397566, 0, 161, -15.0, 0.0),
            (48.72260595578794, 1, 406, -15.0, 0.0),
            (49.540131276144734, 0, 356, -15.0, 0.0),
            (49.605006642065185, 0, 301, -15.0, 0.0),
            (50.56710666239958, 0, 286, -15.0, 0.0),
            (51.75682596679033, 2, 313, -15.0, 0.0),
            (52.5697337988813, 0, 100, -15.0, 0.0),
            (52.6401498839831, 0, 79, -15.0, 0.0),
            (53.42752255938226, 0, 248, -15.0, 0.0),
            (53.53046245794349, 0, 339, -15.0, 0.0),
            (54.429920380667085, 0, 230, -15.0, 0.0),
            (54.71544168822022, 0, 82, -15.0, 0.0),
            (54.97668455371022, 0, 167, -15.0, 0.0),
            (55.14958676092074, 0, 365, -15.0, 0.0),
            (55.54181952552482, 2, 56, -15.0, 0.0),
            (56.61199001995996, 0, 268, -15.0, 0.0),
            (56.932811109085755, 0, 323, -15.0, 0.0),
            (57.92843797417364, 0, 274, -15.0, 0.0),
            (58.57632769813886, 0, 266, -15.0, 0.0),
            (59.023277412219606, 0, 194, -15.0, 0.0),
            (60.14296710131992, 0, 411, -15.0, 0.0),
            (60.99452129806633, 0, 155, -15.0, 0.0),
            (61.27178365533186, 0, 302, -15.0, 0.0),
            (61.87178365533186, 0, 302, -15.0, 0.0),
            (64.557260305599175, 3, self.screenX / 2.0, -15.0, 0.0),
        ]

    def generateEnemyByInfo(self, enemyGenInfo):
        (x, y) = enemyGenInfo[2], enemyGenInfo[3]

        e = None
        if enemyGenInfo[1] == 0:
            e = enemy.NormalEnemy(self.allSprites, x, y)
            e.onEnemyDead = lambda: self.addScore()
        elif enemyGenInfo[1] == 1:
            e = enemy.NormalEnemy2(self.allSprites, x, y)
            e.onEnemyDead = lambda: self.addScore()
        elif enemyGenInfo[1] == 2:
            e = enemy.NormalEnemy3(self.allSprites, x, y)
            e.onEnemyDead = lambda: self.addScore()
        elif enemyGenInfo[1] == 3:
            e = enemy.StageThreeBossEnemy(self.allSprites, x, y)
            e.onEnemyDead = self.stageClear

        if enemyGenInfo[4] != 0:
            e.speed = enemyGenInfo[4]

        self.addEnemy(e)

    def stageClear(self):
        self.stageClearYn = True

        self.sceneManager.score += 200

        for enemy in self.enemyList:
            enemy.kill()
        self.enemyGenInfoList = []
        self.enemyList = []
        return True

    def render(self):
        self.allSprites.draw(self.screen)

        if self.stageClearYn is True:
            self.gameClear.render(self.screen)