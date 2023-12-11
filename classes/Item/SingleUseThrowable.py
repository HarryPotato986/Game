import pygame

from classes.CollisionBox import CollisionBox


class SingleUseThrowable:

    def __init__(self, resourceLocation, texture, itemName):
        self.texture = pygame.image.load(resourceLocation + '/' + texture)
        self.texture = pygame.transform.scale_by(self.texture, .5)
        self.collisionBox = CollisionBox(-10, -10, self.texture.get_width(), self.texture.get_height(), self)
        self.dx = 0
        self.dy = 0
        self.visible = False


    def ticker(self, surface):
        if self.visible:
            surface.blit(self.texture, self.collisionBox.baseRect)

    def throw(self, userCenterX, userCenterY, user):
        self.collisionBox.baseRect.centerx = userCenterX
        self.collisionBox.baseRect.centery = userCenterY
        self.visible = True

