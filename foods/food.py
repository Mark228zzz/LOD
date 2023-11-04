from vars import *


class Food:
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color
        List.foods.append(self)
