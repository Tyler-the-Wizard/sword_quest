"""Specifies code around the player itself"""
from actor import Actor

class Player(Actor):
    def __init__(self):
        super().__init__("player", (100, 100))