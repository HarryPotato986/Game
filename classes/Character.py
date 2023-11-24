import pygame
from classes.BaseObject import BaseObject
from classes.CollisionBox import CollisionBox


class Character(BaseObject):

    def __init__(self, surface, colour, x, y, width, height):
        super().__init__(surface, colour, x, y, width, height)
        print(self)


    def movement(self, keys, dt):
        if keys[pygame.K_w]:
            self.collisionBox.baseRect.y -= 300 * dt
        if keys[pygame.K_s]:
            self.collisionBox.baseRect.y += 300 * dt
        if keys[pygame.K_a]:
            self.collisionBox.baseRect.x -= 300 * dt
        if keys[pygame.K_d]:
            self.collisionBox.baseRect.x += 300 * dt

        self.checkCollisions()


    def checkCollisions(self):
        characterRect = self.collisionBox.baseRect
        collisionTolerance = 10
        if characterRect.right > self.surface.get_width():
            characterRect.right = self.surface.get_width()
        if characterRect.left < 0:
            characterRect.left = 0
        if characterRect.bottom > self.surface.get_height():
            characterRect.bottom = self.surface.get_height()
        if characterRect.top < 0:
            characterRect.top = 0
        for otherBox in CollisionBox.activeBoxs:
            if otherBox != self.collisionBox and characterRect.colliderect(otherBox.baseRect):
                if abs(otherBox.baseRect.top - characterRect.bottom) < collisionTolerance:
                    characterRect.bottom = otherBox.baseRect.top
                if abs(otherBox.baseRect.bottom - characterRect.top) < collisionTolerance:
                    characterRect.top = otherBox.baseRect.bottom
                if abs(otherBox.baseRect.right - characterRect.left) < collisionTolerance:
                    characterRect.left = otherBox.baseRect.right
                if abs(otherBox.baseRect.left - characterRect.right) < collisionTolerance:
                    characterRect.right = otherBox.baseRect.left
