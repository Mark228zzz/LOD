from game import Game

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = float('inf')
        self.h = 0
        self.f = 0
        self.parent = None

    def calculate_h(self, end_node):
        self.h = abs(self.x - end_node.x) + abs(self.y - end_node.y)
        return self.h

    def calculate_f(self):
        self.f = self.g + self.h
        return self.f

def a_star(start, end):
    start_node = Node(start[0], start[1])
    end_node = Node(end[0], end[1])
    start_node.g = 0
    start_node.calculate_h(end_node)
    start_node.calculate_f()

    open_list = [start_node]
    closed_list = []

    while open_list:
        current_node = min(open_list, key=lambda x: x.f)

        if current_node.x == end_node.x and current_node.y == end_node.y:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        open_list.remove(current_node)
        closed_list.append(current_node)

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            x, y = current_node.x + dx, current_node.y + dy
            if not Game.is_obstacle(x, y) and (x, y) not in [(node.x, node.y) for node in closed_list]:
                new_node = Node(x, y)
                new_node.parent = current_node
                new_node.g = current_node.g + 1
                new_node.calculate_h(end_node)
                new_node.calculate_f()

                if new_node not in open_list:
                    open_list.append(new_node)
    return None
