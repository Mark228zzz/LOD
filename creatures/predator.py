from creatures.creature import Creature
from vars import *
from random import randint

class Predator(Creature):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, alive: bool = True, step: int = 1):
        super().__init__(x, y, width, height, color, alive)
        self.satiety = 2500
        self.search_radius = 300
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
            self.satiety -= 1

    def brain(self):
        if self.satiety <= 2500:
            self.find_food()
        else:
            self.random_move()

    def reproduction(self):
        if self.satiety >= 2800:
            if randint(1, 100) == 1:
                predator = Predator(self.x, self.y, self.width, self.height, self.color)

    def find_food(self):
        nearest_food = None
        nearest_distance = float('inf')

        for food in List.foods:
            distance = ((food.x - self.x)**2 + (food.y - self.y)**2)**0.5
            if distance < self.search_radius and distance < nearest_distance:
                nearest_food = food
                nearest_distance = distance

        if nearest_food is not None:
            new_x, new_y = self.x, self.y

            if new_x < nearest_food.x:
                new_x += 1
            elif new_x > nearest_food.x:
                new_x -= 1

            if new_y < nearest_food.y:
                new_y += 1
            elif new_y > nearest_food.y:
                new_y -= 1

            self.x, self.y = new_x, new_y

            if self.x == nearest_food.x and self.y == nearest_food.y:
                self.satiety += 450
                nearest_food.eaten()
        else:
            self.random_move()

    def random_move(self):
        rand_x, rand_y = self.x, self.y
        rand_x, rand_y = rand_x + randint(-self.step, self.step), rand_y + randint(-self.step, self.step)
        if 0 < rand_x < Const.WIDTH and 0 < rand_y < Const.HEIGHT:
            self.x, self.y = rand_x, rand_y

    def die(self):
        List.predators.remove(self)
        return super().die()
