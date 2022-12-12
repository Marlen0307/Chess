from models.ChessFigure import ChessFigure


class Player:
    number_of_figures = 16

    def init_figures(self):
        player_figures = [ChessFigure()] * self.number_of_figures
        for number in [0, self.number_of_figures - 1]:
            player_figures.append(ChessFigure(self.figures_color, self.tx))

    def __init__(self, number, name, color):
        self.number = number
        self.name = name
        self.figures_color = color
