from classes.Item.WeaponItem import WeaponItem
from classes.Projectile import Projectile


class RangedWeaponItem(WeaponItem):

    def __init__(self, resourceLocation, texture, itemName, damage, weaponRange, knockback, weaponCooldown, projectileTexture):
        super().__init__(resourceLocation, texture, itemName, damage, weaponRange, knockback, weaponCooldown)
        self.projectileTexture = projectileTexture
        self.activeProjectiles = []


    def ticker(self, surface):
        if self.weaponCooldownTimer > 0:
            self.weaponCooldownTimer -= 1
        for projectile in self.activeProjectiles:
            projectile.ticker(surface)

    def attack(self, userCollisionBox, userX, userY, facing):
        if self.weaponCooldownTimer == 0:
            newProjectile = Projectile(self.resourceLocation + '/' + "projectile_textures", self.projectileTexture, 20, self.damage, facing, self.weaponRange, userX, userY)
            self.activeProjectiles.append(newProjectile)
