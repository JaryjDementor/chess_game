from models import Board, Player2, Player1
from function import get_figure_dest_field

class Game():
    def get(self):
        game = Board()

        pl1 = Player1('bob')
        pl2 = Player2('ron')

        board = game.start(pl1.cor_white(), pl2.cor_black())

        for i in board:
            print(i)

        queue = 'player1'
        cor_figures = pl1.cor_white()
        cor_opponents_figures = pl2.cor_black()
        opponents_figure = None
        list_avoiding_checkmate = []

        while True:
            figure_dest_field = get_figure_dest_field(cor_figures)
            try:
                figure, dest_field = figure_dest_field
                if figure.make_move(dest_field, board, cor_opponents_figures, cor_figures):
                    if queue == 'player1':
                        cor_opponents_figures = pl1.cor_black()
                        cor_figures = pl2.cor_white()
                        queue = 'player2'
                    elif queue == 'player2':
                        cor_opponents_figures = pl2.cor_black()
                        cor_figures = pl1.cor_black()
                        queue = 'player1'
                    board = game.start(pl1.cor_white(), pl2.cor_black())
                    for i in board:
                        print(i)
            except ValueError:
                print('Incorrect request')






a = Game()

b = a.get()