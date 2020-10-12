
import pygame

def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper


@singleton
class SceneManager:
    def __init__(self):
        print("********** Init SceneManager **********")
        self.scene = None

    def process(self, events):   #필요성 검토 중
        pass

    def update(self):
        if self.scene is not None:
            self.scene.update()

    def render(self):
        self.scene.render()
        #screen.blit(self.image, self.rect)

    def setScene(self, scene):
        self.scene = scene

    def addEnemy(self, enemy):
        self.scene.enemyList.append(enemy)

    def addEnemyBullet(self, enemyBullet):
        self.scene.enemyBulletList.append(enemyBullet)

    def removeEnemy(self, enemy):
        self.scene.removeEnemy(enemy)

    def getPlayer(self):
        return self.scene.player

    def getEnemyList(self):
        return self.scene.enemyList
