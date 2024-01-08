import math

import pygame
from classes.Entities.BaseEntity import BaseEntity
from classes.Item.RangedWeaponItem import RangedWeaponItem
from classes.Item.ThrowableWeaponItem import ThrowableWeaponItem
from classes.Item.WeaponItem import WeaponItem


class Character(BaseEntity):

    def __init__(self, surface, x, y, resourceLocation, textures, scale, name, meleeWeapon, rangedWeapon, singleUseItem, maxHealth):
        super().__init__(surface, x, y, resourceLocation, textures, scale, name, meleeWeapon, maxHealth)
        self.meleeWeapon = meleeWeapon
        self.rangedWeapon = rangedWeapon
        self.singleUseSlot = singleUseItem
        self.meleeWeaponTexture = pygame.image.load(meleeWeapon.resourceLocation + '/' + meleeWeapon.texture)
        self.meleeWeaponTexture = pygame.transform.scale_by(self.meleeWeaponTexture, 65/self.meleeWeaponTexture.get_width())
        self.rangedWeaponTexture = pygame.image.load(rangedWeapon[0].resourceLocation + '/' + rangedWeapon[0].texture)
        self.rangedWeaponTexture = pygame.transform.scale_by(self.rangedWeaponTexture, 65/self.rangedWeaponTexture.get_width())
        self.singleUseWeaponTexture = pygame.image.load(singleUseItem[0].resourceLocation + '/' + singleUseItem[0].texture)
        self.singleUseWeaponTexture = pygame.transform.scale_by(self.singleUseWeaponTexture, 65/self.singleUseWeaponTexture.get_width())

        self.inventoryFont = pygame.font.SysFont("arial.ttf", 60)


    def draw(self):
        if isinstance(self.activeWeapon, RangedWeaponItem):
            if self.facing == 'U':
                pygame.draw.line(self.surface, "red", (self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery),
                                 (self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery - self.activeWeapon.weaponRange))
            elif self.facing == 'D':
                pygame.draw.line(self.surface, "red", (self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery),
                                 (self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery + self.activeWeapon.weaponRange))
            elif self.facing == 'L':
                pygame.draw.line(self.surface, "red", (self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery),
                                 (self.collisionBox.baseRect.centerx - self.activeWeapon.weaponRange, self.collisionBox.baseRect.centery))
            elif self.facing == 'R':
                pygame.draw.line(self.surface, "red", (self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery),
                                 (self.collisionBox.baseRect.centerx + self.activeWeapon.weaponRange, self.collisionBox.baseRect.centery))
        elif isinstance(self.activeWeapon, WeaponItem):
            for i in range(-45, 50, 5):
                if self.facing == 'U':
                    i += 90
                elif self.facing == 'D':
                    i += 270
                elif self.facing == 'L':
                    i += 180
                pygame.draw.line(self.surface, "red", (self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery),
                                 (self.collisionBox.baseRect.centerx+(self.activeWeapon.weaponRange * math.cos(math.radians(i))),
                                  self.collisionBox.baseRect.centery-(self.activeWeapon.weaponRange * math.sin(math.radians(i)))))
        self.surface.blit(self.activeTexture, self.collisionBox.baseRect)
        self.drawHotbar()

    def refreshItemTextures(self):
        self.meleeWeaponTexture = pygame.image.load(self.meleeWeapon.resourceLocation + '/' + self.meleeWeapon.texture)
        self.meleeWeaponTexture = pygame.transform.scale_by(self.meleeWeaponTexture, 65/self.meleeWeaponTexture.get_width())
        self.rangedWeaponTexture = pygame.image.load(self.rangedWeapon[0].resourceLocation + '/' + self.rangedWeapon[0].texture)
        self.rangedWeaponTexture = pygame.transform.scale_by(self.rangedWeaponTexture, 65/self.rangedWeaponTexture.get_width())
        if isinstance(self.singleUseSlot, list):
            self.singleUseWeaponTexture = pygame.image.load(self.singleUseSlot[0].resourceLocation + '/' + self.singleUseSlot[0].texture)
            self.singleUseWeaponTexture = pygame.transform.scale_by(self.singleUseWeaponTexture, 65/self.singleUseWeaponTexture.get_width())
        else:
            self.singleUseWeaponTexture = None

    def drawHotbar(self):
        meleeSlot = pygame.draw.rect(self.surface, "light grey", (20, 20, 75, 75), border_radius=12)
        rangedSlot = pygame.draw.rect(self.surface, "light grey", (115, 20, 75, 75), border_radius=12)
        singleUseSlot = pygame.draw.rect(self.surface, "light grey", (210, 20, 75, 75), border_radius=12)

        meleeItemRect = pygame.Rect(0, 0, 65, 65)
        meleeItemRect.centerx = meleeSlot.centerx
        meleeItemRect.centery = meleeSlot.centery
        rangedItemRect = pygame.Rect(0, 0, 65, 65)
        rangedItemRect.centerx = rangedSlot.centerx
        rangedItemRect.centery = rangedSlot.centery
        singleUseItemRect = pygame.Rect(0, 0, 65, 65)
        singleUseItemRect.centerx = singleUseSlot.centerx
        singleUseItemRect.centery = singleUseSlot.centery

        rangedItemNum = self.inventoryFont.render(str(self.rangedWeapon[1]), True, "black")
        if isinstance(self.singleUseSlot, list):
            singleUseItemNum = self.inventoryFont.render(str(self.singleUseSlot[1]), True, "black")
        else:
            singleUseItemNum = None

        self.surface.blit(self.meleeWeaponTexture, meleeItemRect)
        self.surface.blit(self.rangedWeaponTexture, rangedItemRect)
        self.surface.blit(rangedItemNum, (rangedItemRect.centerx + 10, rangedItemRect.centery))
        if isinstance(self.singleUseWeaponTexture, pygame.surface.Surface):
            self.surface.blit(self.singleUseWeaponTexture, singleUseItemRect)
            if singleUseItemNum is not None:
                self.surface.blit(singleUseItemNum, (singleUseItemRect.centerx + 10, singleUseItemRect.centery))

    def ticker(self, keys, dt):
        if isinstance(self.meleeWeapon, WeaponItem):
            self.meleeWeapon.ticker(self.surface, self)
        if isinstance(self.rangedWeapon, list):
            if isinstance(self.rangedWeapon[0], WeaponItem):
                self.rangedWeapon[0].ticker(self.surface, self)
        if isinstance(self.singleUseSlot, list):
            if isinstance(self.singleUseSlot[0], ThrowableWeaponItem):
                self.singleUseSlot[0].ticker(self.surface, self)
        for throwable in self.activeThrowables:
            throwable.ticker(self.surface, self)
        self.__movement(keys, dt)
        self.draw()

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
            if isinstance(self.activeWeapon, ThrowableWeaponItem):
                self.activeWeapon.attack(self.collisionBox, self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery, self.facing)
                self.singleUseSlot[1] -= 1
                if self.singleUseSlot[1] == 0:
                    self.singleUseSlot = None
                    self.activeWeapon = None
                    self.refreshItemTextures()
            elif isinstance(self.activeWeapon, RangedWeaponItem):
                self.activeWeapon.attack(self, self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery, self.facing)
            elif isinstance(self.activeWeapon, WeaponItem):
                self.activeWeapon.attack(self.collisionBox, self.collisionBox.baseRect.centerx, self.collisionBox.baseRect.centery, self.facing)

    def changeActiveSlot(self, event):
        if event.key == pygame.K_1:
            self.activeWeapon = self.meleeWeapon
        elif event.key == pygame.K_2:
            if isinstance(self.rangedWeapon, list):
                self.activeWeapon = self.rangedWeapon[0]
            else:
                self.activeWeapon = self.rangedWeapon
        elif event.key == pygame.K_3:
            if isinstance(self.singleUseSlot, list):
                self.activeWeapon = self.singleUseSlot[0]
            else:
                self.activeWeapon = self.singleUseSlot
