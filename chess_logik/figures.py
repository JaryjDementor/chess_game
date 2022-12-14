import copy

def make_move(cor_figures, field, dest_field):
    for i in cor_figures:
        if i[1] == field:
            i[1] = dest_field

def make_castling(color, cor_figures, step): #+
    short_castling = [['w_k', '7.4', '7.6'], ['w_r', '7.7', '7.5']]
    long_castling = [['w_k', '7.4', '7.1'], ['w_r', '7.0', '7.2']]
    if color == 'black':
        short_castling = [['b_k', '0.4', '0.6'], ['b_r', '0.7', '0.5']]
        long_castling = [['b_k', '0.4', '0.1'], ['b_r', '0.0', '0.2']]
    if step == 'short castling':
        for i in cor_figures:
            if i[0] == short_castling[0][0]:
                i[-1] = short_castling[0][-1]
            elif i[0] == short_castling[-1][0] and i[-1] == short_castling[-1][1]:
                i[-1] = short_castling[-1][-1]
    else:
        for i in cor_figures:
            if i[0] == long_castling[0][0]:
                i[-1] = long_castling[0][-1]
            elif i[0] == long_castling[-1][0] and i[-1] == long_castling[-1][1]:
                i[-1] = long_castling[-1][-1]

def move_player(desk): #+
    figure = input('figure - ')
    try:
        get_figure(figure)
        field = input('start - ')
        try:
            get_field(field)
            numeric_field = get_field(field)
            if desk[int(numeric_field[0])][int(numeric_field[-1])] == figure:
                step = input('step - ')
                if step == 'short castling' or step == 'long castling':
                    return [figure, numeric_field, step]
                numeric_step = letter_to_number1(step)
                return [figure, numeric_field, numeric_step]

            print('Not exist figure')
        except ValueError:
            print('Not exist field')
        except IndexError:
            print('Not exist field')
    except ValueError:
        print('Not exist figure')



def change_pawn_with_any_figure(color, taken_figures, cor_figurs): #+
    pawn = 'w_p'
    index_desk = '0'
    if color == 'black':
        pawn = 'b_p'
        index_desk = '7'
    choice_player = None
    if taken_figures:
        for i in cor_figurs:
            if i[0] == pawn and i[-1][0] == index_desk:
                print(taken_figures)
                while choice_player not in taken_figures:
                    choice_player = input('Please choose a figure: ')
                i[0] = choice_player
                taken_figures.remove(choice_player)
                break

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

    def validate_move(self, dest_field, color, desk):  # informuj??c??, czy mo??liwy jest ruch na wskazane pole.
        if dest_field in self.list_available_moves(color, desk):
            return dest_field
        else:
            return []


class Pawn(Figure): #+

    def first_move(self, list_move, color, desk):
        first_step = -2
        if color == 'black':
            first_step = 2
        field = str(int(self.field[0]) + first_step) + self.field[1:]
        try:
            if field in self.board:
                step = desk[int(field[0])][int(field[-1])]
                float(step)
                list_move.append(step)
        except IndexError:
            pass
        except ValueError:
            pass

    def kill_figure(self, list_move, color, desk):
        cor_left = str(int(self.field[0]) - 1) + '.' + str(int(self.field[-1]) - 1)
        cor_right = str(int(self.field[0]) - 1) + '.' + str(int(self.field[-1]) + 1)
        color_figure = 'b'
        if color == 'black':
            cor_left = str(int(self.field[0]) + 1) + '.' + str(int(self.field[-1]) - 1)
            cor_right = str(int(self.field[0]) + 1) + '.' + str(int(self.field[-1]) + 1)
            color_figure = 'w'
        try:
            oponents_figure = desk[int(cor_left[0])][int(cor_left[-1])]
            if cor_left in self.board and oponents_figure[0] == color_figure:
                list_move.append(cor_left)
        except IndexError:
            pass
        try:
            oponents_figure = desk[int(cor_right[0])][int(cor_right[-1])]
            if cor_right in self.board and oponents_figure[0] == color_figure:
                list_move.append(cor_right)
        except IndexError:
            pass

    def list_available_moves(self, color, desk):
        # example figure on board 'w_p'/'b_p' - white/black pawn

        list_moves = []
        cor_x = -1

        if color == 'black':
            cor_x = 1
        try:
            step=desk[int(self.field[0]) + cor_x][int(self.field[-1])][0]
            if step != 'w' or step != 'b':
                list_moves.append(str(int(self.field[0]) + cor_x) + '.' + self.field[-1])
        except IndexError:
            pass
        if self.field[0] == '6' or self.field[0] == '1':
            self.first_move(list_moves, color, desk)

        self.kill_figure(list_moves, color, desk)

        return list_moves


class Rook(Figure): #+
    def list_available_moves(self, color, desk):
        numeric_field = self.field
        list_moves = []
        color_figure = 'b'
        cor = [-1, 1]
        if self.field in self.board:
            if color == 'black':
                color_figure = 'w'

            for i in cor:
                while True:
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
                while True:
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


