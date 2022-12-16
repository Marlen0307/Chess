from models import Postion


class ChessFigure:

    def __init__(self, color: str, title: str, position: Postion, direction):
        self.position = position
        self.killed = False
        self.color = color
        self.title = title
        self.direction = direction
        self.moved = False

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

    def get_moved(self):
        return self.moved

    def beat(self, figure_to_beat):  # TODO: IMPLEMENT BEAT METHOD
        figure_to_beat.eleminate()

    def set_title(self, new_title: str):
        self.title = new_title

    def get_position(self):
        return self.position.to_string()

    def eleminate(self):
        self.killed = True
