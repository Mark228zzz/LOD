import pygame
from draw import Draw
from game import Game
from vars import *

def main():
    pygame.init()
    Game.init_game()
    while Game.run:
        pygame.time.delay(150)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.run = False
                break

        Game.window.fill((255, 255, 255))
        Draw.grid()
        Draw.something(9, 7, (25, 25, 25))

        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
