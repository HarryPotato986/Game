from classes.BaseObject import BaseObject
from classes.Entities.EntityTextureHandler import EntityTextureHandler


class BaseEntity(BaseObject):

    def __init__(self, surface, x, y, resourceLocation, textures, scale, name, weapon):
        self.textureHandler = EntityTextureHandler(resourceLocation, textures[0], textures[1], textures[2], textures[3], textures[4], textures[5], textures[6], textures[7], scale)
        super().__init__(surface, x, y, self.textureHandler.idleDown.get_width(), self.textureHandler.idleDown.get_height())
        self.activeTexture = self.textureHandler.idleDown
        self.walkAnimationTimer = 15
        self.weapon = weapon
        self.facing = 'D'
        self.name = name


    def draw(self):
        self.surface.blit(self.activeTexture, self.collisionBox.baseRect)

    def hit(self):
        print(self.name + ": Hit!")
