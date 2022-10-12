from unittest import TestCase, main
from chess_logik.chess_logik_2.figures import Pawn
from chess_logik.chess_logik_2.models import Board

class PawnTest(TestCase):
    player1 =[['class_pawn', 'w_p', '6.1']]
    player2 = [['class_pawn', 'b_p', '1.1']]
    white_pawn = Pawn('white', '6.1', 'w_p')
    black_pawn = Pawn('black', '1.1', 'b_p')
    class_board = Board()

    def test_first_move(self):
        board = self.class_board.start(self.player1, self.player2)
        list_move_white_pawn = ['5.1']
        list_move_black_pawn = ['2.1']

        self.white_pawn.first_move(list_move_white_pawn, board)
        self.black_pawn.first_move(list_move_black_pawn, board)

        self.assertEqual(list_move_white_pawn, ['5.1', '4.1'])
        self.assertEqual(list_move_black_pawn, ['2.1', '3.1'])

    def test_kill_figure_white_pawn(self):
        list_move = ['5.1']

        left_white_kill_figure = [['class_pawn', 'b_p', '5.0']]
        board = self.class_board.start(self.player1, left_white_kill_figure)

        self.white_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['5.1', '5.0'])

        right_white_kill_figure = [['class_pawn', 'b_p', '5.2']]
        board = self.class_board.start(self.player1, right_white_kill_figure)
        list_move = ['5.1']

        self.white_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['5.1', '5.2'])

        left_right_white_kill_figure = [['class_pawn', 'b_p', '5.0'], ['class_pawn', 'b_p', '5.2']]
        board = self.class_board.start(self.player1, left_right_white_kill_figure)
        list_move = ['5.1']

        self.white_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['5.1', '5.0', '5.2'])

    def test_kill_figure_black_pawn(self):
        list_move = ['2.1']

        left_black_kill_figure = [['class_pawn', 'w_p', '2.2']]
        board = self.class_board.start(self.player2, left_black_kill_figure)

        self.black_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['2.1', '2.2'])

        right_black_kill_figure = [['class_pawn', 'w_p', '2.0']]
        board = self.class_board.start(self.player2, right_black_kill_figure)
        list_move = ['2.1']

        self.black_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['2.1', '2.0'])

        left_right_black_kill_figure = [['class_pawn', 'w_p', '2.2'], ['class_pawn', 'w_p', '2.0']]
        board = self.class_board.start(self.player2, left_right_black_kill_figure)
        list_move = ['2.1']

        self.black_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['2.1', '2.0', '2.2'])




if __name__ == '__main__':
    main()
