from source.object.object import Object
import pygame
import os

os.chdir(os.getcwd())
print(os.getcwd())


class Player(Object):
    def __init__(self, screen, spriteGroup):
        super().__init__(screen.get_width() / 2, screen.get_height() / 2 + 200, "assets/images/player.png")
        self.spriteGroup = spriteGroup
        self.screenX, self.screenY = pygame.display.get_surface().get_size()
        self.speed = 5
        self.bullets = []
        #self.setImg("images/player.png")

    def update(self):
        super().update()
        key = pygame.key.get_pressed()

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        if key[pygame.K_LEFT]:
            if (self.x - self.speed) > 0:
                self.x -= self.speed

        if key[pygame.K_RIGHT]:
            if (self.x + self.speed) < self.screenX:
                self.x += self.speed

        if key[pygame.K_UP]:
            if (self.y - self.speed) > 0:
                self.y -= self.speed

        if key[pygame.K_DOWN]:
            if (self.y + self.speed) < self.screenY:
                self.y += self.speed

        if key[pygame.K_SPACE] :
            bullet = Player_Bullet(self.x, self.y)
            self.spriteGroup.add(bullet)
            Player_Bullet.update(bullet)


class Player_Bullet(Object):
    def __init__(self,x,y):
        super().__init__(x,y, "assets/images/player_bullet.png")
        self.speed = 10
        #self.setImg("images/player.png")

    def uddd(self):
        self.update()

    def update(self):
        super().update()
        key = pygame.key.get_pressed()

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.y -= self.speed


