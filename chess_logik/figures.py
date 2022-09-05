import copy
class Boards_field:
    letters_board = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers_board = ['8', '7', '6', '5', '4', '3', '2', '1']
    board = [str(i) + "." + str(j) for i in range(0, 8) for j in range(0, 8)]

def get_field(field):
    board_field = Boards_field()

    numeric_field = letter_to_number1(field)
    if numeric_field in board_field.board:
        return numeric_field
    else:
        raise ValueError

def letter_to_number1(field):  # example: a1 > 1.1; c1 > 3.1
    board_field = Boards_field()
    new_field = str(board_field.numbers_board.index(field[-1])) + '.' + str(board_field.letters_board.index(field[0]))
    if new_field in board_field.board:
        return new_field
    else:
        return None

def number_to_letter(list_moves):  # example: 1.1 > a1; 3.1 > c1
    moves_list = []
    board_field = Boards_field()
    for i in list_moves:
        b = str(board_field.letters_board[int(i[-1])]) + str(board_field.numbers_board[int(i[0])])
        moves_list.append(b)
    return moves_list

def get_figure(figure):
    dict_class_figurs = {'k': King,
         'q': Queen,
         'r': Rook,
         'b': Bishop,
         'kn': Knight,
         'p': Pawn}
    if figure[2:] in dict_class_figurs:
        return dict_class_figurs[figure[2:]]
    else:
        raise ValueError('Not exist figure')




class Figure(Boards_field):

    def __init__(self, field):
        self.field = field
        # self.figura = figure

    def list_available_moves(self, color, desk):  # list_available_moves(),
        pass

    def validate_move(self, dest_field, color, desk):  # informującą, czy możliwy jest ruch na wskazane pole.
        if dest_field in self.list_available_moves(color, desk):
            return dest_field
        else:
            return []


class Pawn(Figure):
    def list_available_moves(self, color, desk):
        list_moves = []
        cor_left = str(int(self.field[0]) - 1) + '.' + str(int(self.field[-1]) - 1)
        cor_right = str(int(self.field[0]) - 1) + '.' + str(int(self.field[-1]) + 1)
        cor_x = -1
        color_figure = 'b'
        first_step = -2
        if self.field in self.board:
            if color == 'black':
                color_figure = 'w'
                cor_x = 1
                first_step = 2
                cor_left = str(int(self.field[0]) + 1) + '.' + str(int(self.field[-1]) - 1)
                cor_right = str(int(self.field[0]) + 1) + '.' + str(int(self.field[-1]) + 1)
            if self.field[0] == '6' or self.field[0] == '1':
                try:
                    first_step = desk[int(self.field[0]) + first_step ][int(self.field[-1])]
                    if first_step in self.board:
                        list_moves.append(first_step)
                except IndexError:
                    pass
            try:
                step=desk[int(self.field[0]) + cor_x][int(self.field[-1])][0]
                if step != 'w' or step != 'b':
                    list_moves.append(str(int(self.field[0]) + cor_x) + '.' + self.field[-1])

                a = desk[int(cor_left[0])][int(cor_left[-1])]
                if a[0] == color_figure:
                    if cor_left in self.board:
                        list_moves.append(cor_left)
                b  = desk[int(cor_right[0])][int(cor_right[-1])]
                if b[0] == color_figure:
                    if cor_right in self.board:
                        list_moves.append(cor_right)
            except IndexError:
                pass
        return list_moves


