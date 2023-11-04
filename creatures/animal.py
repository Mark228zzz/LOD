from creatures.creature import Creature
from random import choice
from random import randint
from vars import *


class Animal(Creature):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, alive: bool = True):
        super().__init__(x, y, width, height, color, alive)
        self.satiety = 100

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
        self.x = self.x + randint(-2, 2)
        self.y = self.y + randint(-2, 2)

    def die(self):
        List.animals.remove(self)
        return super().die()
