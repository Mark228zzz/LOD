class Creature:
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, alive: bool = True):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color
        self.alive = alive
