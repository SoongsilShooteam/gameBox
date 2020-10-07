import arcade
from source.scene.sceneManager import *
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
        self.image = pygame.image.load("assets/images/stageOne.png")
        self.x = self.image.get_width()
        self.y = self.image.get_height()
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        self.rect = self.image.get_rect()
        self.backgroundList = arcade.SpriteList() # bg 이미지 2장을 보관할 sprite list 생성
        self.backgroundSprite = arcade.Sprite("assets/images/stageOne.png") # 첫 번째 bg
        self.backgroundSprite2 = arcade.Sprite("assets/images/stageOne.png") # 두 번째 bg
        #self.size = [480, 800]
        #self.screen = pygame.display.set_mode(self.size)
        self.speed = 2 # 배경이 움직이는 속도

        #self.enemy1 = self.enemy.NWayBentSpiralEnemy(self.player, self.allSprites, self.screenX / 2 - 200, 150, 3)  # 적 객체 생성
        #self.enemy2 = self.enemy.NormalEnemy(self.player, self.allSprites, self.screenY / 2 + 200, 150)  # 적 객체 생성
        # self.allSprites.add(enemy1)  # allSprites 객체에 enemy 추가
        # self.allSprites.add(enemy2)  # allSprites 객체에 enemy 추가

    def process(self, events):
        # 첫 번째 bg 시작 위치 지정
        self.backgroundSprite.center_x = self.screenX // 2 # 첫 bg의 x축 중심은 화면 가로의 절반(중심)
        self.backgroundSprite.center_y = self.y // 2 # 첫 bg의 y축 중심은 화면 세로의 절반(중심)
        self.backgroundSprite.change_y = -self.speed # y축에 speed로 설정한 숫자만큼 아래로 이동하도록 변화를 줌

        self.backgroundList.append(self.backgroundSprite) # sprite list에 첫 번째 bg 추가

        # 두 번째 bg 시작 위치 지정
        self.backgroundSprite2.center_x = self.x // 2 # 두 번째 bg의 x축 중심은 화면 가로의 절반(중심)
        self.backgroundSprite2.center_y = self.screenY + self.y // 2 # 두 번째 bg의 y축 중심은 (화면 세로+이미지 세로)의 절반, 첫 번째 이미지가 끝나는 지점에 두 번째 이미지를 배치해야 하기 때문
        self.backgroundSprite2.change_y = -self.speed # y축에 speed로 설정한 숫자만큼 아래로 이동하도록 변화를 줌

        self.backgroundList.append(self.backgroundSprite2) # sprite list에 두 번째 bg 추가

    def onDraw(self):
        arcade.start_render()
        self.backgroundList.draw() # bg를 저장한 sprite list를 화면에 그리기

    def update(self):
        if self.backgroundSprite.bottom == -self.y:  # 첫 bg가 화면에서 사라지면
            self.backgroundSprite.center_y = self.screenY + self.y // 2  # 첫 bg의 세로 좌표를 bg 2의 시작 지점으로

        if self.backgroundSprite2.bottom == -self.y:  # 두 번째 bg가 화면에서 사라지면
            self.backgroundSprite2.center_y = self.screenY + self.y // 2  # 두 bg의 세로 좌표를 bg 2의 시작 지점으로

        self.backgroundList.update()

        #self.allSprites.update()  # allSprites의 등록된 모든 객체를 업데이트
        #self.allSprites.draw(self.screen)  # allSprites의 등록된 모든 객체를 화면에 그림.

        # 단독 파일로 구현하면 실행되는데 스테이지1에 동일하게 적용하니 배경이 안 움직이네요...