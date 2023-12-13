import math

import pygame

from classes.BaseObject import BaseObject
from classes.CollisionBox import CollisionBox
from classes.Entities.BaseEntity import BaseEntity
from classes.Projectile import Projectile


class SingleUseThrowable:

    def __init__(self, resourceLocation, texture, damage, direction, throwRange, AOERadius, knockback, originX, originY):
        self.texture = pygame.image.load(resourceLocation + '/' + texture)
        self.texture = pygame.transform.scale_by(self.texture, .5)
        self.collisionBox = CollisionBox(originX - (self.texture.get_width()/2), originY - (self.texture.get_height()/2) - 1, self.texture.get_width(), self.texture.get_height(), self)
        self.damage = damage
        self.throwRange = throwRange
        self.direction = direction
        self.AOERadius = AOERadius
        self.knockback = knockback
        self.originX = originX
        self.originY = originY
        self.visible = True


        self.dx = 10
        self.animationDX = 10
        self.animationX = originX


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
        collisionTolerance = self.dx + 10
        if entityRect.right > surface.get_width():
            entityRect.right = surface.get_width()
            self.dx = 0
        elif entityRect.left < 0:
            entityRect.left = 0
            self.dx = 0
        elif entityRect.bottom > surface.get_height():
            entityRect.bottom = surface.get_height()
            self.dx = 0
        elif entityRect.top < 0:
            entityRect.top = 0
            self.dx = 0
        for otherBox in CollisionBox.activeBoxs:
            if otherBox not in [self.collisionBox, holder.collisionBox] and not isinstance(otherBox.boxOf, (Projectile, SingleUseThrowable)) and entityRect.colliderect(otherBox.baseRect):
                if isinstance(otherBox.boxOf, (BaseObject, BaseEntity)):
                    if abs(otherBox.baseRect.top - entityRect.bottom) < collisionTolerance:
                        entityRect.bottom = otherBox.baseRect.top
                        self.dx = 0
                        self.animationDX = 0
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
            for i in range(0, 365, 5):
                pygame.draw.line(surface, "blue", (self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery),
                                 (self.collisionBox.baseRect.centerx+(self.AOERadius * math.cos(math.radians(i))),
                                  self.collisionBox.baseRect.centery-(self.AOERadius * math.sin(math.radians(i)))))

        if self.dx == 0 and self.animationDX == 0:
            hits = []
            x = self.collisionBox.baseRect.centerx
            y = self.collisionBox.baseRect.centery
            for boxs in CollisionBox.activeBoxs:
                if boxs != holder.collisionBox and not isinstance(boxs.boxOf, (Projectile, SingleUseThrowable)):
                    for i in range(0, 365, 5):
                        if i >= 315 or i <= 45:
                            facing = 'R'
                        elif i >= 135 and i <= 225:
                            facing = 'L'
                        elif i > 45 and i < 135:
                            facing = 'U'
                        elif i > 225 and i < 315:
                            facing = 'D'
                        else:
                            facing = 'R'
                        if boxs.baseRect.clipline(x, y, x+(self.AOERadius * math.cos(math.radians(i))), y-(self.AOERadius * math.sin(math.radians(i)))) and boxs.baseRect not in hits:
                            hits.append(boxs.baseRect)
                            if isinstance(boxs.boxOf, BaseEntity):
                                boxs.boxOf.hit(self.damage, facing, self.knockback)
                            else:
                                print("hit")

            self.collisionBox.deactivate()
            holder.activeThrowables.remove(self)
