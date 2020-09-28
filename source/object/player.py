from source.object.object import Object
import pygame
import os

os.chdir(os.getcwd())
print(os.getcwd())


class Player(Object):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.screenX, self.screenY = pygame.display.get_surface().get_size()
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
            if (self.x - self.speed) > 0:
                self.x -= self.speed

        elif key[pygame.K_RIGHT]:
            if (self.x + self.speed) < self.screenX:
                self.x += self.speed

        elif key[pygame.K_UP]:
            if (self.y - self.speed) > 0:
                self.y -= self.speed

        elif key[pygame.K_DOWN]:
            if (self.y + self.speed) < self.screenY:
                self.y += self.speed