import pygame
import os
import math
import random
from source.const import PI
from source.vector import Vector2
from source.object.object import Object
from source.scene.stageOneScene import *
from source.scene import sceneManager

# 적이 쏘는 총알
class EnemyBullet(Object):
    def __init__(self, spriteGroup, x, y, angle, angleRate, speed, speedRate, bullet_img):

        self.spriteGroup = spriteGroup
        self.angle = angle  # 총알이 나아가는 각도
        self.angleRate = angleRate  # 프레임당 각도 변화율
        self.speed = speed  # 총알이 나아가는 속도
        self.speedRate = speedRate  # 프레임당 속도 변화율
        self.screenSize = pygame.display.get_surface().get_size()
        self.sceneManager = sceneManager.SceneManager()
        self.player = self.sceneManager.getPlayer()
        super().__init__(x, y, bullet_img)

    def update(self):
        super().update()

        self.player = self.sceneManager.getPlayer()
        rad = self.angle * (PI / 180) # 각도를 radian으로 변환하고
        self.x += self.speed * math.cos(rad) # 이 radian 값을 cos, sin 함수에 넣어주면
        self.y += self.speed * math.sin(rad) # 이 총알이 날아가야할 방향이 나옴

        self.angle += self.angleRate
        self.speed += self.speedRate

        self.checkDestroyMe()
        self.checkPlayerCollision()

    # 총알이 화면 밖으로 나가면 파괴되어야 하는데, 이를 처리해주는 함수
    def checkDestroyMe(self):
        if (self.x < -30 or
            self.y < - 30 or
            self.x > self.screenSize[0] + 30 or
            self.y > self.screenSize[1] + 30):
            self.kill()

    # 총알이 플레이어와 충돌했는지 판단하는 함수
    def checkPlayerCollision(self):
        v1 = Vector2(self.player.x, self.player.y)
        v2 = Vector2(self.x, self.y)
        if v1.distance(v2) < 20.0:
            print("Collide")
            self.kill()
            self.player.onHitEnemyBullet()

# 모든 적이 상속받는 공통 클래스
class Enemy(Object):
    def __init__(self, spriteGroup, hp, moveSpeed, x, y, img, bullet_img):

        self.spriteGroup = spriteGroup
        self.hp = hp # 적의 체력
        self.moveSpeed = moveSpeed # 적의 이동 속도
        self.lastTime = 0.00
        self.shootAngle = 0.0
        self.shootAngleRate = 0.0
        self.shootSpeed = 10.0
        self.shootSpeedRate = 0.0
        self.shootInterval = 0.1 # N초마다 총알 쏘기
        self.sceneManager = sceneManager.SceneManager()
        self.player = self.sceneManager.getPlayer()
        self.bullet_img = bullet_img
        super().__init__(x, y, img)

    def update(self):
        super().update()

        self.player = self.sceneManager.getPlayer()
        currentTime = pygame.time.get_ticks()
        if (currentTime - self.lastTime) / 1000.0 >= self.shootInterval:
            self.shootBullet()
            self.lastTime = currentTime

    def onHitPlayerBullet(self):
        self.hp -= 1
        if self.hp == 0:
            self.sceneManager.removeEnemy(self)

    def shootBullet(self):
        bullet = EnemyBullet(self.spriteGroup, self.x, self.y, self.shootAngle, self.shootAngleRate, self.shootSpeed,self.shootSpeedRate, self.bullet_img)
        bullet.update()
        self.spriteGroup.add(bullet)

# 선회가속 소용돌이 탄을 발사하는 적
class BentSpiralEnemy(Enemy):
    def __init__(self, spriteGroup, x, y):
        super().__init__(spriteGroup, 100, 0, x, y, "assets/images/enemy01.png", "assets/images/enemy_bullet.png")

    def update(self):
        super().update()
        self.shootAngle += 3

# 다중 선회가속 소용돌이 탄을 발사하는 적 2
class NWayBentSpiralEnemy(Enemy):
    def __init__(self, spriteGroup, x, y, n):
        super().__init__(spriteGroup, 100, 0, x, y, "assets/images/enemy01.png", "assets/images/boss_bullet.png")
        self.n = n

    def update(self):
        super().update()
        self.shootAngle += 3

        if self.y < 100:
            self.y += 1.0

    def shootBullet(self):
        for i in range(self.n):
            super().shootBullet()
            self.shootAngle += 360.0 / self.n

# 유저가 있는 방향으로 탄을 발사하는 적
class NormalEnemy(Enemy):
    def __init__(self, spriteGroup, x, y):
        super().__init__(spriteGroup, 3, 0, x, y, "assets/images/enemy01.png", "assets/images/enemy_bullet.png")
        self.speed = random.randrange(2, 5)
        self.shootInterval = 1.0

    def update(self):
        super().update()
        self.y += self.speed

    def shootBullet(self):
        v1 = Vector2(self.x, self.y)
        v2 = Vector2(self.player.x, self.player.y)
        self.shootAngle = v1.angle(v2) * 180.0 / PI

        super().shootBullet()