class Rook(Figure):
    def list_available_moves(self, color, desk):
        numeric_field = self.field
        list_moves = []
        color_figure = 'b'
        cor = [-1, 1]
        value_for_while = 0
        if self.field in self.board:
            if color == 'black':
                color_figure = 'w'
            count = 1
            for i in cor:
                while value_for_while == 0:
                    new_numeric_field = str(int(numeric_field[0]) + i) + '.' + numeric_field[-1]
                    if new_numeric_field not in self.board:
                        break
                    try:
                        float(desk[int(new_numeric_field[0])][int(new_numeric_field[-1])])
                        list_moves.append(new_numeric_field)
                        numeric_field = new_numeric_field
                    except ValueError:
                        if desk[int(new_numeric_field[0])][int(new_numeric_field[-1])][0] == color_figure:
                            list_moves.append(new_numeric_field)
                        break
                numeric_field = self.field

            for i in cor:
                while value_for_while == 0:
                    new_numeric_field = numeric_field[0] + '.' + str(int(numeric_field[-1]) + i)
                    if new_numeric_field not in self.board:
                        break
                    try:
                        float(desk[int(new_numeric_field[0])][int(new_numeric_field[-1])])
                        list_moves.append(new_numeric_field)
                        numeric_field = new_numeric_field
                    except ValueError:
                        if desk[int(new_numeric_field[0])][int(new_numeric_field[-1])][0] == color_figure:
                            list_moves.append(new_numeric_field)
                        break
                numeric_field = self.field
        return list_moves


class Bishop(Figure):
    def list_available_moves(self, color, desk):
        list_moves = []
        numeric_field = self.field
        color_figure = 'b'
        field = ''
        cor_move_bishop = [[1, 1], [-1, -1], [1, -1], [-1, 1]]

        if color == 'black':
            color_figure = 'w'

        for i in cor_move_bishop:

            while numeric_field in self.board:

                x = int(numeric_field[0])
                y = int(numeric_field[-1])
                new_numeric_field = str(x + i[0]) + "." + str(y + i[-1])

                if not new_numeric_field in self.board:
                    numeric_field = self.field
                    break
                try:
                    field = desk[int(new_numeric_field[0])][int(new_numeric_field[-1])]
                    float(field)
                    list_moves.append(new_numeric_field)
                    numeric_field = new_numeric_field

                except ValueError:
                    if field[0] == color_figure:
                        list_moves.append(new_numeric_field)
                    numeric_field = self.field
                    break

        return list_moves

class Knight(Figure):
    def list_available_moves(self, color, desk):
        list_moves = []
        color_figure = 'b'
        list_cor = [
            [-1, 2],
            [-2, 1],
            [-2, -1],
            [-1, -2],
            [1, -2],
            [2, -1],
            [2, 1],
            [1, 2],
        ]
        if self.field in self.board:
            if color == 'black':
                color_figure = 'w'

            for i in list_cor:
                x = int(self.field[0]) + i[0]
                y = int(self.field[-1]) + i[-1]
                cor_xy = str(x) + "." + str(y)
                if cor_xy in self.board:
                    field = desk[x][y]
                    try:
                        float(field)
                        list_moves.append(cor_xy)
                    except ValueError:
                        if field[0] == color_figure:
                            list_moves.append(cor_xy)

        return list_moves


class Queen(Figure):
    def list_available_moves(self, color, desk):
        bishop = Bishop(self.field)
        rook = Rook(self.field)
        list_moves_bishop = bishop.list_available_moves(color, desk)
        list_moves_rook = rook.list_available_moves(color, desk)
        for i in list_moves_rook:
            list_moves_bishop.append(i)
        return list_moves_bishop


