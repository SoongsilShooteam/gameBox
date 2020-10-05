import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(img)

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    """
    오버라이딩 함수 
    function draw
    object 객체를 화면에 그린다.
    self = self
    screen = 이미지를 그릴 화면
    """
    def render(self, screen):
        screen.blit(self.image, self.rect)

    def getWidth(self):
        return self.image.get_width()

    def getHeight(self):
        return self.image.get_height()