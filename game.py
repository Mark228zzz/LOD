from vars import *


class Game:
    world = [[Char.EMPTY for i in range(Const.WIDTH)] for i in range(Const.HEIGHT)] # 2d world
    info = '' # this var will be under print world. Info for set some text (informations)

    @staticmethod
    def print_world(): # print world. Wigth by height
        Game.__clear_screen()
        for i in reversed(Game.world):
            print(*i)
        print(Game.info)
    
    @staticmethod
    def __clear_screen():
        print('\n' * Const.CLEAR_SCREEN_VALUE)
