import logging

logging.basicConfig(filename='logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class Creature:
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, alive: bool = True):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color
        self.alive = alive
        self.nutritional_value: int
        self.age: int = 0

        logging.info(f'{self.__class__} was created.')

    def loop(self): ...

    def die(self):
        self.alive = False
        logging.info(f'{self.__class__} dead.')
        del self
