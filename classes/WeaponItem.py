import pygame
import math


from classes.CollisionBox import CollisionBox
from classes.BaseItem import BaseItem
from classes.Entities.BaseEntity import BaseEntity


class WeaponItem(BaseItem):

    def __init__(self, ResourceLocation, texture, itemName, damage, weaponRange):
        super().__init__(ResourceLocation, texture, itemName)
        self.damage = damage
        self.weaponRange = weaponRange


    def attack(self, userCollisionBox, userX, userY, facing):
        hits = []
        for boxs in CollisionBox.activeBoxs:
            if boxs != userCollisionBox:
                for i in range(-45, 50, 5):
                    if facing == 'U':
                        i += 90
                    elif facing == 'D':
                        i += 270
                    elif facing == 'L':
                        i += 180
                    if boxs.baseRect.clipline(userX, userY, userX+(self.weaponRange * math.cos(math.radians(i))), userY-(self.weaponRange * math.sin(math.radians(i)))) and boxs.baseRect not in hits:
                        hits.append(boxs.baseRect)
                        if isinstance(boxs.boxOf, BaseEntity):
                            boxs.boxOf.hit()
                        else:
                            print("hit")




