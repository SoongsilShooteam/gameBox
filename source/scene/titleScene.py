from source.scene.sceneManager import *
from source.object.object import Object
import os

os.chdir(os.getcwd())
print(os.getcwd())


class TitleScene(SceneManager):
    def __init__(self, screen):
        SceneManager.__init__(self)

        self.menu = [None, None, None]
        for i in range(0, 3):
            self.menu[i] = (Object(0, 0, "images/menu.png"))
            #self.menu[i].setImg("images/menu.png") #지울 예정
            self.menu[i].x = 0.5 * screen.get_width()
            self.menu[i].y = 0.5 * screen.get_height() + i * 100
            self.menu[i].update()

    def process(self, events):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.fill((255, 255, 255))

        for i in range(3):
            self.menu[i].render(screen)

