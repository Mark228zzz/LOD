import game

class Food:
    def __init__(self, x: int, y: int, satiety: int = 100):
        self.x = x
        self.y = y
        self.satiety = satiety
        self.color = (255, 255, 0)

        game.Game.list_of_foods.append(self)
