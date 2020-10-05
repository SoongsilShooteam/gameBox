from source.scene.sceneManager import *
from source.object.object import Object


class TitleScene(SceneManager):
    def __init__(self):
        super().__init__()
        #self.spriteGroup = spriteGroup
        self.img = 'assets/images/title.png'
        self.image = pygame.image.load(self.img)
        self.x = 0.5 * self.image.get_width()
        self.y = 0.5 * self.image.get_height()
        self.now = "title"
        #self.spriteGroup.add(self)

    def update(self):
        super().update()