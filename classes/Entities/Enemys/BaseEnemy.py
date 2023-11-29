from classes.Entities.BaseEntity import BaseEntity


class BaseEnemy(BaseEntity):

    def __init__(self, surface, x, y, resourceLocation, textures, scale, name, weapon):
        super().__init__(surface, x, y, resourceLocation, textures, scale, name, weapon)