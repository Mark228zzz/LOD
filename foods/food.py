from vars import List
import logging
from random import randint

logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class Food:
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color
        self.nutritional_value = randint(250, 650)

        List.foods.append(self)

        logging.info(f'{self.__class__} was created.')

    def eaten(self): # when some object ate this food, run this method
        List.foods.remove(self)
        logging.info(f'{self.__class__} was eaten.')
        del self