from source.scene.sceneManager import *


class StageOneScene(SceneManager):
    def __init__(self):
        SceneManager.__init__(self)

    def process(self, events):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.fill((100, 100, 100))