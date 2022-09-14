import copy

def change_pawn_with_any_figure(color, desk, taken_figures):
    pawn = 'w_p'
    index_desk = 0
    if color == 'black':
        pawn = 'b_p'
        index_desk = 7
    choice_player = None
    field = None
    count = 0
    if taken_figures:
        for i in desk[index_desk]:
            if i == pawn:
                print(taken_figures)
                while choice_player not in taken_figures:
                    choice_player = input('Please choose a figure: ')
                field = str(index_desk) + '.' + str(count)

                desk[index_desk][count] = choice_player
                taken_figures.remove(choice_player)
                break
            count += 1

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
        king = 'w_k'
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
                king = 'b_k'

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

    def validate_move(self, dest_field, color, desk):
        list_moves = self.list_available_moves(color, desk)
        watcher = Watcher()
        dict_avalible_move_oponents = watcher.dict_avalible_move_oponents(color, desk)
        invalid_move = []

        for i in list_moves:
            for j in dict_avalible_move_oponents.values():
                if i in j:
                    invalid_move.append(i)
                    break
        for i in invalid_move:
            list_moves.remove(i)

        if dest_field in list_moves:
            return dest_field


class Watcher:
    def dict_avalible_move_oponents(self, color, desk):
        # potrzebuje zmiany coloru dla funkcji King.validat_move
        dict_avalible_moves = {}
        color_figures = 'b'
        color_for_figure = 'black'
        count = 0
        if color == 'black':
            color_for_figure = 'white'
            color_figures = 'w'

        for i in desk:
            for j in i:
                field = str(desk.index(i)) + '.' + str(count)
                if j[0] == color_figures:
                    class_figure = get_figure(j)(field)
                    list_moves = class_figure.list_available_moves(color_for_figure, desk)
                    if list_moves:
                        dict_avalible_moves[(j, field)] = list_moves
                count += 1
            count = 0
        return dict_avalible_moves

    def avoiding_checkmate(self, kings_cor, desk, field):

        color = 'white'
        color_oponents = 'black'
        list_move = [field]
        cor = [1, 1]
        list_avoiding_checkmate = []

        if kings_cor[0][0] == 'b':
            color = 'black'
            color_oponents = 'white'

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
        King = get_figure(kings_cor[0])(kings_cor[-1])
        list_move_king = King.list_available_moves(color, desk)
        ivalid_move = []
        for i in list_move_king:
            dest_field = King.validate_move(i, color, desk)
            if not dest_field:
                ivalid_move.append(i)
        for i in ivalid_move:
            list_move_king.remove(i)

        for i in list_move_king:
            list_avoiding_checkmate.append([kings_cor[0], kings_cor[-1], i])

        dict_avalible_move = self.dict_avalible_move_oponents(color_oponents, desk)
        dict_avalible_move.pop(tuple(kings_cor))

        for i in list_move:
            for j, k in dict_avalible_move.items():
                if i in k:
                    list_avoiding_checkmate.append([j[0], j[-1], i])

        # musze sprawdzic czy po kroku figury, z listy list_avoiding_checkmate,
        # nie bedzie znowu zagrozenia

        ivalid_move = []
        for i in list_avoiding_checkmate:
            desk_checmate_check = copy.deepcopy(desk)
            desk_checmate_check[int(i[1][0])][int(i[1][-1])] = i[1]
            desk_checmate_check[int(i[-1][0])][int(i[-1][-1])] = i[0]
            kings_field = None

            # wyciagam nowe/stare kordynaty king
            for j in desk_checmate_check:
                for k in j:
                    if k == kings_cor[0]:
                        kings_field = str(desk_checmate_check.index(j)) + '.' + str(j.index(k))

            dict_avalible_move_oponents = self.dict_avalible_move_oponents(color, desk_checmate_check)

            for j in dict_avalible_move_oponents.values():
                if kings_field in j:
                    ivalid_move.append(i)
                    break
        for i in ivalid_move:
            list_avoiding_checkmate.remove(i)
        return list_avoiding_checkmate