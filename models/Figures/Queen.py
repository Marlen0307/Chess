from Constants import Directions, CrossDirections
from models import Postion
from models.ChessFigure import ChessFigure
from models.Figures.Bishop import get_top_right_left_bottom_moves, get_top_left_right_bottom_moves
from models.Figures.Rook import get_horizontal_moves, get_vertical_moves


class Queen(ChessFigure):
    def __init__(self, color: str, title: str, position: Postion, direction, player):
        super().__init__(color, title, position, direction, player)

    def get_all_moves(self):
        x = self.position.x
        y = self.position.y
        left_positions = get_horizontal_moves(self, x, y, Directions.LEFT)
        right_positions = get_horizontal_moves(self, x, y, Directions.RIGHT)
        top_positions = get_vertical_moves(self, x, y, Directions.TOP)
        bottom_positions = get_vertical_moves(self, x, y, Directions.BOTTOM)
        top_right_moves = get_top_right_left_bottom_moves(self, self.position, CrossDirections.RIGHT_TOP)
        bottom_left_moves = get_top_right_left_bottom_moves(self, self.position, CrossDirections.LEFT_BOTTOM)
        top_left_moves = get_top_left_right_bottom_moves(self, self.position, CrossDirections.LEFT_TOP)
        right_bottom_moves = get_top_left_right_bottom_moves(self, self.position, CrossDirections.RIGHT_BOTTOM)
        return left_positions + right_positions + top_positions + bottom_positions + top_right_moves + top_left_moves +\
            bottom_left_moves + right_bottom_moves

    def get_moving_options(self):
        moves = self.get_all_moves()
        self.get_next_move(moves)
