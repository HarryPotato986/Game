import pygame

from classes.CollisionBox import CollisionBox
from classes.Entities.Enemys.BaseEnemy import BaseEnemy


class BaseRoom:

    def __init__(self, resourceLocation, texture, collisionBoxs: tuple[int, int, int, int] | tuple[tuple[int, int, int, int], tuple[int, int, int, int]],
                 enemys: tuple[BaseEnemy, tuple[int, int]] | tuple[tuple[BaseEnemy, tuple[int, int]], tuple[BaseEnemy, tuple[int, int]]]):
        self.texture = resourceLocation + '/' + texture
        self.collisionBoxs = []
        self.enemys = []

        if isinstance(collisionBoxs, tuple):
            if isinstance(collisionBoxs[0], tuple):
                for box in collisionBoxs:
                    newBox = CollisionBox(box[0], box[1], box[2], box[3], self)
                    self.collisionBoxs.append(newBox)
            else:
                newBox = CollisionBox(collisionBoxs[0], collisionBoxs[1], collisionBoxs[2], collisionBoxs[3], self)
                self.collisionBoxs.append(newBox)
        self.deactivateCollisionBoxs()

        if isinstance(enemys, tuple):
            if isinstance(enemys[0], tuple):
                for enemy in enemys:
                    enemy[0].collisionBox.baseRect.x = enemy[1][0]
                    enemy[0].collisionBox.baseRect.y = enemy[1][1]
                    self.enemys.append(enemy[0])

    def activateCollisionBoxs(self):
        for boxs in self.collisionBoxs:
            boxs.activate()

    def deactivateCollisionBoxs(self):
        for boxs in self.collisionBoxs:
            boxs.deactivate()
