import pygame

from classes.CollisionBox import CollisionBox


class SingleUseThrowable:

    def __init__(self, resourceLocation, texture, itemName, originX, originY):
        self.texture = pygame.image.load(resourceLocation + '/' + texture)
        self.texture = pygame.transform.scale_by(self.texture, .5)
        self.collisionBox = CollisionBox(originX - (self.texture.get_width()/2), originY - (self.texture.get_height()/2) - 1, self.texture.get_width(), self.texture.get_height(), self)
        self.originX = originX
        self.originY = originY
        self.visible = True


        self.dx = 10
        self.dy = 25
        '''if direction == 'U':
            self.dy = -speed
            self.texture = pygame.transform.rotate(self.texture, 90)
            self.collisionBox.resize(self.texture.get_width(), self.texture.get_height())
            self.collisionBox.baseRect.centerx = originX
            self.collisionBox.baseRect.centery = originY
        elif direction == 'D':
            self.dy = speed
            self.texture = pygame.transform.rotate(self.texture, -90)
            self.collisionBox.resize(self.texture.get_width(), self.texture.get_height())
            self.collisionBox.baseRect.centerx = originX
            self.collisionBox.baseRect.centery = originY
        elif direction == 'L':
            self.dx = -speed
            self.texture = pygame.transform.rotate(self.texture, 180)
        elif direction == 'R':
            self.dx = speed'''


    def ticker(self, surface):
        if abs(self.collisionBox.baseRect.x - self.originX) <= 400:
            self.collisionBox.baseRect.x += self.dx
            x = self.collisionBox.baseRect.x
            self.collisionBox.baseRect.y = self.originY + (0.002*((x-self.originX)*(x-(self.originX+400))))
        else:
            self.dx = 0
            self.dy = 0

        if self.visible:
            surface.blit(self.texture, self.collisionBox.baseRect)

