from classes.BaseItem import BaseItem


class WeaponItem(BaseItem):

    def __init__(self, ResourceLocation, texture, damage, weaponRange):
        super().__init__(ResourceLocation, texture)
        self.damage = damage
        self.weaponRange = weaponRange


    def attack(self):
        pass