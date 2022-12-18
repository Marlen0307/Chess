from models.ChessBoard import get_position, get_x_index, get_y_index, ChessBoard
from models.ChessFigure import ChessFigure
from models import Postion
from Constants import Directions, extremes


class Rook(ChessFigure):
    def __init__(self, color: str, title: str, position: Postion, direction, player):
        super().__init__(color, title, position, direction, player)

    def is_position_valid(self, pos: Postion):

        if pos.occupied:  # if position is occupied by opponent position is valid
            return pos.chess_figure.color != self.color
        return True  # if position is not occupied position is valid

    def get_horizontal_moves(self, x, y,
                             direction):

        index_of_coordinate_to_be_moved = get_x_index(x)

        def get_condition():
            condition = index_of_coordinate_to_be_moved >= extremes[direction]

            if direction == Directions.RIGHT:
                condition = index_of_coordinate_to_be_moved <= extremes[direction]
            return condition

        moves_arr = []
        while get_condition():
            pos = get_position(ChessBoard.x_positions[index_of_coordinate_to_be_moved], y)
            if self.is_position_valid(pos):
                moves_arr.append(pos)
                index_of_coordinate_to_be_moved = index_of_coordinate_to_be_moved + self.get_direction(direction) * 1

            index_of_coordinate_to_be_moved = index_of_coordinate_to_be_moved + self.get_direction(direction) * 1
            break_condition = pos.to_string() != self.position.to_string()
            if break_condition:
                break
        return moves_arr

    def get_vertical_moves(self, x, y, direction):

        self.direction = direction

        index_of_coordinate_to_be_moved = get_y_index(y)

        def get_condition():
            condition = index_of_coordinate_to_be_moved >= extremes[direction]

            if direction == Directions.TOP:
                condition = index_of_coordinate_to_be_moved <= extremes[direction]
            return condition

        moves_arr = []
        while get_condition():
            pos = get_position(x, ChessBoard.y_positions[index_of_coordinate_to_be_moved])
            if self.is_position_valid(pos):
                moves_arr.append(pos)
                index_of_coordinate_to_be_moved = index_of_coordinate_to_be_moved + self.get_direction(direction) * 1
                continue
            index_of_coordinate_to_be_moved = index_of_coordinate_to_be_moved + self.get_direction(direction) * 1
            break_condition = pos.to_string() != self.position.to_string()
            if break_condition:
                break
        return moves_arr

    def get_all_moves(self):
        x = self.position.x
        y = self.position.y
        left_positions = self.get_horizontal_moves(x, y, Directions.LEFT)
        right_positions = self.get_horizontal_moves(x, y, Directions.RIGHT)
        top_positions = self.get_vertical_moves(x, y, Directions.TOP)
        bottom_positions = self.get_vertical_moves(x, y, Directions.BOTTOM)
        return left_positions + right_positions + top_positions + bottom_positions

    def get_moving_options(self):
        moves = self.get_all_moves()
        self.get_next_move(moves)
