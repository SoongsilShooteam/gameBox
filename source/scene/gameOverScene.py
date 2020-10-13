from source.scene import sceneManager, titleScene
from pygame import mixer as Mixer
from source.object.object import Object
import pygame

class GameOverScene():
    def __init__(self, screen):
        print("********** Init GameOverScene **********")
        self.img = 'assets/images/gameOverScene.png'
        self.image = pygame.transform.scale(pygame.image.load(self.img), (480, 800))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.x = self.image.get_width()
        self.y = self.image.get_height()
        self.player = None
        self.sceneManager = sceneManager.SceneManager()

        Mixer.init()
        Mixer.music.load("assets/sounds/title.mp3") # sound 변경 예정
        Mixer.music.play()

    def update(self):
        if self.image is not None:
            self.rect = self.image.get_rect()
            self.rect.center = (self.x * 0.5, self.y * 0.5)

        # key = pygame.key.get_pressed()
        # if key[pygame.K_SPACE]:
        # 스페이스 키가 탄환 발사 키로 사용중이라 키보드 입력으로 받으면 게임오버 화면이 너무 빠르게 지나가서
        # 클릭으로 바뀌게 코드 입력해두었어요

        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            self.sceneManager.setScene(titleScene.TitleScene(self.screen))

    def render(self):
        self.screen.blit(self.image, self.rect)
