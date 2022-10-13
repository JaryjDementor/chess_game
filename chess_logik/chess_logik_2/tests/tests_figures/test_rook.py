from unittest import TestCase, main
from chess_logik.chess_logik_2.figures import Rook
from chess_logik.chess_logik_2.models import Board

class RookTest(TestCase):
    player1 = [['class_rook', 'w_r', '7.1']]
    player2 = [['class_rook', 'b_r', '0.1']]
    white_rook = Rook('white', '7.1', 'w_r')
    black_rook = Rook('black', '0.1', 'b_r')
    class_board = Board()

    def test_list_available_moves_white_rook(self):

        board = self.class_board.start(self.player1, self.player2)
        expected_result = ['6.1', '5.1', '4.1', '3.1', '2.1', '1.1', '0.1', '7.0', '7.2', '7.3', '7.4', '7.5', '7.6', '7.7']

        list_move = self.white_rook.list_available_moves(board)
        self.assertEqual(list_move, expected_result)

        player1 = [['class_rook', 'w_r', '7.1'], ['class_king', 'w_k', '7.4']]
        player2 = [['class_rook', 'b_r', '0.1'], ['class_pawn', 'b_p', '4.1']]
        board = self.class_board.start(player1, player2)
        expected_result = ['6.1', '5.1', '4.1', '7.0', '7.2', '7.3']

        list_move = self.white_rook.list_available_moves(board)
        self.assertEqual(list_move, expected_result)

    def test_list_available_moves_black_rook(self):

        board = self.class_board.start(self.player1, self.player2)
        expected_result = ['1.1', '2.1', '3.1', '4.1', '5.1', '6.1', '7.1', '0.0', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7']

        list_move = self.black_rook.list_available_moves(board)
        self.assertEqual(list_move, expected_result)

        player1 = [['class_rook', 'w_r', '0.4']]
        player2 = [['class_rook', 'b_r', '0.1'], ['class_pawn', 'b_p', '1.1']]
        board = self.class_board.start(player1, player2)
        expected_result = ['0.0', '0.2', '0.3', '0.4']

        list_move = self.black_rook.list_available_moves(board)
        self.assertEqual(list_move, expected_result)

    def test_make_move_white_rook(self):

        board = self.class_board.start(self.player1, self.player2)

        self.assertTrue(self.white_rook.move)
        self.white_rook.make_move('3.1', board, self.player2, self.player1)
        self.assertEqual(self.white_rook.field, '3.1')
        self.assertFalse(self.white_rook.move)

    def test_make_move_black_rook(self):

        board = self.class_board.start(self.player1, self.player2)

        self.assertTrue(self.black_rook.move)
        self.black_rook.make_move('4.1', board, self.player1, self.player2)
        self.assertEqual(self.black_rook.field, '4.1')
        self.assertFalse(self.black_rook.move)


if __name__ == '__main__':
    main()