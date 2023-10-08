from vars import *


class Life:
    def __init__(self, name: str, symbol: str, x: int = 0, y: int = 0, alive: bool = True, random_start_pos: bool = False):
        self.name = name
        self.symbol = symbol
        self.x, self.y = x, y
        self.alive = alive
        self.random_start_pos = random_start_pos
