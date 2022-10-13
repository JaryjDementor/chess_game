from unittest import TestCase, main
from chess_logik.chess_logik_2.figures import Bishop
from chess_logik.chess_logik_2.models import Board

class Bishop_Test(TestCase):
    player1 = [['class_bishop', 'w_b', '6.2']]
    player2 = [['class_bishop', 'b_b', '1.2']]
    white_bishop = Bishop('white', '6.2', 'w_b')
    black_bishop = Bishop('black', '1.2', 'b_b')
    class_board = Board()

    def test_list_available_moves_white_bishop(self):
        board = self.class_board.start(self.player1, self.player2)
        expected_result = ['7.3', '5.1', '4.0', '7.1', '5.3', '4.4', '3.5', '2.6', '1.7']

        list_move = self.white_bishop.list_available_moves(board)
        self.assertEqual(list_move, expected_result)


        player1 = [['class_pawn', 'w_b', '6.2'], ['class_pawn', 'w_p', '5.1']]
        player2 = [['class_rook', 'b_r', '4.4']]
        board = self.class_board.start(player1, player2)
        expected_result = ['7.3', '7.1', '5.3', '4.4']

        list_move = self.white_bishop.list_available_moves(board)
        self.assertEqual(list_move, expected_result)

    def test_list_available_moves_black_bishop(self):
        board = self.class_board.start(self.player1, self.player2)
        expected_result = ['2.3', '3.4', '4.5', '5.6', '6.7', '0.1', '2.1', '3.0', '0.3']

        list_move = self.black_bishop.list_available_moves(board)
        self.assertEqual(list_move, expected_result)

        player1 = [['class_knight', 'w_kn', '2.3'], ['class_pawn', 'w_p', '3.0']]
        player2 = [['class_bishop', 'b_b', '1.2'], ['class_king', 'b_k', '0.3']]
        board = self.class_board.start(player1, player2)
        expected_result = ['2.3', '0.1', '2.1', '3.0']

        list_move = self.black_bishop.list_available_moves(board)
        self.assertEqual(list_move, expected_result)

    def test_make_move_white_bishop(self):

        board = self.class_board.start(self.player1, self.player2)

        self.assertTrue(self.white_bishop.move)
        self.white_bishop.make_move('7.3', board, self.player2, self.player1)
        self.assertEqual(self.white_bishop.field, '7.3')
        self.assertFalse(self.white_bishop.move)

    def test_make_move_black_bishop(self):

        board = self.class_board.start(self.player1, self.player2)

        self.assertTrue(self.black_bishop.move)
        self.black_bishop.make_move('2.3', board, self.player2, self.player1)
        self.assertEqual(self.black_bishop.field, '2.3')
        self.assertFalse(self.black_bishop.move)


if __name__ == '__main__':
    main()