from creatures.creature import Creature
from vars import List, Const
from random import randint

class Predator(Creature):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, alive: bool = True, step: int = 1):
        super().__init__(x, y, width, height, color, alive)
        self.satiety = 2500
        self.search_radius = 250
        self.step = step

        List.predators.append(self)

    def loop(self):
        if self.alive:
            self.check()
            self.brain()
            self.reproduction()

    def check(self):
        if self.satiety <= 1:
            self.die()
        else:
            self.satiety -= 2

    def brain(self):
        if self.satiety <= 2500:
            self.hunt()
        else:
            self.random_move()

    def reproduction(self):
        if self.satiety >= 2800:
            if randint(1, 100) == 1:
                predator = Predator(self.x, self.y, self.width, self.height, self.color)

    def hunt(self):
        nearest_prey = None
        nearest_distance = float('inf')

        for animal in List.animals:
            distance = ((animal.x - self.x) ** 2 + (animal.y - self.y) ** 2) ** 0.5
            if distance < self.search_radius and distance < nearest_distance:
                nearest_prey = animal
                nearest_distance = distance

        if nearest_prey is not None:
            new_x, new_y = self.x, self.y

            if new_x < nearest_prey.x:
                new_x += 1
            elif new_x > nearest_prey.x:
                new_x -= 1

            if new_y < nearest_prey.y:
                new_y += 1
            elif new_y > nearest_prey.y:
                new_y -= 1

            self.x, self.y = new_x, new_y

            if self.x == nearest_prey.x and self.y == nearest_prey.y:
                self.satiety += 900
                nearest_prey.die()

    def random_move(self):
        rand_x, rand_y = self.x, self.y
        rand_x, rand_y = rand_x + randint(-self.step, self.step), rand_y + randint(-self.step, self.step)
        if 0 < rand_x < Const.WIDTH and 0 < rand_y < Const.HEIGHT:
            self.x, self.y = rand_x, rand_y

    def die(self):
        List.predators.remove(self)
        return super().die()
