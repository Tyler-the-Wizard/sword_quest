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

        super().__init__(
            constants.SS_TILES,
            (
                rect[0] * constants.TILE_SCALE,
                rect[1] * constants.TILE_SCALE,
                rect[2],
                rect[3]
            ),
            (0, 0)
        )

    def draw(self, surface, coords):
        surface.blit(self.image, coords)

# The global array of tiles; used to draw levels
TILES = [
    0,
    Tile((0, 1, 16, 16)),
    Tile((14, 4, 8, 8)),
    Tile((16, 6, 32, 16))
]