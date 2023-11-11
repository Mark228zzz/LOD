from vars import List


class Window:
    def __init__(self, name: str, game_window, visible: bool = False):
        self.name = name
        self.game_window = game_window
        self.visible = visible
        self.initialized = True

        List.windows.append(self)

    def draw(self): ...
