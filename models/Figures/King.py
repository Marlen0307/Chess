from Constants import BoardSides
from models import Postion
from models.ChessBoard import get_x_index, get_y_index, ChessBoard, get_position
from models.ChessFigure import ChessFigure


class King(ChessFigure):
    def __init__(self, color: str, title: str, position: Postion, direction, player):
        super().__init__(color, title, position, direction, player)
        self.side = BoardSides.RIGHT
        self.castling_done = False
        self.in_check = False
        self.figures_that_threaten_check = []

    def set_in_check(self, in_check, figures_that_threaten_chess):
        self.in_check = in_check
        self.figures_that_threaten_check = figures_that_threaten_chess

    def get_in_check(self):
        return self.in_check

    def set_board_side(self, new_side):
        self.side = new_side

    def get_figures_that_threaten_check(self):
        return self.figures_that_threaten_check

    def is_position_in_check(self, position_to_test):
        other_player = self.player.get_other_player()
        for figure in other_player.player_figures:
            figure_moves = figure.get_moves()
            figure_causes_check = len(
                list(filter(lambda pos: pos.to_string() == position_to_test.to_string(), figure_moves))) > 0
            if figure_causes_check:
                return True
        return False

    def get_moves(self):
        starting_x_index = get_x_index(self.position.x) - 1
        starting_y_index = get_y_index(self.position.y) - 1
        x_indexes = [starting_x_index, starting_x_index + 1, starting_x_index + 2]
        y_indexes = [starting_y_index, starting_y_index + 1, starting_y_index + 2]
        moves_arr = []

        for y_index in y_indexes:
            if y_index < 0 or y_index > 7:
                continue
            y = ChessBoard.y_positions[y_index]
            for x_index in x_indexes:
                if x_index < 0 or x_index > 7:
                    continue
                x = ChessBoard.x_positions[x_index]
                pos = get_position(x, y)
                if self.is_position_valid(pos):
                    moves_arr.append(pos)

        return moves_arr

    def check_move_for_board_side(self, pos):
        if pos.x < 'E':
            self.set_board_side(BoardSides.LEFT)
        else:
            self.set_board_side(BoardSides.RIGHT)

    def check_for_castling(self, moves):  # TODO: implement castling
        pass

    def get_moving_options(self):
        moves = self.get_moves()
        king_valid_moves = list(filter(lambda pos: not self.is_position_in_check(pos), moves))
        if len(king_valid_moves) > 0:
            self.check_for_castling(king_valid_moves)
            print("Select your next move: \n")
            for i in range(len(king_valid_moves)):
                print(str(i) + " : " + king_valid_moves[i].to_string())
            new_pos = king_valid_moves[int(input())]
            self.check_move_for_board_side(new_pos)
            self.move(new_pos)
            return
        self.get_next_move(king_valid_moves)
