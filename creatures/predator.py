from creatures.creature import Creature
from vars import *

class Predator(Creature):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, alive: bool = True):
        super().__init__(x, y, width, height, color, alive)

    def loop(self):
        pass

    def check(self):
        pass

    def brain(self):
        pass

    def reproduction(self):
        pass

    def find_food(self):
        pass

    def random_move(self):
        pass

    def die(self):
        self.alive = False
        List.predators.remove(self)
        del self
