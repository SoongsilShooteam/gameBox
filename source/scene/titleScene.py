from source.scene.sceneManager import *
from source.object.object import Object


class TitleScene(SceneManager):
    def __init__(self, screen):
        SceneManager.__init__(self)

        self.menu = [None, None, None]
        for i in range(0, 3):
            self.menu[i] = (Object(0, 0))
            self.menu[i].setImg("images/menu.png")
            self.menu[i].x = 0.5 * screen.get_width()
            self.menu[i].y = 0.5 * screen.get_height() + i * 100
            print(self.menu[i].getHeight())
    def process(self, events):
        pass
        # print("process")

    def update(self):
        pass
        # print("update")

    def render(self, screen):
        screen.fill((255, 255, 255))

        for i in range(3):
            self.menu[i].render(screen)
        # menu[i]
        # print("TitleScene")
