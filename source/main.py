import pygame
from pygame import mixer
import os
from source.scene import titleScene, stageOneScene,sceneManager
from source.object import player, enemy

pygame.init()

size = [480, 800]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("TEST")
isRun = True
isPlay = False

# 프로세스의 현재 경로를 루트로 변경함.
path = os.path.join(os.path.dirname(__file__), "../")
os.chdir(path)

allSprites = pygame.sprite.Group() #allSprites 객체 생성

titleScene = titleScene.TitleScene(screen) #타이틀 화면 생성
sceneManager = sceneManager.SceneManager() #sceneManager 생성
sceneManager.setScene(titleScene) #시작화면을 titleScene 화면으로 고정

while isRun:
    clock.tick(60)

    mouse = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    sceneManager.update()
    sceneManager.render()

    #pygame.display.update()
    pygame.display.flip()

pygame.quit()
