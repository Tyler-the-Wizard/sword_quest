import pygame

import constants

def load_spritesheet(filename):
    return pygame.image.load("sprites/" + filename).convert()

sheet_cache = []

# Load all spritesheets
sheet_cache.insert(constants.SS_TILES, load_spritesheet("tiles.png"))
class Sprite:
    def __init__(self, sheet_index, rect, coords):
        """
        sheet_index : index of spritesheet (from constants file)
        rect : tuple4 containing coordinates on the spritesheet
        coords : tuple2 containing position of the sprite in x, y
        """

        rect = pygame.Rect(rect)
        surf = pygame.Surface(rect.size).convert()
        surf.blit(sheet_cache[sheet_index], (0, 0), rect)
        self.image = pygame.transform.scale(surf, (surf.get_width()  * constants.GRAPHICS_SCALE,
                                                   surf.get_height() * constants.GRAPHICS_SCALE))

        self.x, self.y = coords
        self.width = rect.width * constants.GRAPHICS_SCALE
        self.height = rect.height * constants.GRAPHICS_SCALE

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))