"""This file defines all tiles used in levels."""
# TODO: maybe later each level can have its own tileset

import pygame

import constants
from sprite import Sprite

class Tile(Sprite):
    def __init__(self, rect, props = {}):
        """
        rect : rect containing coordinates on the spritesheet
        props : dict containing properties of the tile
            can_touch : bool (default True)
        """

        self.can_touch = ("can_touch" in props.keys()) and props["can_touch"] or True

        super().__init__(constants.SS_TILES, rect, (0, 0))

    def draw(self, surface, coords):
        self.x, self.y = coords
        super().draw(surface)

# The global array of tiles; used to draw levels
TILES = [
    0,
    Tile(pygame.Rect(0  * 8, 1  * 8, 16, 16)),
    Tile(pygame.Rect(16 * 8, 6  * 8, 32, 16))
]