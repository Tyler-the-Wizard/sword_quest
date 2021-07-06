import pygame

import constants

pygame.init()
clock = pygame.time.Clock()
pygame.display.init()

screen = pygame.display.set_mode(constants.SCREEN_SIZE)
pygame.display.set_caption("Quest of the Two Swords")

import level

running = True
while running:
    screen.fill(constants.C_BLACK)

    # Test code: draw a level
    level.draw([8, 8,
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 0, 0, 0, 0, 1,
        1, 0, 2, 2, 0, 0, 0, 1,
        1, 0, 2, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 0, 0, 1,
        1, 0, 0, 0, 0, 2, 0, 1,
        1, 0, 0, 0, 0, 0, 0, 1,
        1, 1, 1, 1, 1, 1, 1, 1
    ], screen)

    pygame.display.flip()
    clock.tick(constants.FPS)

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            pass