from source.scene.sceneManager import *
from source.object.object import Object

class TitleScene(SceneManager):
    def __init__(self):
        SceneManager.__init__(self)

    def process(self, events):
        print("process")

    def update(self):
        print("update")

    def render(self, screen):
        screen.fill((255, 255, 255))

        menu = [None, None, None]
        for i in range(0, 3):
            menu[i] = (Object())
            menu[i].setImg("images/menu.png")
            menu[i].render(screen,
                           0.5 * screen.get_width() - 0.5 * menu[i].getWidth(),
                           0.5 * screen.get_height() - 0.5 * menu[i].getHeight() + i * 100)
        menu[i]
        #print("TitleScene")