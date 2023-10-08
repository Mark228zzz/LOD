from vars import *


class Game:
    world = [[Char.EMPTY for i in range(Const.WIDTH)] for i in range(Const.HEIGHT)] # 2d world
    info = ''

    @staticmethod
    def print_world():
        for i in reversed(Game.world):
            print(*i)
        print(Game.info)
