from typing import Union

from models.ChessBoard import ChessBoard, initial_figures_mapping
from models.Figures.Bishop import Bishop
from models.Figures.King import King
from models.Figures.Knight import Knight
from models.Figures.Pawn import Pawn
from models.Figures.Queen import Queen
from models.Figures.Rook import Rook
from models.Postion import Position


class Player:
    number_of_figures = 16

    def init_figures(self):
        initial_indexes_for_player = []
        if self.number == 0:
            initial_indexes_for_player.extend((0, 1))
        else:
            initial_indexes_for_player.extend([6, 7])
        for index_of_number in range(len(ChessBoard.y_positions)):
            for index_of_letter in range(len(ChessBoard.x_positions)):
                if index_of_number not in initial_indexes_for_player:  # this condition will only be satisfied by empty rows initially
                    continue
                pos: Position = ChessBoard.positions[index_of_number][index_of_letter]
                figure: Union[Bishop, King, Knight, Pawn, Queen, Rook, None] = None
                if index_of_number == 1 or index_of_number == 6:  # these are the rows were the Pawns are initially
                    figure = Pawn(self.figures_color, '', pos)
                else:
                    figure = initial_figures_mapping[pos.to_string()](
                        self.figures_color, '', pos)
                figure.set_title(type(figure).__name__)
                pos.set_chess_figure(figure)
                self.player_figures.append(figure)
    def __init__(self, number, name, color):
        self.number = number
        self.name = name
        self.figures_color = color
        self.player_figures = [] * self.number_of_figures
        self.init_figures()
