from unittest import TestCase, main
from chess_logik.chess_logik_2.figures import Watcher
from chess_logik.chess_logik_2.models import Board
from chess_logik.chess_logik_2.models import Cor_Figures


class WatcherTest(TestCase):
    class_board = Board()
    cor_figures = Cor_Figures()
    cor_white_figure = cor_figures.cor_white()
    cor_black_figure = cor_figures.cor_black()

    def test_white_dict_avalible_move_figures(self):




if __name__ == '__main__':
    main()
