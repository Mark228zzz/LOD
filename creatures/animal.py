from creatures.creature import Creature


class Animal(Creature):
    def __init__(self, x: int, y: int, alive: bool = True):
        super().__init__(x, y, alive)

    def find_food(self):
        pass

    def move_to_food(self):
        pass

    def random_move(self):
        pass