class King(Figure):

    def list_available_moves(self, color, desk):

        list_moves = []
        color_figure = 'b'
        list_cor = [
            [-1, 1],
            [1, 1],
            [1, -1],
            [-1, -1],
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1],
        ]
        if self.field in self.board:
            if color == 'black':
                color_figure = 'w'

            for i in list_cor:
                x = int(self.field[0]) + i[0]
                y = int(self.field[-1]) + i[1]
                cor_xy = str(x) + "." + str(y)
                if cor_xy in self.board:
                    field = desk[x][y]
                    try:
                        float(field)
                        list_moves.append(cor_xy)
                    except ValueError:
                        if field[0] == color_figure:
                            list_moves.append(cor_xy)

        return list_moves

    def validate_move(self, dest_field, color,
                      desk):  # król musi sprawdzić czy nie zagrożone jest pole na ktore pojdzie
        numeric_dest_field = letter_to_number1(dest_field)
        if numeric_dest_field not in self.list_available_moves(color, desk):
            return []
        kings_cor = ['w_k', numeric_dest_field]
        if color == 'black':
            kings_cor[0] = 'b_k'

        if not self.checkmate_check(kings_cor, desk):
            return numeric_dest_field

    def checkmate_check(self, kings_cor, desk):
        color = 'black'
        color_figure = 'b'
        if kings_cor[0][0] == 'b':
            color_figure = 'w'
            color = 'white'

        for i in desk:
            for j in i:
                if j[0] == color_figure:
                    field = str(desk.index(i)) + '.' + str(i.index(j))
                    class_figure = get_figure(j)(field)
                    list_move = class_figure.list_available_moves(color, desk)
                    if kings_cor[-1] in list_move:
                        return 'check'


class Watcher:

    def avoiding_checkmate(self, kings_cor, desk, field):

        color_figure = 'w'
        color = 'white'

        list_move = [field]
        cor = [1, 1]
        list_avoiding_checkmate = []

        if kings_cor[0][0] == 'b':
            color_figure = 'b'
            color = 'black'
        # Sprawdzam jaka figura zagraza i jakie pola mogą zapobiec zagrozeniu Króla. Pola zapisuje do listy 'list_move'.

        x = abs(int(kings_cor[-1][0]) - int(field[0]))
        y = abs(int(kings_cor[-1][-1]) - int(field[-1]))
        check_knight = str(x) + '.' + str(y)
        if check_knight != '1.2' and check_knight != '2.1':
            if field[0] > kings_cor[-1][0]:
                cor[0] = -1
            if field[-1] > kings_cor[-1][-1]:
                cor[-1] = -1
            if field[0] == kings_cor[-1][0] and field[-1] != kings_cor[-1][-1]:
                cor[0] = 0
            elif field[0] != kings_cor[-1][0] and field[-1] == kings_cor[-1][-1]:
                cor[-1] = 0

            value_for_while = field
            while float(value_for_while) != float(kings_cor[-1]):

                new_field = str(int(value_for_while[0]) + cor[0]) + '.' + str(int(value_for_while[-1]) + cor[-1])
                if new_field != kings_cor[-1]:
                    list_move.append(new_field)
                value_for_while = new_field
        # Sprawdzam na jakie pole moze uciec Król. Zapisuje od razu do listy 'list_avoiding_checkmate'.
        King = get_figure(kings_cor[0])(kings_cor[-1])
        list_move_king = King.list_available_moves(color, desk)
        for i in list_move_king:
            list_avoiding_checkmate.append([kings_cor[0], kings_cor[-1], i])

        # Mając pola ktore mogą zapobiec zagrozeniu, sprwdzam każdą figure, jakie wszystkie mozliwe ruchy  moze wykonac. Jak w liscie ruchów figury jest pole z listy
        # list_move to zapisuje tą figure do listy 'list_avoiding_checkmate'
        for i in desk:
            for j in i:
                if j[0] == color_figure and j[-1] != 'k':
                    desk_checmate_check = copy.deepcopy(desk)
                    field_figure = str(desk_checmate_check.index(i)) + '.' + str(i.index(j))
                    class_figure = get_figure(j)(field_figure)
                    list_move_figure = class_figure.list_available_moves(color, desk_checmate_check)
                    for k in list_move_figure:
                        if k in list_move:

                            desk_checmate_check[int(field_figure[0])][int(field_figure[-1])] = str(desk_checmate_check.index(i)) + '.' + str(i.index(j))
                            desk_checmate_check[int(k[0])][int(k[-1])] = j
                            checmate_check = King.checkmate_check(kings_cor, desk_checmate_check)
                            if not checmate_check:
                                list_avoiding_checkmate.append([j, field_figure, k])

        return list_avoiding_checkmate