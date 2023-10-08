from game import Game
from life import Life

def starter():
    for life in range(1):
        life = Life('some life', '$', random_start_pos_var=True)
    
    while True:
        Game.loop()

if __name__ == "__main__":
    starter()
