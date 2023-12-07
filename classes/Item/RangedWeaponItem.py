from classes.Item.WeaponItem import WeaponItem


class RangedWeaponItem(WeaponItem):

    def __init__(self, ResourceLocation, texture, itemName, damage, weaponRange, knockback, weaponCooldown):
        super().__init__(ResourceLocation, texture, itemName, damage, weaponRange, knockback, weaponCooldown)
        self.activeProjectiles = []


    def ticker(self):
        if self.weaponCooldownTimer > 0:
            self.weaponCooldownTimer -= 1
        for projectile in self.activeProjectiles:
            projectile.ticker()

    def attack(self, userCollisionBox, userX, userY, facing):
        if self.weaponCooldownTimer == 0:
            pass