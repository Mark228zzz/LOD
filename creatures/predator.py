from creatures.creature import Creature
from vars import *
from random import randint

class Predator(Creature):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, alive: bool = True):
        super().__init__(x, y, width, height, color, alive)
        List.predators.append(self)

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
        rand_x, rand_y = self.x, self.y
        rand_x, rand_y = rand_x + randint(-self.step, self.step), rand_y + randint(-self.step, self.step)
        if 0 < rand_x < Const.WIDTH and 0 < rand_y < Const.HEIGHT:
            self.x, self.y = rand_x, rand_y

    def die(self):
        self.alive = False
        List.predators.remove(self)
        del self
