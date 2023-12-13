from classes.Item.RangedWeaponItem import RangedWeaponItem
from classes.Item.SingleUseThrowable import SingleUseThrowable
from classes.Item.ThrowableWeaponItem import ThrowableWeaponItem
from classes.Item.WeaponItem import WeaponItem

testSword = WeaponItem("assets/item_textures", "test sword.png", "test sword", 10, 75, 30, 60)

testBow = RangedWeaponItem("assets/item_textures", "test bow.png", "test bow", 15, 400, 10, 60, "test projectile 1.png")

testSingleUse = ThrowableWeaponItem("assets/item_textures", "test single use.png", "test single use", 15, 400, 50, 10, 0, "test single use.png")