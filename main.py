import pygame
from draw import Draw
from game import Game
from vars import *

def main():
    pygame.init()
    Game.init_game() # creates all the necessary things for start

    while Game.run:
        Const.STEP += 1
        pygame.time.delay(1) # pause the game for 1 millisecond

        Game.window.fill((255, 255, 255)) # fill all map

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.run = False
                break

        Game.loops() # make loop for every objects

        Game.spawn_food() # spawning food every iteration
        Draw.all() # draw all objects on the map

        #test function
        #if Const.STEP % 25 == 0:
        #    with open('logs2.txt', 'a') as logs2:
        #        logs2.write(round(len(List.animals)/10) * '#')
        #        logs2.write(f" - {len(List.animals)}")
        #        logs2.write('\n')

        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
