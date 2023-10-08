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
        
    @staticmethod
    def set_on_map(new_x: int, new_y: int, symbol: str, cur_x: int = 0, cur_y: int = 0, anyway: bool = False):
        if anyway:
            Game.world[new_y][new_x] = symbol
        else:
            if Game.world[new_y][new_x] == Char.EMPTY:
                Game.__delete_from_map(cur_x, cur_y)
                Game.world[new_y][new_x] = symbol
    
    @staticmethod
    def __delete_from_map(x: int, y: int): # delete any symbol on x, y
        Game.world[y][x] = Char.EMPTY
