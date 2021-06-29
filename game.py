import pygame

pygame.init()

# TODO move to constants
screen_size = (1600, 900)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("My awesome swords game!!!!")

running = True
while running:
    screen.fill((0, 0, 0)) # maybe a different color?

    # Test code: display a rectangle
    pygame.draw.rect(screen, (255, 255, 255),
        pygame.Rect(500, 500, 800, 300)
    )
    pygame.draw.rect(screen, (0, 0, 0),
        pygame.Rect(520, 520, 760, 260)
    )

    pygame.display.flip()

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False