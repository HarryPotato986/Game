import pygame

from classes.BaseObject import BaseObject
from classes.CollisionBox import CollisionBox
from classes.Entities.BaseEntity import BaseEntity
from classes.Projectile import Projectile


class SingleUseThrowable:

    def __init__(self, resourceLocation, texture, direction, throwRange, originX, originY):
        self.texture = pygame.image.load(resourceLocation + '/' + texture)
        self.texture = pygame.transform.scale_by(self.texture, .5)
        self.collisionBox = CollisionBox(originX - (self.texture.get_width()/2), originY - (self.texture.get_height()/2) - 1, self.texture.get_width(), self.texture.get_height(), self)
        self.throwRange = throwRange
        self.direction = direction
        self.originX = originX
        self.originY = originY
        self.visible = True


        self.dx = 10
        self.animationDX = 10
        self.animationX = originX
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


    def ticker(self, surface, holder):
        if self.direction == 'R':
            if abs(self.animationX - self.originX) <= self.throwRange:
                self.collisionBox.baseRect.x += self.dx
                self.animationX += self.animationDX
                self.collisionBox.baseRect.y = self.originY + (0.002*((self.animationX-self.originX)*(self.animationX-(self.originX+self.throwRange))))
            else:
                self.dx = 0
                self.animationDX = 0
        if self.direction == 'L':
            if abs(self.animationX - self.originX) <= self.throwRange:
                self.collisionBox.baseRect.x -= self.dx
                self.animationX -= self.animationDX
                self.collisionBox.baseRect.y = self.originY + (0.002*((self.animationX-self.originX)*(self.animationX-(self.originX-self.throwRange))))
            else:
                self.dx = 0
                self.animationDX = 0

        entityRect = self.collisionBox.baseRect
        collisionTolerance = self.dx + 1
        if entityRect.right > surface.get_width():
            entityRect.right = surface.get_width()
            self.dx = 0
        if entityRect.left < 0:
            entityRect.left = 0
            self.dx = 0
        if entityRect.bottom > surface.get_height():
            entityRect.bottom = surface.get_height()
            self.dx = 0
        if entityRect.top < 0:
            entityRect.top = 0
            self.dx = 0
        for otherBox in CollisionBox.activeBoxs:
            if otherBox not in [self.collisionBox, holder.collisionBox] and not isinstance(otherBox.boxOf, (Projectile, SingleUseThrowable)) and entityRect.colliderect(otherBox.baseRect):
                if isinstance(otherBox.boxOf, (BaseObject, BaseEntity)):
                    if abs(otherBox.baseRect.top - entityRect.bottom) < collisionTolerance:
                        entityRect.bottom = otherBox.baseRect.top
                        self.dx = 0
                    if abs(otherBox.baseRect.bottom - entityRect.top) < collisionTolerance:
                        entityRect.top = otherBox.baseRect.bottom
                        self.dx = 0
                    if abs(otherBox.baseRect.right - entityRect.left) < collisionTolerance:
                        entityRect.left = otherBox.baseRect.right
                        self.dx = 0
                    if abs(otherBox.baseRect.left - entityRect.right) < collisionTolerance:
                        entityRect.right = otherBox.baseRect.left
                        self.dx = 0

        if self.visible:
            surface.blit(self.texture, self.collisionBox.baseRect)

