import pygame

class Object:
    def __init__(self) :
        self.x=0
        self.y=0

    #이미지 세팅
    def setImg(self, img) :
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(img).convert()

    """
    function draw
    object 객체를 화면에 그린다.
    self = self
    x = 이미지가 나타날 x좌표
    y = 이미지가 나타날 y좌표
    screen = 이미지를 그릴 화면
    """
    def render(self,screen,x=None,y=None):
        if x:
            self.x=x
        if y:
            self.y=y
        screen.blit(self.img,(self.x,self.y))

    def getWidth(self):
        return self.img.get_width()
    def getHeight(self):
        return self.img.get_height()