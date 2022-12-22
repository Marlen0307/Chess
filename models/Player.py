from typing import Union
from models.Figures.Bishop import Bishop
from models.Figures.King import King
from models.Figures.Knight import Knight
from models.Figures.Pawn import Pawn
from models.Figures.Queen import Queen
from models.Figures.Rook import Rook
from models.Postion import Position
from models.ChessBoard import ChessBoard, get_figures_by_name

initial_figures_mapping = {
    '1A': Rook,
    '8A': Rook,
    '1H': Rook,
    '8H': Rook,
    '1B': Knight,
    '8B': Knight,
    '1G': Knight,
    '8G': Knight,
    '1C': Bishop,
    '8C': Bishop,
    '1F': Bishop,
    '8F': Bishop,
    '1D': Queen,
    '8D': Queen,
    '1E': King,
    '8E': King
}


class Player:
    number_of_figures = 16

    def __init__(self, number, name, color, game):
        self.number = number
        self.name = name
        self.figures_color = color
        self.game = game
        self.player_figures = [] * self.number_of_figures
        self.init_figures()

    def init_figures(self):
        initial_indexes_for_player = []
        if self.number == 0:
            initial_indexes_for_player.extend((0, 1))  # initial positions for player 1
        else:
            initial_indexes_for_player.extend([6, 7])  # initial positions for player 2

        # loop through positions matrix and fill the initial positions with figures
        for index_of_number in range(len(ChessBoard.y_positions)):
            for index_of_letter in range(len(ChessBoard.x_positions)):
                if index_of_number not in initial_indexes_for_player:  # this condition will only be satisfied by empty rows initially
                    continue
                pos: Position = ChessBoard.positions[index_of_number][index_of_letter]
                figure: Union[Bishop, King, Knight, Pawn, Queen, Rook, None] = None
                direction = 1
                if self.number == 1:  # second player figures need to go down the board
                    direction = -1
                if index_of_number == 1 or index_of_number == 6:  # these are the rows were the Pawns are initially
                    figure = Pawn(self.figures_color, '', pos, direction, self)
                else:
                    figure = initial_figures_mapping[pos.to_string()](
                        self.figures_color, '', pos, direction, self)
                figure.set_title(type(figure).__name__)
                pos.set_chess_figure(figure)
                self.player_figures.append(figure)

    def get_other_player(self):
        return list(filter(lambda p: p.number != self.number, self.game.players))[0]

    def look_for_potential_check_on_enemy(self):
        king_figures = get_figures_by_name('King')
        enemy_king = list(filter(lambda f: f.color != self.figures_color, king_figures))[0]
        enemy_king_position = enemy_king.position.to_string()
        figures_that_cause_chess = []
        for figure in self.player_figures:
            figure_moves = figure.get_moves()
            figure_causes_check = len(
                list(filter(lambda pos: pos.to_string() == enemy_king_position, figure_moves))) > 0
            if figure_causes_check:
                figures_that_cause_chess.append(figure)
        enemy_king_in_check = len(figures_that_cause_chess) > 0
        enemy_king.set_in_check(enemy_king_in_check, figures_that_cause_chess)

    def look_for_check_on_your_king(self):
        king = list(filter(lambda figure: figure.title == 'King', self.player_figures))[0]
        if king.get_in_check():
            king_moves = king.get_moves()
            king_valid_moves = list(filter(lambda pos: not king.is_position_in_check(pos), king_moves))
            if len(king_valid_moves) == 0:
                other_player = self.get_other_player()
                self.game.end(other_player)
                return False
            print(self.name + '! You are in check. You must move your king')
            king.get_moving_options()
            return True
        return True

    def move_figure(self, figure_to_be_moved):
        figure_to_be_moved.get_moving_options()
        self.look_for_potential_check_on_enemy()

    def choose_moving_figure(self, figure_name_to_be_moved: str):
        matching_figures = []
        # find figures with the typed name
        for figure in self.player_figures:
            if type(figure).__name__ == figure_name_to_be_moved and not figure.killed:
                matching_figures.append(figure)
        # if matching_figures is empty, that means the figure is killed or does not exist
        if len(matching_figures) == 0:
            print('You do not have this active figure')
        elif len(matching_figures) == 1:
            self.move_figure(matching_figures[0])
        else:
            print("Choose which " + figure_name_to_be_moved + " do you want to move: \n")
            for index in range(len(matching_figures)):
                print(str(index) + " : " + matching_figures[index].get_position() + "\n")
            self.move_figure(matching_figures[int(input())])
