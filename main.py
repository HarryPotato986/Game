import pygame
from classes.BaseObject import BaseObject

pygame.init()
screen = pygame.display.set_mode((1200, 900), pygame.SCALED)
clock = pygame.time.Clock()

running = True
dt = 0


testRect = BaseObject(screen, "red", 600, 450, 20, 40)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    testRect.draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        testRect.y -= 300 * dt
    if keys[pygame.K_s]:
        testRect.y += 300 * dt
    if keys[pygame.K_a]:
        testRect.x -= 300 * dt
    if keys[pygame.K_d]:
        testRect.x += 300 * dt
    testRect.updateRect()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
