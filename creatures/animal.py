from creatures.creature import Creature
from random import choice
from vars import *


class Animal(Creature):
    def __init__(self, x: int, y: int, color: tuple, alive: bool = True):
        super().__init__(x, y, color, alive)
        List.animals.append(self)

    def loop(self):
        if self.alive:
            self.brain()

    def brain(self):
        if choice([True, False]):
            self.random_move()
        else:
            self.find_food()

    def find_food(self):
        pass

    def move_to_food(self):
        pass

    def random_move(self):
        pass
