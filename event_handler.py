import pygame

import config

def handle(event):
    """Updates global variables based on behavior; for example,
    arrow keys move the player."""

    if event.type == pygame.KEYDOWN:
        # A key was pressed
        if event.key == pygame.K_LEFT:
            config.L = True
        elif event.key == pygame.K_RIGHT:
            config.R = True
        elif event.key == pygame.K_UP:
            config.U = True
        elif event.key == pygame.K_DOWN:
            config.D = True

        elif event.key == pygame.K_z:
            config.Jump = True

    elif event.type == pygame.KEYUP:
        # A key was released
        if event.key == pygame.K_LEFT:
            config.L = False
        elif event.key == pygame.K_RIGHT:
            config.R = False
        elif event.key == pygame.K_UP:
            config.U = False
        elif event.key == pygame.K_DOWN:
            config.D = False
        
        elif event.key == pygame.K_z:
            config.Jump = False
