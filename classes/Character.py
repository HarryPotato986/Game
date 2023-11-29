import math

import pygame
from classes.BaseObject import BaseObject
from classes.CollisionBox import CollisionBox
from classes.CharacterTextureHandler import CharacterTextureHandler
from classes.WeaponItem import WeaponItem


class Character(BaseObject):

    def __init__(self, surface, x, y, resourceLocation, textures, scale, weapon):
        self.textureHandler = CharacterTextureHandler(resourceLocation, textures[0], textures[1], textures[2], textures[3], textures[4], textures[5], textures[6], textures[7], scale)
        super().__init__(surface, x, y, self.textureHandler.idleDown.get_width(), self.textureHandler.idleDown.get_height())
        self.activeTexture = self.textureHandler.idleDown
        self.walkAnimationTimer = 15
        self.weapon = weapon
        self.facing = 'D'


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

        self.__checkCollisions()


    def __checkCollisions(self):
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

    def attack(self, event):
        if event.key == pygame.K_e:
            if isinstance(self.weapon, WeaponItem):
                self.weapon.attack(self.collisionBox, self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery, self.facing)
