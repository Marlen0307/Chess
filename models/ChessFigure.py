import json

from Constants import Directions, figures
from models import Postion


def is_position_valid(figure, pos: Postion):
    if pos.occupied:  # if position is occupied by opponent position is valid
        return pos.chess_figure.color != figure.color
    return True  # if position is not occupied position is valid


class ChessFigure:

    def __init__(self, color: str, title: str, position: Postion, direction, player):
        self.position = position
        self.killed = False
        self.color = color
        self.title = title
        self.direction = direction
        self.moved = False
        self.player = player

    def move(self, new_position: Postion):
        if not self.moved:
            self.set_moved(True)
        self.position.set_chess_figure(None)
        self.position = new_position
        if new_position.occupied:
            self.beat(new_position.get_chess_figure())
        new_position.set_chess_figure(self)

    def set_moved(self, is_moved):
        self.moved = is_moved

    def get_direction(self, direction: Directions):
        if direction == Directions.RIGHT or direction == Directions.TOP:
            return 1
        if direction == Directions.LEFT or direction == Directions.BOTTOM:
            return -1

    def get_moved(self):
        return self.moved

    def beat(self, figure_to_beat):
        figure_to_beat.eleminate()

    def set_title(self, new_title: str):
        self.title = new_title

    def get_position(self):
        return self.position.to_string()

    def eleminate(self):
        self.killed = True

    def get_next_move(self, moving_options):
        if len(moving_options) > 0:
            print("Select your next move: \n")
            for i in range(len(moving_options)):
                print(str(i) + " : " + moving_options[i].to_string())
            new_pos = moving_options[int(input())]
            self.move(new_pos)
            return
        print("You do not have any possible moves with this figure! Choose another one")
        print(json.dumps(figures)[1:-1])  # print figure choices
        key = input()
        figure_to_be_moved = figures[int(key)]
        self.player.choose_moving_figure(figure_to_be_moved)
