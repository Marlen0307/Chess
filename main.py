from models.ChessBoard import ChessBoard
from models.Player import Player

players = [] * 2
colors = {
    0: 'white',
    1: 'black'
}

board = ChessBoard()


def init_players():
    for number in [0, 1]:
        num_of_player = number + 1
        default_player_name = "Player " + str(num_of_player)
        player_name = input("Write name for " + default_player_name)
        if player_name == "":
            player_name = default_player_name
        player_color = colors[number]
        players.insert(number, Player(number, player_name, player_color))


def start_game():
    print(board)
    init_players()
    print(players)


start_game()
