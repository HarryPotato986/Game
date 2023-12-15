import pygame

from classes.BaseObject import BaseObject
from classes.CollisionBox import CollisionBox
from classes.Entities.BaseEntity import BaseEntity


class Projectile:

    def __init__(self, resourceLocation, texture, speed, damage, knockback, direction, projectileRange, originX, originY):
        self.texture = pygame.image.load(resourceLocation + '/' + texture)
        self.texture = pygame.transform.scale_by(self.texture, .5)
        self.collisionBox = CollisionBox(originX - (self.texture.get_width()/2), originY - (self.texture.get_height()/2), self.texture.get_width(), self.texture.get_height(), self)
        self.speed = speed
        self.damage = damage
        self.knockback = knockback
        self.direction = direction
        self.projectileRange = projectileRange
        self.originX = originX
        self.originY = originY
        self.visible = True

        self.dx = 0
        self.dy = 0
        if direction == 'U':
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
            self.dx = speed


    def ticker(self, surface, parentWeapon, holder):
        self.collisionBox.baseRect.x += self.dx
        self.collisionBox.baseRect.y += self.dy


        if not (self.dx == 0 and self.dy == 0):
            if abs(self.collisionBox.baseRect.x - self.originX) >= self.projectileRange or abs(self.collisionBox.baseRect.y - self.originY) >= self.projectileRange:
                if self.direction == 'L':
                    self.texture = pygame.transform.rotate(self.texture, 45)
                elif self.direction == 'R':
                    self.texture = pygame.transform.rotate(self.texture, -45)
                self.dx = 0
                self.dy = 0

            entityRect = self.collisionBox.baseRect
            collisionTolerance = self.speed + 1
            if entityRect.right > surface.get_width():
                entityRect.right = surface.get_width()
                self.dx = 0
                self.dy = 0
            if entityRect.left < 0:
                entityRect.left = 0
                self.dx = 0
                self.dy = 0
            if entityRect.bottom > surface.get_height():
                entityRect.bottom = surface.get_height()
                self.dx = 0
                self.dy = 0
            if entityRect.top < 0:
                entityRect.top = 0
                self.dx = 0
                self.dy = 0
            for otherBox in CollisionBox.activeBoxs:
                if otherBox not in [self.collisionBox, holder.collisionBox] and not isinstance(otherBox.boxOf, Projectile) and entityRect.colliderect(otherBox.baseRect):
                    if isinstance(otherBox.boxOf, BaseEntity):
                        otherBox.boxOf.hit(self.damage, self.direction, self.knockback)
                        self.collisionBox.deactivate()
                        parentWeapon.activeProjectiles.remove(self)
                    elif isinstance(otherBox.boxOf, BaseObject):
                        if abs(otherBox.baseRect.top - entityRect.bottom) < collisionTolerance:
                            entityRect.bottom = otherBox.baseRect.top
                            self.dx = 0
                            self.dy = 0
                        if abs(otherBox.baseRect.bottom - entityRect.top) < collisionTolerance:
                            entityRect.top = otherBox.baseRect.bottom
                            self.dx = 0
                            self.dy = 0
                        if abs(otherBox.baseRect.right - entityRect.left) < collisionTolerance:
                            entityRect.left = otherBox.baseRect.right
                            self.dx = 0
                            self.dy = 0
                        if abs(otherBox.baseRect.left - entityRect.right) < collisionTolerance:
                            entityRect.right = otherBox.baseRect.left
                            self.dx = 0
                            self.dy = 0
        elif self.dx == 0 and self.dy == 0:
            entityRect = self.collisionBox.baseRect
            for otherBox in CollisionBox.activeBoxs:
                if otherBox == holder.collisionBox and entityRect.colliderect(otherBox.baseRect):
                    self.collisionBox.deactivate()
                    parentWeapon.activeProjectiles.remove(self)
                    holder.rangedWeapon[1] += 1

        surface.blit(self.texture, self.collisionBox.baseRect)


