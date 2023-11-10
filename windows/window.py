from vars import List


class Window:
    def __init__(self, game_window, visible: bool = False):
        self.game_window = game_window
        self.visible = visible
        List.windows.append(self)

    def draw(self): ...
