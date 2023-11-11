from structures.structure import Structure
from vars import List


class Obstacle(Structure):
    def __init__(self, x: int, y: int, color: tuple, can_step_on_cell: bool = True):
        super().__init__(x, y, color, can_step_on_cell)
        self.can_step_on_cell = False
        List.obstacles.append(self)

    def remove(self):
        List.obstacles.remove(self)
