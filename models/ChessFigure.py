from models import Postion


class ChessFigure:

    def __init__(self, color: str, title: str, position: Postion):
        self.position = position
        self.killed = False
        self.color = color
        self.title = title

    def move(self, new_position: Postion):
        self.position = new_position

    def set_title(self, new_title: str):
        self.title = new_title

    def get_position(self):
        return self.position.to_string()
