import pygame
import os
from source.scene import titleScene,stageOneScene
from source.object import player

pygame.init()

size = [1024, 768]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("TEST")

run = True
clock = pygame.time.Clock()

# 프로세스의 현재 경로를 루트로 변경함.
#os.chdir("../")

titleScene = titleScene.TitleScene(screen) #타이틀 화면 생성
stageOneScene = stageOneScene.StageOneScene() #스테이지 1 생성
scene = titleScene #처음 화면을 타이틀 화면으로 고정
scene.nextScene(stageOneScene) #타이틀화면 다음은 스테이지 1 화면으로 고정

#player = player.Player(100,400)
player = player.Player(screen)
allSprites=pygame.sprite.Group()

play = False
while run:
    clock.tick(60)

    mouse=pygame.mouse.get_pos()
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            scene = scene.next
            play = True

    scene.render(screen)
    scene.update()

    if play:
        player.render(screen)
        player.update()
        #print(player.rect)

    #pygame.display.update()
    pygame.display.flip()

pygame.quit()
