import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)

    #이미지 세팅
    def setImg(self, img):
        self.img = pygame.image.load(img)

    """
    function draw
    object 객체를 화면에 그린다.
    self = self
    x = 이미지가 나타날 x좌표
    y = 이미지가 나타날 y좌표
    screen = 이미지를 그릴 화면
    """
    def render(self,screen):
        screen.blit(self.img, (self.x, self.y))
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)

    def getWidth(self):
        return self.img.get_width()
    def getHeight(self):
        return self.img.get_height()