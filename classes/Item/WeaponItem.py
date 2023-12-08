import math


from classes.CollisionBox import CollisionBox
from classes.Item.BaseItem import BaseItem
from classes.Entities.BaseEntity import BaseEntity


class WeaponItem(BaseItem):

    def __init__(self, resourceLocation, texture, itemName, damage, weaponRange, knockback, weaponCooldown):
        super().__init__(resourceLocation, texture, itemName)
        self.damage = damage
        self.weaponRange = weaponRange
        self.knockback = knockback
        self.weaponCooldown = weaponCooldown
        self.weaponCooldownTimer = 0


    def ticker(self, surface):
        if self.weaponCooldownTimer > 0:
            self.weaponCooldownTimer -= 1

    def attack(self, userCollisionBox, userX, userY, facing):
        if self.weaponCooldownTimer == 0:
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
                            self.weaponCooldownTimer = self.weaponCooldown
                            if isinstance(boxs.boxOf, BaseEntity):
                                boxs.boxOf.hit(self.damage, facing, self.knockback)
                            else:
                                print("hit")




