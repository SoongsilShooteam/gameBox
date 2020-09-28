import pygame
import os
from source.scene import titleScene,stageOneScene
from source.object import player

pygame.init()

size = [1024, 768]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("TEST")
isRun = True
isPlay = False

# 프로세스의 현재 경로를 루트로 변경함.
#os.chdir("../")

titleScene = titleScene.TitleScene(screen) #타이틀 화면 생성
stageOneScene = stageOneScene.StageOneScene() #스테이지 1 생성
scene = titleScene #처음 화면을 타이틀 화면으로 고정
scene.nextScene(stageOneScene) #타이틀화면 다음은 스테이지 1 화면으로 고정

#player = player.Player(100,400)
player = player.Player(screen) #플레이어 객체 생성
allSprites = pygame.sprite.Group() #allSprites 객체 생성
allSprites.add(player) #allSprites 객체에 player 추가


while isRun:
    clock.tick(60)

    mouse = pygame.mouse.get_pos()
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # 메뉴 클릭 이벤트 추가 예정
            if not isPlay :
                scene = scene.next
                isPlay = True

    scene.update()
    scene.render(screen)

    if isPlay:
        allSprites.update() #allSprites의 등록된 모든 객체를 업데이트
        allSprites.draw(screen) #allSprites의 등록된 모든 객체를 화면에 그림.

    #pygame.display.update()
    pygame.display.flip()

pygame.quit()
