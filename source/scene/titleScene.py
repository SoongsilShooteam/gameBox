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
            menu[i] = (Object(0,0))
            menu[i].setImg("images/menu.png")
            menu[i].x=0.5 * screen.get_width() - 0.5 * menu[i].getWidth()
            menu[i].y=0.5 * screen.get_height() + i * 100
            menu[i].render(screen)
        menu[i]
        #print("TitleScene")