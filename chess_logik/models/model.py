import pandas as pd

class Color_figure:

    def get_white_figures(self):
        white_figurs = [['w_k', 'e1'], ['w_q', 'd1'], ['w_r', 'a1'], ['w_r', 'h1'], ['w_b', 'c1'], ['w_b', 'f1'], ['w_kn', 'b1'], ['w_kn', 'g1'], ['w_p', 'a2'], ['w_p', 'b2'], ['w_p', 'c2'], ['w_p', 'd2'], ['w_p', 'e2'], ['w_p', 'f2'], ['w_p', 'g2'], ['w_p', 'h2']]
        return white_figurs

    def get_black_figures(self):
        black_figurs = [['b_k', 'e8'], ['b_q', 'd8'], ['b_r', 'a8'], ['b_r', 'h8'], ['b_b', 'c8'], ['b_b', 'f8'],
                        ['b_kn', 'b8'], ['b_kn', 'g8'], ['b_p', 'a7'], ['b_p', 'b7'], ['b_p', 'c7'], ['b_p', 'd7'], ['b_p', 'e7'], ['b_p', 'f7'], ['b_p', 'g7'], ['b_p', 'h7']]

        return black_figurs



class Board:
    def konstructor_board(self):
        field = ['', '', '', '', '', '', '', '']
        board = []
        for i in range(8):
            board.append(field)

        board = pd.DataFrame(board, index=[8, 7, 6, 5, 4, 3, 2, 1], columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

        return board


class User(Color_figure):
    def __int__(self, name):
        self.name = name


class Player1(User):

    def figures(self):
        figurs = self.get_white_figures()
        return figurs



class Player2(User):

    def figures(self):
        figurs = self.get_black_figures()
        return figurs



class Move:

    def start(self, cor_player1, cor_player2):
        class_board = Board()
        board = class_board.konstructor_board()
        for i in cor_player1:
            board.at[int(i[1][1]), i[1][0]] = i[0]

        for i in cor_player2:
            board.at[int(i[1][1]), i[1][0]] = i[0]
        return board

