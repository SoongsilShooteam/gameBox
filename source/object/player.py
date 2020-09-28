from source.object.object import Object
import pygame
import os

os.chdir(os.getcwd())
print(os.getcwd())


class Player(Object):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2 + 200
        self.speed = 3
        self.image = pygame.image.load("images/player.png")
        #self.setImg("images/player.png")

    def update(self):
        key = pygame.key.get_pressed()

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        if key[pygame.K_LEFT]:
            self.x -= self.speed

        elif key[pygame.K_RIGHT]:
            self.x += self.speed

        elif key[pygame.K_UP]:
            self.y -= self.speed

        elif key[pygame.K_DOWN]:
            self.y += self.speed
