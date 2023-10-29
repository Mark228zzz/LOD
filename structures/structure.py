class Structure:
    def __init__(self, x: int, y: int, color: tuple, can_step_on_cell: bool = True):
        self.x, self.y = x, y
        self.color = color
        self.can_step_on_cell = can_step_on_cell
