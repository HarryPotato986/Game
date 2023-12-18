from classes.Item.RangedWeaponItem import RangedWeaponItem
from classes.Item.SingleUseThrowable import SingleUseThrowable


class ThrowableWeaponItem(RangedWeaponItem):

    def __init__(self, resourceLocation, texture, itemName, damage, weaponRange, AOERadius, knockback, weaponCooldown, projectileTexture):
        super().__init__(resourceLocation, texture, itemName, damage, weaponRange, knockback, weaponCooldown, projectileTexture)
        self.AOERadius = AOERadius


    def ticker(self, surface, holder):
        if self.weaponCooldownTimer > 0:
            self.weaponCooldownTimer -= 1

    def attack(self, userCollisionBox, userX, userY, facing):
        if self.weaponCooldownTimer == 0:
            newProjectile = SingleUseThrowable(self.resourceLocation, self.projectileTexture, self.damage, facing, self.weaponRange, self.AOERadius, self.knockback, userX, userY)
            userCollisionBox.boxOf.activeThrowables.append(newProjectile)
            self.weaponCooldownTimer = self.weaponCooldown
