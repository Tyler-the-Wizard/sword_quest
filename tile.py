"""This file defines all tiles used in levels."""
# TODO: maybe later each level can have its own tileset

import constants
from sprite import Sprite

class Tile(Sprite):
    def __init__(self, rect, coords, props):
        """
        rect : rect containing coordinates on the spritesheet
        coords : tuple2 containing position of the sprite in x, y
        props : dict containing properties of the tile
            can_touch : bool (default True)
        """

        self.can_touch = ("can_touch" in props.keys()) and props["can_touch"] or True

        super().__init__(constants.SS_TILES, rect, coords)