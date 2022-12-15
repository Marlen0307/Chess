from models import Postion
from models.ChessFigure import ChessFigure


class Bishop(ChessFigure):
    def __init__(self, color: str, title: str, position: Postion, direction):
        super().__init__(color, title, position, direction)
