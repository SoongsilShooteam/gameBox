from source.object.object import Object
from source.vector import Vector2
from source.scene.stageOneScene import *
from source.scene import sceneManager
from source.scene import sceneManager
from source.scene import gameOverScene
import pygame
import os
from pygame import mixer as Mixer

os.chdir(os.getcwd())
print(os.getcwd())


class Player(Object):
    def __init__(self, screen, spriteGroup):
        super().__init__(screen.get_width() / 2, screen.get_height() / 2 + 200, "assets/images/player.png")
        self.spriteGroup = spriteGroup
        self.screen = screen
        self.sceneManager = sceneManager.SceneManager()
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        self.speed = 5
        self.lastTime = 0.00
        self.shootInterval = 0.1
        self.hp = 5
        self.playerHpBarList = []

        self.leftBullet = False
        self.rightBullet = False

        for i in range(self.hp) :
            self.playerHpBarList.append(PlayerHpBar(i*30+30, 770))
            self.spriteGroup.add(self.playerHpBarList[i])

        spriteGroup.add(self)
        Mixer.init()
        self.gunSound = Mixer.Sound('assets/sounds/gun.mp3')



    def update(self):
        super().update()
        key = pygame.key.get_pressed()

        self.item = self.sceneManager.getItem()

        if key[pygame.K_LEFT]:
            if (self.x - self.speed) > 0:
                self.x -= self.speed

        if key[pygame.K_RIGHT]:
            if (self.x + self.speed) < self.screenX:
                self.x += self.speed

        if key[pygame.K_UP]:
            if (self.y - self.speed) > 0:
                self.y -= self.speed

        if key[pygame.K_DOWN]:
            if (self.y + self.speed) < self.screenY:
                self.y += self.speed

        if key[pygame.K_SPACE]:
            currentTime = pygame.time.get_ticks()

            if (currentTime - self.lastTime) / 1000.0 >= self.shootInterval:
                self.gunSound.stop()
                self.gunSound.play()
                self.spriteGroup.add(PlayerBullet(self.x, self.y - 25))
                if self.leftBullet is True :
                    self.spriteGroup.add(PlayerBullet(self.x-17, self.y + 5))
                if self.rightBullet is True :
                    self.spriteGroup.add(PlayerBullet(self.x+17, self.y + 5))
                self.lastTime = currentTime

    def onHitEnemyBullet(self):
        self.hp -= 1
        self.sceneManager.score -= 100
        if self.sceneManager.score <= 0:
            self.sceneManager.score = 0
            print(self.sceneManager.score)
        else:
            print(self.sceneManager.score)
        self.playerHpBarList[self.hp].kill()
        self.playerHpBarList.pop()
        if self.hp == 0:
            self.kill()
            self.sceneManager.setScene(gameOverScene.GameOverScene(self.screen))

    def plusHp(self):
        self.hp += 2

        for i in range(2) :
            self.playerHpBarList.append(PlayerHpBar(self.playerHpBarList[-1].x + 30, 770))
            self.spriteGroup.add(self.playerHpBarList[-1])

class PlayerHpBar(Object) :
    def __init__(self, x, y):
        super().__init__(x, y, "assets/images/player.png")
        self.image = pygame.transform.scale(self.image, (30, 30))

    def update(self):
        super().update()
        key = pygame.key.get_pressed()


class PlayerBullet(Object):
    def __init__(self, x, y):
        super().__init__(x, y, "assets/images/player_bullet.png")
        self.speed = 10
        self.screenSize = pygame.display.get_surface().get_size()
        self.sceneManager = sceneManager.SceneManager()

    def update(self):
        super().update()
        key = pygame.key.get_pressed()

        self.checkDestroyMe()
        self.checkPlayerCollision()

        self.y -= self.speed

    # 총알이 화면 밖으로 나가면 파괴되어야 하는데, 이를 처리해주는 함수
    def checkDestroyMe(self):
        if (self.x < -30 or
                self.y < - 30 or
                self.x > self.screenSize[0] + 30 or
                self.y > self.screenSize[1] + 30):
            self.kill()

    # 총알이 적과 충돌했는지 판단하는 함수
    def checkPlayerCollision(self):
        for enemy in self.sceneManager.getEnemyList():
            v1 = Vector2(enemy.x, enemy.y)
            v2 = Vector2(self.x, self.y)
            if v1.distance(v2) < enemy.colliderRange:
                self.kill()
                enemy.onHitPlayerBullet()