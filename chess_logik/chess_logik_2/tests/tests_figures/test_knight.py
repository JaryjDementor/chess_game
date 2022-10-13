from unittest import TestCase, main
from chess_logik.chess_logik_2.figures import Knight
from chess_logik.chess_logik_2.models import Board

class KnightTest(TestCase):
    player1 = [['class_knight', 'w_kn', '5.2']]
    player2 = [['class_knight', 'b_kn', '2.2']]
    white_knight = Knight('white', '5.2', 'w_kn')
    black_knight = Knight('black', '2.2', 'b_kn')
    class_board = Board()

    def test_list_available_moves_white_knight(self):
        board = self.class_board.start(self.player1, self.player2)
        expected_result = ['4.4', '3.3', '3.1', '4.0', '6.0', '7.1', '7.3', '6.4']

        list_move = self.white_knight.list_available_moves(board)
        self.assertEqual(list_move, expected_result)

        player1 = [['class_knight', 'w_kn', '5.2'], ['class_pawn', 'w_p', '3.3'], ['class_pawn', 'w_p', '6.4']]
        player2 = [['class_knight', 'b_kn', '4.0'], ['class_knight', 'b_kn', '7.3']]
        board = self.class_board.start(player1, player2)
        expected_result = ['4.4', '3.1', '4.0', '6.0', '7.1', '7.3']

        list_move = self.white_knight.list_available_moves(board)
        self.assertEqual(list_move, expected_result)

    def test_list_available_moves_black_knight(self):
        board = self.class_board.start(self.player1, self.player2)
        expected_result = ['1.4', '0.3', '0.1', '1.0', '3.0', '4.1', '4.3', '3.4']

        list_move = self.black_knight.list_available_moves(board)
        self.assertEqual(list_move, expected_result)

        player1 = [['class_pawn', 'w_p', '0.1'], ['class_pawn', 'w_p', '1.4']]
        player2 = [['class_knight', 'b_kn', '2.2'], ['class_knight', 'b_kn', '0.3'], ['class_pawn', 'b_p', '4.1'], ['class_knight', 'b_kn', '3.4']]
        board = self.class_board.start(player1, player2)
        expected_result = ['1.4', '0.1', '1.0', '3.0', '4.3']

        list_move = self.black_knight.list_available_moves(board)
        self.assertEqual(list_move, expected_result)



if __name__ == '__main__':
    main()