import pygame

from classes.CollisionBox import CollisionBox


class Projectile:

    def __init__(self, ResourceLocation, texture, speed, damage, direction, projectileRange, originX, originY):
        self.texture = pygame.image.load(ResourceLocation + '/' + texture)
        self.collisionBox = CollisionBox(originX, originY, self.texture.get_width(), self.texture.get_height(), self)
        self.speed = speed
        self.damage = damage
        self.direction = direction
        self.projectileRange = projectileRange
        self.originX = originX
        self.originY = originY


    def ticker(self, surface):
        if self.direction == 'U':
            self.collisionBox.baseRect.y -= self.speed
        elif self.direction == 'D':
            self.collisionBox.baseRect.y += self.speed
        elif self.direction == 'L':
            self.collisionBox.baseRect.x -= self.speed
        elif self.direction == 'R':
            self.collisionBox.baseRect.x += self.speed

        surface.blit(self.texture, self.collisionBox.baseRect)