class Bishop(Figure): #+
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

                if new_numeric_field not in self.board:
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

class Knight(Figure): #+
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
        if color == 'black':
            color_figure = 'w'

        if self.field in self.board:

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


class Queen(Figure):#+
    def list_available_moves(self, color, desk):
        bishop = Bishop(self.field)
        rook = Rook(self.field)
        list_moves_bishop = bishop.list_available_moves(color, desk)
        list_moves_rook = rook.list_available_moves(color, desk)
        for i in list_moves_rook:
            list_moves_bishop.append(i)
        return list_moves_bishop


class King(Figure): #+
    count_move = 0

    def list_available_moves(self, color, desk):
        # king = 'w_k'
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
                # king = 'b_k'
            if self.count_move == 0:
                castling_list = self.castling_king(color, desk)
                if castling_list:
                    for i in castling_list:
                        list_moves.append(i)

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
        dict_avalible_move_oponents = watcher.dict_avalible_move_figures(color, desk)

        for i in list_moves[-1::1]:
            for j in dict_avalible_move_oponents.values():
                if i in j:
                    list_moves.remove(i)
                    break

        if dest_field in list_moves:
            self.count_move += 1
            return dest_field

    def castling_king(self, color, desk):
        king_cor = '7.4'
        rook = 'w_r'
        if color == 'black':
            king_cor = '0.4'
            rook = 'b_r'
        avalible_castling = []
        cor = [-1, 1]
        value = 'long'
        for i in cor:
            cor_for_castling = king_cor
            while cor_for_castling in self.board:
                cor_for_castling = cor_for_castling[:2] + str(int(cor_for_castling[-1]) + i)
                if cor_for_castling[-1] == '0' or cor_for_castling[-1] == '7':
                    figure = desk[int(cor_for_castling[0])][int(cor_for_castling[-1])]
                    if figure == rook:
                        avalible_castling.append('{} castling'.format(value))
                        break
                try:
                    float(desk[int(cor_for_castling[0])][int(cor_for_castling[-1])])
                except ValueError:
                    break

            value = 'short'

        return avalible_castling


class Watcher:
    def dict_avalible_move_figures(self, color, desk):
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

    def search_possible_fields(self, kings_cor, field):
        cor = [1, 1]
        x = abs(int(kings_cor[-1][0]) - int(field[0]))
        y = abs(int(kings_cor[-1][-1]) - int(field[-1]))
        check_knight = str(x) + '.' + str(y)
        possible_fields = [field]

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
                    possible_fields.append(new_field)
                value_for_while = new_field
        return possible_fields

    def search_possible_figure(self, kings_cor, desk, possible_fields, color):

        list_possible_figure = []

        dict_avalible_move = self.dict_avalible_move_figures(color, desk)
        dict_avalible_move.pop(tuple(kings_cor))

        for i in possible_fields:
            for j, k in dict_avalible_move.items():
                if i in k:
                    list_possible_figure.append([j[0], j[-1], i])
        return list_possible_figure

    def check_list_avoiding_checkmate(self, list_avoiding_checkmate, kings_cor, color, desk):
        for i in list_avoiding_checkmate[-1::-1]:
            desk_checmate_check = copy.deepcopy(desk)
            desk_checmate_check[int(i[1][0])][int(i[1][-1])] = i[1]
            desk_checmate_check[int(i[-1][0])][int(i[-1][-1])] = i[0]
            kings_field = None

            # wyciagam nowe/stare kordynaty king
            for j in desk_checmate_check:
                for k in j:
                    if k == kings_cor[0]:
                        kings_field = str(desk_checmate_check.index(j)) + '.' + str(j.index(k))

            dict_avalible_move_oponents = self.dict_avalible_move_figures(color, desk_checmate_check)

            for j in dict_avalible_move_oponents.values():
                if kings_field in j:
                    list_avoiding_checkmate.remove(i)
                    break
        return list_avoiding_checkmate

    def avoiding_checkmate(self, kings_cor, desk, field):

        color = 'white'
        color_oponents = 'black'
        if kings_cor[0][0] == 'b':
            color = 'black'
            color_oponents = 'white'

        possible_fields = self.search_possible_fields(kings_cor, field)

        list_avoiding_checkmate = self.search_possible_figure(kings_cor, desk, possible_fields, color_oponents)

        King = get_figure(kings_cor[0])(kings_cor[-1])
        list_move_king = King.list_available_moves(color, desk)

        for i in list_move_king[-1::1]:
            dest_field = King.validate_move(i, color, desk)
            if not dest_field:
                list_move_king.remove(i)

        list_avoiding_checkmate = list_avoiding_checkmate.__add__(list_move_king)
        # for i in list_move_king:
        #     list_avoiding_checkmate.append([kings_cor[0], kings_cor[-1], i])

        verified_list_avoiding_checkmate = self.check_list_avoiding_checkmate(list_avoiding_checkmate, kings_cor, color, desk)

        return verified_list_avoiding_checkmate