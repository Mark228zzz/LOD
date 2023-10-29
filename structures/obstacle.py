from structures.structure import Structure


class Obstacle(Structure):
    def __init__(self, x: int, y: int, color: tuple, can_step_on_cell: bool = True):
        super().__init__(x, y, color, can_step_on_cell)
        self.can_step_on_cell = False
