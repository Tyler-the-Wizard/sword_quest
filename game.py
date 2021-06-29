import pygame

import constants

pygame.init()

screen = pygame.display.set_mode(constants.SCREEN_SIZE)
pygame.display.set_caption("My awesome swords game!!!!")

running = True
while running:
    screen.fill(constants.C_BLACK)

    # Test code: display a rectangle
    pygame.draw.rect(screen, constants.C_WHITE,
        pygame.Rect(500, 500, 800, 300)
    )
    pygame.draw.rect(screen, constants.C_BLACK,
        pygame.Rect(520, 520, 760, 260)
    )

    pygame.display.flip()

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False