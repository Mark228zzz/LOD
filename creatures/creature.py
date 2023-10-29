class Creature:
    def __init__(self, x: int, y: int, color: tuple, alive: bool = True):
        self.x = x
        self.y = y
        self.alive = alive

    def die(self):
        self.alive = False
