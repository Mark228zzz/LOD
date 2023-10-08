from vars import *
from random import randint
from game import Game
from random import choice


class Life:
    def __init__(self, name: str, symbol: str, x: int = 0, y: int = 0, alive: bool = True, random_start_pos_var: bool = False):
        self.name = name
        self.symbol = symbol
        self.x, self.y = x, y
        self.satiety = 15
        self.alive = alive
        List.list_of_lifes.append(self)
        self.random_start_pos_var = random_start_pos_var
        
        if self.random_start_pos_var: self.random_start_pos()
    
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
        if self.satiety < 8:
            self.find_food()
        else:
            if choice([True, False]):
                self.random_move()
            else:
                self.wait()
            
    def wait(self):
        pass
    
    def random_move(self):
        new_x, new_y = self.x, self.y
        match choice(['x', 'y']):
            case 'x':
                new_x += choice([1, -1])
            case 'y':
                new_y += choice([1, -1])
        self.set_on_map(new_x, new_y)
        
    def find_food(self):
        pass
        
    def set_on_map(self, new_x: int, new_y: int, anyway: bool = False):
        Game.set_on_map(new_x, new_y, self.symbol, anyway)
    
    def random_start_pos(self):
        new_x, new_y = randint(0, Const.WIDTH-1), randint(0, Const.HEIGHT-1)
        self.set_on_map(new_x, new_y, anyway=True)
    
    def die(self):
        self.alive = False
        del self
