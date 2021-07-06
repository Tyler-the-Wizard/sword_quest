"""Specifies code around the player itself"""
from monster import Monster

class Player(Monster):
    def __init__(self):
        super().__init__("player", (100, 100))