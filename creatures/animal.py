from creatures.creature import Creature
from random import randint
from vars import *
import logging

logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class Animal(Creature):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, alive: bool = True, step: int = 1):
        super().__init__(x, y, width, height, color, alive)
        self.satiety = 1000
        self.search_radius = 250
        self.step = step

        List.animals.append(self)

        logging.info(f'{self.__class__} was created.')

    def loop(self):
        if self.alive:
            self.check()
            self.brain()
            self.reproduction()

    def check(self):
        if self.satiety <= 1:
            self.die()

    def brain(self):
        if self.satiety <= 1000:
            self.find_food()
        else:
            self.random_move()
        self.satiety -= 1

    def reproduction(self):
        if self.satiety >= 1200:
            if randint(1, 25) == 1:
                if randint(1, 100) == 1:
                    animal = Animal(self.x, self.y, self.width, self.height, (0, 255, 0))
                else:
                    animal = Animal(self.x, self.y, self.width, self.height, self.color, step=4)

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
                    self.satiety += 580
                    List.foods.remove(nearest_food)
            else:
                self.random_move()

    def random_move(self):
        rand_x, rand_y = self.x, self.y
        rand_x, rand_y = rand_x + randint(-self.step, self.step), rand_y + randint(-self.step, self.step)
        if 0 < rand_x < Const.WIDTH and 0 < rand_y < Const.HEIGHT:
            self.x, self.y = rand_x, rand_y

    def die(self):
        List.animals.remove(self)
        logging.info(f'{self.__class__} dead.')
        return super().die()

