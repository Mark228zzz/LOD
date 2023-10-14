import pygame
import random

pygame.init()


class Game:
    run = True
    window_width, window_height = 800, 600
    grid_size = 20
    cols = window_width // grid_size
    rows = window_height // grid_size
    window = None
    list_of_creatures = []
    list_of_foods = []
    
    @staticmethod
    def init_game():
        grid = [['' for _ in range(Game.cols)] for _ in range(Game.rows)]
        Game.window = pygame.display.set_mode((Game.window_width, Game.window_height), pygame.RESIZABLE)
    
    @staticmethod
    def draw_grid():
        Game.cols = Game.window_width // Game.grid_size
        Game.rows = Game.window_height // Game.grid_size
        for y in range(Game.rows):
            for x in range(Game.cols):
                pygame.draw.rect(Game.window, (200, 200, 200), (x * Game.grid_size, y * Game.grid_size, Game.grid_size, Game.grid_size), 1)
    
    @staticmethod
    def draw_creatures():
        for creature in Game.list_of_creatures:
            pygame.draw.rect(Game.window, creature.color, (creature.x * Game.grid_size, creature.y * Game.grid_size, Game.grid_size, Game.grid_size))    

    @staticmethod
    def draw_foods():
        for food in Game.list_of_foods:
            pygame.draw.rect(Game.window, food.color, (food.x * Game.grid_size, food.y * Game.grid_size, Game.grid_size, Game.grid_size))
    
    @staticmethod
    def loop():
        for creature in Game.list_of_creatures:
            creature.decrease_hunger()
            creature.move_to_food()
            creature.reproduction()

class Creature:
    def __init__(self, x: int = Game.cols // 2, y: int = Game.rows // 2):
        self.x = x
        self.y = y
        self.hunger = 150
        self.color = (0, 0, 255)
        self.search_radius = 50
        self.alive = True
        
        Game.list_of_creatures.append(self)
    
    def move_to_food(self):
        if self.alive:
            if self.hunger < 100:
                nearest_food = None
                nearest_distance = float('inf')
                
                for food in Game.list_of_foods:
                    distance = ((food.x - self.x)**2 + (food.y - -self.y)**2)**0.5
                    if distance < self.search_radius and distance < nearest_distance:
                        nearest_food = food
                        nearest_distance = distance
                
                if nearest_food is not None:
                    if self.x < nearest_food.x:
                        self.x += 1
                    elif self.x > nearest_food.x:
                        self.x -= 1
                    
                    if self.y < nearest_food.y:
                        self.y += 1
                    elif self.y > nearest_food.y:
                        self.y -= 1
            
                    if self.x == nearest_food.x and self.y == nearest_food.y:
                        self.hunger += nearest_food.satiety
                        Game.list_of_foods.remove(nearest_food)
                        food = Food()
                else:
                    self.random_move()
            else:
                self.random_move()
        else:
            Game.list_of_creatures.remove(self)
        
    def reproduction(self):
        if self.hunger >= 160:
            if random.randint(1, 10) == 1:
                self.hunger -= 65
                life = Creature(x=self.x, y=self.y)
    
    def random_move(self):
        random_direction = (random.choice(['x', 'y']), random.choice([-1, 1]))
        match random_direction[0]:
            case 'x':
                self.x += random_direction[1]
            case 'y':
                self.y += random_direction[1]
    
    def decrease_hunger(self):
        if not self.hunger <= 0:
            self.hunger = max(0, self.hunger - 1)
        else:
            self.alive = False


class Food:
    def __init__(self, satiety: int = 100):
        self.x = random.randint(0, Game.cols-1)
        self.y = random.randint(0, Game.rows-1)
        self.satiety = satiety
        self.color = (255, 255, 0)
        Game.list_of_foods.append(self)


life = Creature()
food = Food()
Game.init_game()

while Game.run:
    pygame.time.delay(250)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game.run = False
            break
        elif event.type == pygame.VIDEORESIZE:
            Game.window_width, Game.window_height = event.w, event.h
            Game.window = pygame.display.set_mode((Game.window_width, Game.window_height), pygame.RESIZABLE)
    
    Game.window.fill((255, 255, 255))
    Game.loop()
    Game.draw_grid()
    Game.draw_creatures()
    Game.draw_foods()
    pygame.display.update()

pygame.quit()
