from figures import Pawn, Rook, Bishop, Knight, Watcher
from dataclasses import make_dataclass


class Board():

    def konstructor_board(self):
        board = []
        count = 0

        for i in range(8):
            row = []
            for j in range(8):
                row.append(str(count) + '.' + str(j))
            count += 1
            board.append(row)

        return board

    def start(self, cor_player1, cor_player2):
        board = self.konstructor_board()

        for i in board:
            for j in cor_player1:
                if j[-1] in i:
                    board[int(j[-1][0])][int(j[-1][-1])] = j[1]

            for k in cor_player2:
                if k[-1] in i:
                    board[int(k[-1][0])][int(k[-1][-1])] = k[1]


        return board

class Chess_Figures():
    def white_figures(self):
        w_r_1 = Rook('white', '7.0', 'w_r')
        w_r_2 = Rook('white', '7.7', 'w_r')

        w_kn_1 = Knight('white', '7.1', 'w_kn')
        w_kn_2 = Knight('white', '7.6', 'w_kn')

        w_b_1 = Bishop('white', '7.2', 'w_b')
        w_b_2 = Bishop('white', '7.5', 'w_b')

        w_p_1 = Pawn('white', '6.0', 'w_p')
        w_p_2 = Pawn('white', '6.1', 'w_p')
        w_p_3 = Pawn('white', '6.2', 'w_p')
        w_p_4 = Pawn('white', '6.3', 'w_p')
        w_p_5 = Pawn('white', '6.4', 'w_p')
        w_p_6 = Pawn('white', '6.5', 'w_p')
        w_p_7 = Pawn('white', '6.6', 'w_p')
        w_p_8 = Pawn('white', '6.7', 'w_p')
        return [w_r_1, w_r_2, w_kn_1, w_kn_2, w_b_1, w_b_2, w_p_1, w_p_2, w_p_3, w_p_4, w_p_5, w_p_6, w_p_7, w_p_8]

    def black_figures(self):
        b_r_1 = Rook('black', '0.7', 'b_r')
        b_r_2 = Rook('black', '0.0', 'b_r')

        b_kn_1 = Knight('black', '0.6', 'b_kn')
        b_kn_2 = Knight('black', '0.1', 'b_kn')

        b_b_1 = Bishop('white', '0.5', 'b_b')
        b_b_2 = Bishop('white', '0.2', 'b_b')

        b_p_1 = Pawn('black', '1.0', 'b_p')
        b_p_2 = Pawn('black', '1.1', 'b_p')
        b_p_3 = Pawn('black', '1.2', 'b_p')
        b_p_4 = Pawn('black', '1.3', 'b_p')
        b_p_5 = Pawn('black', '1.4', 'b_p')
        b_p_6 = Pawn('black', '1.5', 'b_p')
        b_p_7 = Pawn('black', '1.6', 'b_p')
        b_p_8 = Pawn('black', '1.7', 'b_p')
        return [b_r_1, b_r_2, b_kn_1, b_kn_2, b_b_1, b_b_2, b_p_1, b_p_2, b_p_3, b_p_4, b_p_5, b_p_6, b_p_7, b_p_8]


class Cor_Figures(Chess_Figures):

    def cor_white(self):
        coordinates = []
        class_figures = self.white_figures()
        for i in class_figures:
            coordinates.append([i, i.name, i.field])
        return coordinates

    def cor_black(self):
        coordinates = []
        class_figures = self.black_figures()
        for i in class_figures:
            coordinates.append([i, i.name, i.field])
        return coordinates




class User(Cor_Figures):
    def __init__(self, name):
        self.name = name



class Player1(User):
    taken_figure = []

    def list_figures(self):
        figures = self.cor_white()
        return figures





class Player2(User):
    taken_figure = []

    def list_figures(self):
        figures = self.cor_black()
        return figures








pl1 = Player1('bob')
pl2 = Player2('ron')

a = Board()

board = a.start(pl1.cor_white(), pl2.cor_black())

# for i in board:
#     print(i)

cor = pl1.cor_white()

# for i in cor:
#     print(i[1], i[0].list_available_moves(board))

# print(pl1.cor_white())
#
w = Watcher()
d = w.dict_avalible_move_figures(pl1.cor_white(), board)

for key, value in d.items():
    print(key, value)