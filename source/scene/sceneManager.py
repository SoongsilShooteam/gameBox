
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
        self.nextScene = None
        self.currentScene = None
        self.gameLevel = 1
        self.score = 0


    def process(self, events):   #필요성 검토 중
        pass

    def update(self):
        if self.nextScene is not None:
            self.currentScene = self.nextScene
            self.nextScene = None

        if self.currentScene is not None:
            self.currentScene.update()

    def render(self):
        self.currentScene.render()
        #screen.blit(self.image, self.rect)

    def setScene(self, scene):
        #self.screen.fill((0, 0, 0))
        self.nextScene = scene

    def addEnemy(self, enemy):
        self.currentScene.enemyList.append(enemy)

    def addEnemyBullet(self, enemyBullet):
        self.currentScene.enemyBulletList.append(enemyBullet)

    def removeEnemy(self, enemy):
        self.currentScene.removeEnemy(enemy)

    def getPlayer(self):
        return self.currentScene.player

    def getEnemyList(self):
        return self.currentScene.enemyList

