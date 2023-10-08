from vars import *
from random import randint
from game import Game


class Life:
    def __init__(self, name: str, symbol: str, x: int = 0, y: int = 0, alive: bool = True, random_start_pos: bool = False):
        self.name = name
        self.symbol = symbol
        self.x, self.y = x, y
        self.satiety = 15
        self.alive = alive
        self.random_start_pos = random_start_pos
        
        if self.random_start_pos: self.random_start_pos()
    
    def loop(self):
        if self.alive:
            self.brain()
            self.check()
    
    def check(self):
        if self.satiety <= 0:
            self.die()
        else:
            self.satiety -= 1

    def brain(self):
        pass
        
    def set_on_map(self, new_x: int, new_y: int, anyway: bool = False):
        Game.set_on_map(new_x, new_y, self.symbol, anyway)
    
    def random_start_pos(self):
        new_x, new_y = randint(0, Const.WIDTH-1), randint(0, Const.HEIGHT-1)
        self.set_on_map(new_x, new_y, anyway=True)
    
    def die(self):
        self.alive = False
        del self
