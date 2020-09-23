from source.object.object import Object
import pygame

class Player(Object): #Object class 상속

    def __init__(self):
        Object.__init__(self)

        self.x=100
        self.y=400

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