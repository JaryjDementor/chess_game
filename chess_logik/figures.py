
def letter_to_number1(field):  # example: a1 > 1.1; c1 > 3.1
    board_field = Boards_field()
    new_field = (
        str(board_field.letters_board.index(field[0]) + 1) + "." + field[1:]
    )
    if new_field in board_field.board:
        return new_field
    else:
        return None

def number_to_letter(list_moves):  # example: 1.1 > a1; 3.1 > c1
    moves_list = []
    for i in list_moves:
        b = Boards_field.letters_board[int(i[0]) - 1] + i[-1]
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


class Boards_field:
    letters_board = ["a", "b", "c", "d", "e", "f", "g", "h"]
    board = [str(i) + "." + str(j) for i in range(1, 9) for j in range(1, 9)]

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
        cor_left = number_to_letter([str(int(self.field[0]) - 1) + '.' + str(int(self.field[-1]) + 1)])[0]
        cor_right = number_to_letter([str(int(self.field[0]) + 1) + '.' + str(int(self.field[0]) + 1)])[0]
        cor_y = 1
        color_figure = 'b'
        field = number_to_letter([self.field])[0]

        if self.field in self.board:
            if color == 'black':
                cor_y = -1
                color_figure = 'w'

            if not desk.at[int(field[-1]) + cor_y, field[0]]:
                list_moves.append(self.field[0] + '.' + str(int(self.field[-1]) + cor_y))

            try:
                if desk.at[int(cor_left[-1]), cor_left[0]][0] == color_figure:
                    list_moves.append(letter_to_number1(cor_left))

            except IndexError:
                pass

            try:
                if desk.at[int(cor_right[-1]), cor_right[0]][0] == color_figure:
                    list_moves.append(letter_to_number1(cor_right))

            except IndexError:
                pass

        return list_moves


class Rook(Figure):
    def list_available_moves(self, color, desk):

        list_moves = []
        color_figure = 'b'

        if self.field in self.board:
            if color == 'black':
                color_figure = 'w'

            for i in self.board:
                if self.field[0] == i[0]:
                    field = number_to_letter([i])[0]

                    if desk.at[int(field[-1]), field[0]]:
                        if desk.at[int(field[-1]), field[0]][0] == color_figure:
                            list_moves.append(i)
                        break

                    list_moves.append(i)

            for i in self.board:
                if self.field[-1] == i[-1]:
                    field = number_to_letter([i])[0]

                    if desk.at[int(field[-1]), field[0]]:
                        if desk.at[int(field[-1]), field[0]][0] == color_figure:
                            list_moves.append(i)
                        break

                    list_moves.append(i)

        return list_moves

class Bishop(Figure):
    def list_available_moves(self, color, desk):
        list_moves = []
        number_field_for_while = self.field
        color_figure = 'b'
        field = ''
        cor_move_bishop = [[1, 1], [-1, -1], [1, -1], [-1, 1]]

        if color == 'black':
            color_figure = 'w'

        for i in cor_move_bishop:

            while number_field_for_while in self.board or number_field_for_while[0] != '8' or number_field_for_while[-1] != '8':

                x = int(number_field_for_while[0])
                y = int(number_field_for_while[-1])
                new_number_field_for_while = str(x + i[0]) + "." + str(y + i[-1])

                if not new_number_field_for_while in self.board:
                    number_field_for_while = self.field
                    break

                field = number_to_letter([new_number_field_for_while])[0]

                try:
                    if desk.at[int(field[-1]), field[0]][0]:
                        number_field_for_while = self.field
                        if desk.at[int(field[-1]), field[0]][0] == color_figure:
                            list_moves.append(new_number_field_for_while)
                        break

                except IndexError:
                    pass

                list_moves.append(new_number_field_for_while)
                number_field_for_while = new_number_field_for_while


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
                    field = number_to_letter([cor_xy])[0]
                    if not desk.at[int(field[-1]), field[0]]:
                        list_moves.append(cor_xy)
                    else:
                        if desk.at[int(field[-1]), field[0]][0] == color_figure:
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
                if x != 0 and y != 0 and cor_xy in self.board:
                    field = number_to_letter([cor_xy])[0]

                    if not desk.at[int(field[-1]), field[0]]:
                        list_moves.append(cor_xy)
                    else:
                        if desk.at[int(field[-1]), field[0]][0] == color_figure:
                            list_moves.append(cor_xy)

        return list_moves

    def validate_move(self, dest_field, color, desk): # król musi sprawdzić czy nie zagrożone pole
        if not dest_field in self.list_available_moves(color, desk):
            return []

        color_figure = 'b'
        if color == 'black':
            color_figure = 'w'

        count_index = 9
        count_column = 0
        for row in desk.values:
            count_index -= 1
            for value in row:
                count_column += 1
                try:
                    if value[0] == color_figure:
                        field = str(count_column) + '.' + str(count_index)
                        class_figure = get_figure(value)(field)
                        if dest_field in class_figure.list_available_moves(color, desk):
                            return []
                except IndexError:
                    pass
            count_column = 0
        return dest_field
