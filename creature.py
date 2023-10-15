from game import *
import random


class Creature:
    def __init__(self, x: int = Game.cols // 2, y: int = Game.rows // 2, color: tuple = (0, 0, 255)):
        self.x = x
        self.y = y
        self.hunger = 150
        self.age = 0
        self.color = color
        self.search_radius = 50
        self.alive = True
        
        Game.list_of_creatures.append(self)
    
    def move_to_food(self):
        if self.alive:
            if self.hunger < 100:
                nearest_food = None
                nearest_distance = float('inf')

                for food in Game.list_of_foods:
                    distance = ((food.x - self.x)**2 + (food.y - self.y)**2)**0.5
                    if distance < self.search_radius and distance < nearest_distance:
                        nearest_food = food
                        nearest_distance = distance

                if nearest_food is not None:
                    new_x, new_y = self.x, self.y

                    if new_x < nearest_food.x and not Game.is_obstacle(self.x + 1, self.y):
                        new_x += 1
                    elif new_x > nearest_food.x and not Game.is_obstacle(self.x - 1, self.y):
                        new_x -= 1

                    if new_y < nearest_food.y and not Game.is_obstacle(self.x, self.y + 1):
                        new_y += 1
                    elif new_y > nearest_food.y and not Game.is_obstacle(self.x, self.y - 1):
                        new_y -= 1
                        
                    if not Game.is_obstacle(new_x, new_y):
                        self.x, self.y = new_x, new_y

                    if self.x == nearest_food.x and self.y == nearest_food.y:
                        self.hunger += nearest_food.satiety
                        Game.list_of_foods.remove(nearest_food)
                else:
                    self.random_move()
            else:
                self.random_move()
        else:
            Game.list_of_creatures.remove(self)
        
        if self.age >= random.randint(170, 230):
            Game.list_of_creatures.remove(self)
        else:
            self.age += 1
        
    def reproduction(self):
        if self.hunger >= 160:
            if random.randint(1, 30) == 1:
                self.hunger -= 65
                life = Creature(x=self.x, y=self.y, color=(self.color[0]+5, self.color[1]+5, 255))
    
    def random_move(self):
        random_direction = (random.choice(['x', 'y']), random.choice([-1, 1]))
        match random_direction[0]:
            case 'x':
                new_x = self.x + random_direction[1]
                if 0 <= new_x < Game.window_width and not Game.is_obstacle(new_x, self.y) and Game.check(new_x * Game.grid_size, self.y * Game.grid_size):
                    self.x = new_x
            case 'y':
                new_y = self.y + random_direction[1]
                if 0 <= new_y < Game.window_height and not Game.is_obstacle(self.x, new_y) and Game.check(self.x * Game.grid_size, new_y * Game.grid_size):
                    self.y = new_y
    
    def decrease_hunger(self):
        if not self.hunger <= 0:
            self.hunger = max(0, self.hunger - 1)
        else:
            self.alive = False