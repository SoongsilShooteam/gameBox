from source.object.object import Object
from source.vector import Vector2
from source.scene.stageOneScene import *
from source.scene import sceneManager
import pygame
import os
import random as rnd

os.chdir(os.getcwd())
print(os.getcwd())


class Item(Object):
    def __init__(self, x, y, spriteGroup, player, use = True) :
        super().__init__(x, y, "assets/images/item.png")
        self.spriteGroup = spriteGroup
        self.sceneManager = sceneManager.SceneManager()
        self.player = player
        self.use = use
        self.speed = 8
        self.angle = rnd.randrange(2, 8, 2)
        self.xMove = (self.speed / (self.angle + 1))
        self.yMove = (self.speed - (self.speed / (self.angle + 1)))

        self.spriteGroup.add(self)

    def update(self):
        super().update()
        key = pygame.key.get_pressed()

        self.moving()
        self.checkPlayerCollisionItem()
        self.usingYn()

    def moving(self):

        self.x = self.x + self.xMove
        self.y = self.y + self.yMove

        if self.x >= 400 :
            self.xMove = - (self.speed / (self.angle + 1))
            self.angle = rnd.randint(1, 9)

        if self.x < 10 :
            self.xMove = (self.speed / (self.angle + 1))
            self.angle = rnd.randint(1, 9)

        if self.y >= 800 :
            self.yMove = - ((self.speed - (self.speed / (self.angle + 1))))
            self.angle = rnd.randint(1, 9)

        if self.y < 10 :
            self.yMove = (self.speed - (self.speed / (self.angle + 1)))
            self.angle = rnd.randint(1, 9)


    def checkPlayerCollisionItem(self):
        v1 = Vector2(self.player.x, self.player.y)
        v2 = Vector2(self.x, self.y)
        if v1.distance(v2) < 40.0:
            self.kill()
            print('a11111')
            self.rndNum = rnd.randrange(1,10)
            print(self.rndNum)

            if self.rndNum < 7 :
                self.player.plusHp()
            if self.rndNum >= 7:
                if self.player.leftBullet is False :
                    self.player.leftBullet = True

                elif self.player.leftBullet is True :
                    self.player.rightBullet = True
                else :
                    self.player.plusHp()

    def usingYn(self):
        if self.use is False :
            self.kill()