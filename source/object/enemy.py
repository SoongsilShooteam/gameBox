import pygame
import os
import math
import random
from source.const import PI
from source.vector import Vector2
from source.object.object import Object
from source.scene.stageOneScene import *
from source.scene import sceneManager

class BossEnemyHpBar:
    def __init__(self, spriteGroup, enemy):
        self.enemy = enemy
        self.enemyMaxHp = enemy.hp
        self.enemyPrevHp = enemy.hp
        self.spriteGroup = spriteGroup

        self.hpGuageBarBg = Object(0, 0, "assets/images/hp_bar_guage2.png")
        self.hpGuageBar = Object(0, 0, "assets/images/hp_bar_guage.png")
        self.originalHpGuageBarImage = self.hpGuageBar.image
        self.hpGuageBarEdge = Object(0, 0, "assets/images/hp_bar_edge.png")

        screenSize = pygame.display.get_surface().get_size()
        self.hpGuageBarBg.x = screenSize[0] / 2 + 17
        self.hpGuageBarBg.y = 55
        self.hpGuageBar.x = screenSize[0] / 2 + 17
        self.originalHpGuageBarX = self.hpGuageBar.x
        self.hpGuageBar.y = 55
        self.hpGuageBarEdge.x = screenSize[0] / 2
        self.hpGuageBarEdge.y = 55

        self.spriteGroup.add(self.hpGuageBarBg)
        self.spriteGroup.add(self.hpGuageBar)
        self.spriteGroup.add(self.hpGuageBarEdge)
        self.hpGuageBarBg.update()
        self.hpGuageBar.update()
        self.hpGuageBarEdge.update()

    def __del__(self):
        self.spriteGroup.remove(self.hpGuageBarBg)
        self.spriteGroup.remove(self.hpGuageBar)
        self.spriteGroup.remove(self.hpGuageBarEdge)

    def update(self):
        # 적 Hp에 변화가 생겼다면
        if self.enemyPrevHp is not self.enemy.hp:
            hpGuageBarWidth = int(self.lerp(self.originalHpGuageBarImage.get_rect().width, 0, 1.0 - self.enemy.hp / self.enemyMaxHp))
            self.hpGuageBar.image = pygame.transform.scale(self.originalHpGuageBarImage, (hpGuageBarWidth, self.originalHpGuageBarImage.get_rect().height))
            self.hpGuageBar.x = self.originalHpGuageBarX - (self.originalHpGuageBarImage.get_rect().width - self.hpGuageBar.image.get_rect().width) / 2
            self.enemyPrevHp = self.enemy.hp

    def lerp(self, fromValue, toValue, t):
        return fromValue + (toValue - fromValue) * t

# 적이 쏘는 총알
class EnemyBullet(Object):
    def __init__(self, spriteGroup, x, y, angle, angleRate, speed, speedRate, bulletImg):
        self.spriteGroup = spriteGroup
        self.angle = angle  # 총알이 나아가는 각도
        self.angleRate = angleRate  # 프레임당 각도 변화율
        self.speed = speed  # 총알이 나아가는 속도
        self.speedRate = speedRate  # 프레임당 속도 변화율
        self.screenSize = pygame.display.get_surface().get_size()
        self.sceneManager = sceneManager.SceneManager()
        self.player = self.sceneManager.getPlayer()
        super().__init__(x, y, bulletImg)

        # 총알 회전도에 따라서 image 회전
        imageAngle = self.angle
        if imageAngle < 0.0:
            imageAngle += 360.0
        self.image = pygame.transform.rotate(self.image, (360 - imageAngle) + 90)

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
            self.kill()
            self.player.onHitEnemyBullet()

# 모든 적이 상속받는 공통 클래스
class Enemy(Object):
    def __init__(self, spriteGroup, hp, moveSpeed, x, y, img, bulletImg):
        self.spriteGroup = spriteGroup
        self.screenSize = pygame.display.get_surface().get_size()
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
        self.bulletImg = bulletImg
        super().__init__(x, y, img)

        spriteGroup.add(self)

    def update(self):
        super().update()

        currentTime = pygame.time.get_ticks()
        if (currentTime - self.lastTime) / 1000.0 >= self.shootInterval:
            self.shootBullet()
            self.lastTime = currentTime

        self.checkDestroyMe()

    # 적이 화면 밖으로 나가면 파괴되어야 하는데, 이를 처리해주는 함수
    def checkDestroyMe(self):
        if self.y > self.screenSize[1] + 50:
            self.kill()
            self.sceneManager.removeEnemy(self)

    def onHitPlayerBullet(self):
        self.hp -= 1
        if self.hp == 0:
            self.sceneManager.removeEnemy(self)

    def shootBullet(self):
        bullet = EnemyBullet(self.spriteGroup, self.x, self.y, self.shootAngle, self.shootAngleRate, self.shootSpeed,self.shootSpeedRate, self.bulletImg)
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
        super().__init__(spriteGroup, 100, 0, x, y, "assets/images/boss01.png", "assets/images/boss_bullet.png")
        self.image = pygame.transform.scale(self.image, (140, 100))
        self.n = n
        self.lastTime2 = currentTime = pygame.time.get_ticks()
        self.bossEnemyHpBar = BossEnemyHpBar(spriteGroup, self)

    def update(self):
        super().update()
        self.shootAngle += 3

        if self.y < 130:
            self.y += 1.0

        if self.bossEnemyHpBar is not None:
            self.bossEnemyHpBar.update()

    def onHitPlayerBullet(self):
        super().onHitPlayerBullet()

        if self.hp <= 0:
            del self.bossEnemyHpBar
            self.bossEnemyHpBar = None

    def shootBullet(self):
        for i in range(self.n):
            super().shootBullet()
            self.shootAngle += 360.0 / self.n

        # 유도탄 팔사
        currentTime = pygame.time.get_ticks()
        if (currentTime - self.lastTime2) / 1000.0 >= 1.0:
            prevShootAngle = self.shootAngle

            v1 = Vector2(self.x, self.y)
            v2 = Vector2(self.player.x, self.player.y)
            self.shootAngle = v1.angle(v2) * 180.0 / PI
            super().shootBullet()

            self.shootAngle = prevShootAngle
            self.lastTime2 = currentTime

# 유저가 있는 방향으로 탄을 발사하는 적
class NormalEnemy(Enemy):
    def __init__(self, spriteGroup, x, y):
        super().__init__(spriteGroup, 1, 0, x, y, "assets/images/enemy01.png", "assets/images/enemy_bullet.png")
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
