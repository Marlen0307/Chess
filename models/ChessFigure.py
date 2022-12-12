from models import Postion


class ChessFigure:

    def __init__(self, color: str, title: str, position: Postion):
        self.position = position
        self.color = color
        self.title = title
