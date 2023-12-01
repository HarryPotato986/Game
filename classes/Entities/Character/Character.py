import math

import pygame
from classes.CollisionBox import CollisionBox
from classes.Entities.BaseEntity import BaseEntity
from classes.WeaponItem import WeaponItem


class Character(BaseEntity):

    def __init__(self, surface, x, y, resourceLocation, textures, scale, name, weapon):
        super().__init__(surface, x, y, resourceLocation, textures, scale, name, weapon)


    def draw(self):
        for i in range(-45, 50, 5):
            if self.facing == 'U':
                i += 90
            elif self.facing == 'D':
                i += 270
            elif self.facing == 'L':
                i += 180
            pygame.draw.line(self.surface, "red", (self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery),
                             (self.collisionBox.baseRect.centerx+(self.weapon.weaponRange * math.cos(math.radians(i))),
                              self.collisionBox.baseRect.centery-(self.weapon.weaponRange * math.sin(math.radians(i)))))
        self.surface.blit(self.activeTexture, self.collisionBox.baseRect)

    def inputHandler(self, keys, dt):
        self.__movement(keys, dt)

    def __movement(self, keys, dt):
        if keys[pygame.K_w]:
            self.facing = 'U'
            self.collisionBox.baseRect.y -= 300 * dt
            if self.activeTexture not in self.textureHandler.walkUp:
                self.activeTexture = self.textureHandler.walkUp[0]
            elif self.walkAnimationTimer == 0:
                if self.activeTexture == self.textureHandler.walkUp[0]:
                    self.activeTexture = self.textureHandler.walkUp[1]
                    self.walkAnimationTimer = 15
                elif self.activeTexture == self.textureHandler.walkUp[1]:
                    self.activeTexture = self.textureHandler.walkUp[0]
                    self.walkAnimationTimer = 15
            else:
                self.walkAnimationTimer -=1
        if keys[pygame.K_s]:
            self.facing = 'D'
            self.collisionBox.baseRect.y += 300 * dt
            if self.activeTexture not in self.textureHandler.walkDown:
                self.activeTexture = self.textureHandler.walkDown[0]
            elif self.walkAnimationTimer == 0:
                if self.activeTexture == self.textureHandler.walkDown[0]:
                    self.activeTexture = self.textureHandler.walkDown[1]
                    self.walkAnimationTimer = 15
                elif self.activeTexture == self.textureHandler.walkDown[1]:
                    self.activeTexture = self.textureHandler.walkDown[0]
                    self.walkAnimationTimer = 15
            else:
                self.walkAnimationTimer -=1
        if keys[pygame.K_a]:
            self.facing = 'L'
            self.collisionBox.baseRect.x -= 300 * dt
            if self.activeTexture not in self.textureHandler.walkLeft and not keys[pygame.K_w] and not keys[pygame.K_s]:
                self.activeTexture = self.textureHandler.walkLeft[0]
            elif self.walkAnimationTimer == 0:
                if self.activeTexture == self.textureHandler.walkLeft[0]:
                    self.activeTexture = self.textureHandler.walkLeft[1]
                    self.walkAnimationTimer = 15
                elif self.activeTexture == self.textureHandler.walkLeft[1]:
                    self.activeTexture = self.textureHandler.walkLeft[0]
                    self.walkAnimationTimer = 15
            else:
                self.walkAnimationTimer -=1
        if keys[pygame.K_d]:
            self.facing = 'R'
            self.collisionBox.baseRect.x += 300 * dt
            if self.activeTexture not in self.textureHandler.walkRight and not keys[pygame.K_w] and not keys[pygame.K_s]:
                self.activeTexture = self.textureHandler.walkRight[0]
            elif self.walkAnimationTimer == 0:
                if self.activeTexture == self.textureHandler.walkRight[0]:
                    self.activeTexture = self.textureHandler.walkRight[1]
                    self.walkAnimationTimer = 15
                elif self.activeTexture == self.textureHandler.walkRight[1]:
                    self.activeTexture = self.textureHandler.walkRight[0]
                    self.walkAnimationTimer = 15
            else:
                self.walkAnimationTimer -=1

        if not (keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]):
            if self.activeTexture in self.textureHandler.walkUp:
                self.activeTexture = self.textureHandler.idleUp
            elif self.activeTexture in self.textureHandler.walkRight:
                self.activeTexture = self.textureHandler.idleRight
            elif self.activeTexture in self.textureHandler.walkLeft:
                self.activeTexture = self.textureHandler.idleLeft
            elif self.activeTexture in self.textureHandler.walkDown:
                self.activeTexture = self.textureHandler.idleDown

        self.checkCollisions(10)


    def attack(self, event):
        if event.key == pygame.K_e:
            if isinstance(self.weapon, WeaponItem):
                self.weapon.attack(self.collisionBox, self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery, self.facing)
