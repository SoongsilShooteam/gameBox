import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

    #이미지 세팅
    def setImg(self, img):
        self.img = pygame.image.load(img)

    """
    오버라이딩 함수 
    function draw
    object 객체를 화면에 그린다.
    self = self
    screen = 이미지를 그릴 화면
    """
    def render(self, screen):
        self.rect = self.img.get_rect()
        self.rect.center = (self.x, self.y)

        screen.blit(self.img, self.rect)

    def getWidth(self):
        return self.img.get_width()

    def getHeight(self):
        return self.img.get_height()