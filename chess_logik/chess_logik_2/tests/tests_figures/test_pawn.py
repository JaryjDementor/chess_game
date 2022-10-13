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

        white_pawn_left_kill_figure = [['class_pawn', 'b_p', '5.0']]
        board = self.class_board.start(self.player1, white_pawn_left_kill_figure)

        self.white_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['5.1', '5.0'])

        white_pawn_right_kill_figure = [['class_pawn', 'b_p', '5.2']]
        board = self.class_board.start(self.player1, white_pawn_right_kill_figure)
        list_move = ['5.1']

        self.white_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['5.1', '5.2'])

        white_pawn_left_right_kill_figure = [['class_pawn', 'b_p', '5.0'], ['class_pawn', 'b_p', '5.2']]
        board = self.class_board.start(self.player1, white_pawn_left_right_kill_figure)
        list_move = ['5.1']

        self.white_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['5.1', '5.0', '5.2'])

    def test_kill_figure_black_pawn(self):
        list_move = ['2.1']

        black_pawn_left_kill_figure = [['class_pawn', 'w_p', '2.2']]
        board = self.class_board.start(self.player2, black_pawn_left_kill_figure)

        self.black_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['2.1', '2.2'])

        black_pawn_right_kill_figure = [['class_pawn', 'w_p', '2.0']]
        board = self.class_board.start(self.player2, black_pawn_right_kill_figure)
        list_move = ['2.1']

        self.black_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['2.1', '2.0'])

        black_pawn_left_right_kill_figure = [['class_pawn', 'w_p', '2.2'], ['class_pawn', 'w_p', '2.0']]
        board = self.class_board.start(self.player2, black_pawn_left_right_kill_figure)
        list_move = ['2.1']

        self.black_pawn.kill_figure(list_move, board)
        self.assertEqual(list_move, ['2.1', '2.0', '2.2'])

    def test_list_available_moves_white_pawn(self):
        player2 = [['class_pawn', 'b_p', '5.0']]
        board = self.class_board.start(self.player1, player2)

        list_moves = self.white_pawn.list_available_moves(board)
        self.assertEqual(list_moves, ['5.1', '4.1', '5.0'])

        player2 = [['class_pawn', 'b_p', '5.1']]
        board = self.class_board.start(self.player1, player2)

        list_moves = self.white_pawn.list_available_moves(board)
        self.assertEqual(list_moves, [])


    def test_list_available_moves_black_pawn(self):
        player1 = [['class_pawn', 'w_p', '2.2']]
        board = self.class_board.start(player1, self.player2)
        list_move = self.black_pawn.list_available_moves(board)
        self.assertEqual(list_move, ['2.1', '3.1', '2.2'])

        player1 = [['class_pawn', 'w_p', '2.1']]
        board = self.class_board.start(player1, self.player2)

        list_move = self.black_pawn.list_available_moves(board)
        self.assertEqual(list_move, [])

    def test_make_move(self):
        board = self.class_board.start(self.player1, self.player2)

        self.white_pawn.make_move('5.1', board, self.player2, self.player1)
        self.assertEqual(self.white_pawn.field, '5.1')

        self.black_pawn.make_move('2.1', board, self.player1, self.player2)
        self.assertEqual(self.black_pawn.field, '2.1')



if __name__ == '__main__':
    main()
