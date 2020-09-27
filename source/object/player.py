from source.object.object import Object
import pygame


class Player(Object):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2 + 200


    def setImg(self, img):
        self.img = pygame.image.load(img)

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.x -= 3
            #print(self.x)
        elif key[pygame.K_RIGHT]:
            self.x += 3
            #print(self.x)
        elif key[pygame.K_UP]:
            self.y -= 3
            #print(self.y)
        elif key[pygame.K_DOWN]:
            self.y += 3
            #print(self.y)