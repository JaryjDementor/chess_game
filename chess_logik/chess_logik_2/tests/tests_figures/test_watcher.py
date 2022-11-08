from unittest import TestCase, main
from chess_logik.chess_logik_2.figures import Watcher, King, Queen, Knight, Rook, Bishop, Pawn
from chess_logik.chess_logik_2.models import Board
from chess_logik.chess_logik_2.models import Cor_Figures


class WatcherTest(TestCase):
    class_board = Board()
    watcher = Watcher()
    w_k = King('white', '7.4', 'w_k')
    w_q = Queen('white', '7.3', 'w_q')
    w_r = Rook('white', '7.0', 'w_r')
    w_kn = Knight('white', '7.1', 'w_kn')
    w_b = Bishop('white', '7.2', 'w_b')
    w_p = Pawn('white', '6.4', 'w_p')

    b_k = King('black', '0.4', 'b_k')
    b_q = Queen('black', '0.3', 'b_q')
    b_r = Rook('black', '0.0', 'b_r')
    b_kn = Knight('black', '0.1', 'b_kn')
    b_b = Bishop('black', '0.2', 'b_b')
    b_p = Pawn('black', '1.4', 'b_p')

    cor_white_figure = [[w_k, w_k.name, w_k.field], [w_q, w_q.name, w_q.field], [w_r, w_r.name, w_r.field], [w_kn, w_kn.name, w_kn.field], [w_b, w_b.name, w_b.field], [w_p, w_p.name, w_p.field]]
    cor_black_figure = [[b_k, b_k.name, b_k.field], [b_q, b_q.name, b_q.field], [b_r, b_r.name, b_r.field], [b_kn, b_kn.name, b_kn.field], [b_b, b_b.name, b_b.field], [b_p, b_p.name, b_p.field]]

    def test_white_dict_avalible_move_figures(self):
        board = self.class_board.start(self.cor_white_figure, self.cor_black_figure)

        dict_avalible_avalible_move = self.watcher.dict_avalible_move_figures(self.cor_white_figure, board)
        expected_result = {(self.w_k, 'w_k', '7.4'): ['6.5', '6.3', '7.5'],
                           (self.w_q, 'w_q', '7.3'): ['6.2', '5.1', '4.0', '6.3', '5.3', '4.3', '3.3', '2.3', '1.3', '0.3'],
                           (self.w_r, 'w_r', '7.0'): ['6.0', '5.0', '4.0', '3.0', '2.0', '1.0', '0.0'],
                           (self.w_kn, 'w_kn', '7.1'): ['6.3', '5.2', '5.0'],
                           (self.w_b, 'w_b', '7.2'): ['6.1', '5.0', '6.3', '5.4', '4.5', '3.6', '2.7'],
                           (self.w_p, 'w_p', '6.4'): ['5.4', '4.4']}
        self.assertEqual(dict_avalible_avalible_move, expected_result)

    def test_black_dict_avalible_move_figures(self):
        board = self.class_board.start(self.cor_white_figure, self.cor_black_figure)

        dict_avalible_avalible_move = self.watcher.dict_avalible_move_figures(self.cor_black_figure, board)
        expected_result = {(self.b_k, 'b_k', '0.4'): ['1.5', '1.3', '0.5'],
                           (self.b_q, 'b_q', '0.3'): ['1.2', '2.1', '3.0', '1.3','2.3', '3.3', '4.3', '5.3','6.3', '7.3'],
                           (self.b_r, 'b_r', '0.0'): ['1.0', '2.0', '3.0', '4.0','5.0', '6.0', '7.0'],
                           (self.b_kn, 'b_kn', '0.1'): ['2.0', '2.2', '1.3'],
                           (self.b_b, 'b_b', '0.2'): ['1.3', '2.4', '3.5','4.6', '5.7', '1.1','2.0'],
                           (self.b_p, 'b_p', '1.4'): ['2.4', '3.4']}

        self.assertEqual(dict_avalible_avalible_move, expected_result)

    def test_search_possible_fields_white(self):
        kings_cor = ['w_k', '7.4']

        cor_knight = '5.3'
        expected_result_knight = ['5.3']
        possible_fields = self.watcher.search_possible_fields(kings_cor, cor_knight)
        self.assertEqual(possible_fields, expected_result_knight)

        cor_rook = '3.4'
        expected_result_rook = ['3.4', '4.4', '5.4', '6.4']
        possible_fields = self.watcher.search_possible_fields(kings_cor, cor_rook)
        self.assertEqual(possible_fields, expected_result_rook)

        cor_bishop = '4.7'
        expected_result_bishop = ['4.7', '5.6', '6.5']
        possible_fields = self.watcher.search_possible_fields(kings_cor, cor_bishop)
        self.assertEqual(possible_fields, expected_result_bishop)

    def test_search_possible_fields_black(self):
        kings_cor = ['b_k', '0.4']

        cor_knight = '2.3'
        expected_result_knight = ['2.3']
        possible_fields = self.watcher.search_possible_fields(kings_cor, cor_knight)
        self.assertEqual(possible_fields, expected_result_knight)

        cor_rook = '3.4'
        expected_result_rook = ['3.4', '2.4', '1.4']
        possible_fields = self.watcher.search_possible_fields(kings_cor, cor_rook)
        self.assertEqual(possible_fields, expected_result_rook)

        cor_bishop = '3.7'
        expected_result_bishop = ['3.7', '2.6', '1.5']
        possible_fields = self.watcher.search_possible_fields(kings_cor, cor_bishop)
        self.assertEqual(possible_fields, expected_result_bishop)




        # cor_white_figure = [['w_k', 'w_k', '7.4']]
        # cor_black_knight = [['b_kn', 'b_kn', '5.3']]
        # cor_black_rook = [['b_r', 'b_r', '3.4']]
        # cor_black_bishop = [['b_b', 'b_b', '4.7']]
        #
        # board = self.class_board.start(cor_white_figure, cor_black_bishop)
        # for i in board:
        #     print(i)


        # print(possible_fields)







if __name__ == '__main__':
    main()
