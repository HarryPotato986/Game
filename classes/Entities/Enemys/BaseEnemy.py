import pygame

from classes.Entities.BaseEntity import BaseEntity


def get_vector_distance(vector_1, vector_2):
    return (vector_1 - vector_2).magnitude()


class BaseEnemy(BaseEntity):

    def __init__(self, surface, x, y, resourceLocation, textures, scale, name, weapon, maxHealth):
        super().__init__(surface, x, y, resourceLocation, textures, scale, name, weapon, maxHealth)


        self.direction = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.speed = 3

        self.position = pygame.math.Vector2(self.collisionBox.baseRect.center)

    def chase_player(self, playerPos):
        self.position = pygame.math.Vector2(self.collisionBox.baseRect.center)
        player_vector = pygame.math.Vector2(playerPos)
        enemy_vector = pygame.math.Vector2(self.collisionBox.baseRect.center)
        distance = get_vector_distance(player_vector, enemy_vector)

        if distance > 0:
            self.direction = (player_vector - enemy_vector).normalize()
        #else:
            #self.direction = pygame.math.Vector2()
            self.velocity = self.direction * self.speed
            self.position += self.velocity

            self.collisionBox.baseRect.centerx = self.position.x
            self.collisionBox.baseRect.centery = self.position.y

        self.checkCollisions(10)

    def ticker(self, playerPos):
        self.draw()
        if self.collisionBox.active:
            self.chase_player(playerPos)

