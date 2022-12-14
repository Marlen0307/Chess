from models import Postion
from models.ChessFigure import ChessFigure


class Queen(ChessFigure):
    def __init__(self, color: str, title: str, position: Postion):
        super().__init__(color, title, position)
