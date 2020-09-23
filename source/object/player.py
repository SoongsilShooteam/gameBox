# from source.object.object import Object
import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        pygame.sprite.Sprite.__init__(self)

    def setImg(self,img):
        self.img = pygame.image.load(img)

    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))
        self.rect = self.img.get_rect()
        self.rect.center = (self.x,self.y)

    def update(self, key):
        if key[pygame.K_LEFT]:
            self.x-=3
            print(self.x)
        elif key[pygame.K_RIGHT]:
            self.x+=3
            print(self.x)
        elif key[pygame.K_UP]:
            self.y-=3
            print(self.y)
        elif key[pygame.K_DOWN]:
            self.y+=3
            print(self.y)