import pygame

import ItemInit
from classes.BaseObject import BaseObject
from classes.Character import Character

pygame.init()
screen = pygame.display.set_mode((1200, 900), pygame.SCALED)
clock = pygame.time.Clock()

running = True
dt = 0

characterAssets = ["back profile.png", "right profile.png", "left profile.png", "front profile.png",
                   ["back profile left walk.png", "back profile right walk.png"], ["right profile walk.png", "right profile walk 2.png"],
                   ["left profile walk 2.png", "left profile walk.png"], ["front profile left walk.png", "front profile right walk.png"]]

character = Character(screen, 600, 450, "assets/character_textures", characterAssets, 0.5, ItemInit.testSword)
testRect = BaseObject(screen, 200, 200, 100, 100, "green")
testRect2 = BaseObject(screen, 750, 500, 80, 200, "blue")
testRect3 = BaseObject(screen, 200, 700, 50, 50, "yellow")
testRect4 = BaseObject(screen, 900, 200, 50, 50, 'purple')


while running:

    screen.fill("black")

    character.draw()
    testRect.draw()
    testRect2.draw()
    testRect3.draw()
    testRect4.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            character.attack(event)

    keys = pygame.key.get_pressed()
    character.inputHandler(keys, dt)


    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
