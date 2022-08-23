

class Color_figure:

    def get_white_figures(self):
        white_figurs = [['w_k', '7.4'], ['w_q', '7.3'], ['w_r', '7.0'], ['w_r', '7.7'], ['w_b', '7.2'], ['w_b', '7.5'],
                        ['w_kn', '7.1'], ['w_kn', '7.6'], ['w_p', '6.0'], ['w_p', '6.1'], ['w_p', '6.2'],
                        ['w_p', '6.3'],['w_p', '6.4'], ['w_p', '6.5'], ['w_p', '6.6'], ['w_p', '6.7']]
        return white_figurs

    def get_black_figures(self):
        black_figurs = [['b_k', '0.4'], ['b_q', '0.3'], ['b_r', '0.0'], ['b_r', '0.7'], ['b_b', '0.2'], ['b_b', '0.5'],
                        ['b_kn', '0.1'], ['b_kn', '0.6'], ['b_p', '1.0'], ['b_p', '1.1'], ['b_p', '1.2'],
                        ['b_p', '1.3'], ['b_p', '1.4'], ['b_p', '1.5'], ['b_p', '1.6'], ['b_p', '1.7']]

        return black_figurs



class Board:
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


class User(Color_figure):
    def __int__(self, name):
        self.name = name

    taken_figure = []


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

        for i in board:
            for j in cor_player1:
                if j[-1] in i:
                    board[int(j[-1][0])][int(j[-1][-1])] = j[0]

            for k in cor_player2:
                if k[-1] in i:
                    board[int(k[-1][0])][int(k[-1][-1])] = k[0]


        return board

# white_figurs = [['w_k', '7.4'], ['w_q', '7.3'], ['w_r', '7.0'], ['w_r','7.7'], ['w_b', '7.2'], ['w_b', '7.5'],
#                 ['w_kn', '7.1'], ['w_kn', '7.6'], ['w_p', '6.0'], ['w_p', '6.1'], ['w_p', '6.2'], ['w_p', '6.3'],
#                 ['w_p', '6.4'], ['w_p', '6.5'], ['w_p', '6.6'], ['w_p', '6.7']]
#
# black_figure = [['b_k', '0.4'], ['b_q', '0.3'], ['b_r', '0.0'], ['b_r', '0.7'], ['b_b', '0.2'], ['b_b', '0.5'],
#                         ['b_kn', '0.1'], ['b_kn', '0.6'], ['b_p', '1.0'], ['b_p', '1.1'], ['b_p', '1.2'], ['b_p', '1.3'], ['b_p', '1.4'], ['b_p', '1.5'], ['b_p', '1.6'], ['b_p', '1.7']]
#
# f=Move()
#
# bor = f.start(white_figurs, black_figure)
#
# for i in bor:
#     print(i)