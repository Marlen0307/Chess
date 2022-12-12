import string
from typing import Union

from models.ChessFigure import ChessFigure


class Position:
    y = None
    x = None
    occupied: bool = None
    chess_figure: ChessFigure = None

    def __init__(self, y_pos: Union[str, int], x_pos: Union[str, int], figure: Union[ChessFigure, None]):
        self.y = str(y_pos)
        self.x = str(x_pos)
        self.occupied = figure is not None
        self.chess_figure = figure

    def set_chess_figure(self, new_figure: ChessFigure):
        self.chess_figure = new_figure
