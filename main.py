import pygame
from classes.BaseObject import BaseObject
from classes.Character import Character

pygame.init()
screen = pygame.display.set_mode((1200, 900), pygame.SCALED)
clock = pygame.time.Clock()

running = True
dt = 0

character = Character(screen, "red", 600, 450, 20, 40)
testRect = BaseObject(screen, "green", 200, 200, 100, 100)
testRect2 = BaseObject(screen, "blue", 750, 500, 80, 200)
testRect3 = BaseObject(screen, "yellow", 200, 700, 50, 50)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    character.draw()
    testRect.draw()
    testRect2.draw()
    testRect3.draw()

    keys = pygame.key.get_pressed()
    character.movement(keys, dt)


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
