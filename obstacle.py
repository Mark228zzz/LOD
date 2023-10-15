from game import *

class Obstacle:
    def __init__(self, x: int, y: int, width: int = 1, height: int = 1, color: tuple = (150, 75, 0)):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color

        Game.list_of_obstacles.append(self)
