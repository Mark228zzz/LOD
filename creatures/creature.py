class Creature:
    def __init__(self, x: int, y: int, alive: bool = True):
        self.x = x
        self.y = y
        self.alive = alive

    def loop(self):
        if not self.alive: self.die()

    def die(self):
        self.alive = False
