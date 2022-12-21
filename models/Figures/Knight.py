from models import Postion
from models.ChessBoard import get_x_index, get_y_index, ChessBoard, get_position
from models.ChessFigure import ChessFigure


class Knight(ChessFigure):
    def __init__(self, color: str, title: str, position: Postion, direction, player):
        super().__init__(color, title, position, direction, player)

    def get_moves_by_step(self, x_step, y_step):
        x_index = get_x_index(self.position.x)
        y_index = get_y_index(self.position.y)
        new_y_index = y_index + y_step
        new_x_index_1 = x_index + x_step
        new_x_index_2 = x_index - x_step
        moves_arr = []
        y = 0
        try:
            y = ChessBoard.y_positions[new_y_index]
        except IndexError:
            return moves_arr

        for i_of_x in [new_x_index_1, new_x_index_2]:
            x = 'A'
            try:
                x = ChessBoard.x_positions[i_of_x]
            except IndexError:
                continue
            pos = get_position(x, y)
            if self.is_position_valid(pos):
                moves_arr.append(pos)
        return moves_arr

    def get_moves(self):
        vetical_L_moves = self.get_moves_by_step(1, 2)
        horizontal_L_moves = self.get_moves_by_step(2, 1)
        return vetical_L_moves + horizontal_L_moves

    def get_moving_options(self):
        moves = self.get_moves()
        self.get_next_move(moves)
