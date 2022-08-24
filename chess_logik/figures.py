
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
        numeric_dest_field = letter_to_number1(dest_field)
        if numeric_dest_field in self.list_available_moves(color, desk):
            return dest_field
        else:
            return []


class Pawn(Figure):
    def list_available_moves(self, color, desk):
        list_moves = []
        numeric_field = letter_to_number1(self.field)
        cor_left = str(int(numeric_field[0]) - 1) + '.' + str(int(numeric_field[-1]) - 1)
        cor_right = str(int(numeric_field[0]) - 1) + '.' + str(int(numeric_field[-1]) + 1)
        cor_x = -1
        color_figure = 'b'

        if self.field in self.board:
            if color == 'black':
                color_figure = 'w'
                cor_x = 1
        try:
            step = desk[int(numeric_field[0]) + cor_x][int(numeric_field[-1])][0]
            if step != 'w' or step != 'b':
                list_moves.append(str(int(numeric_field[0]) + cor_x) + '.' + numeric_field[-1])
        except ValueError:
            pass

        if desk[int(cor_left[0])][int(cor_left[-1])][0] == color_figure:
            list_moves.append(cor_left)

        if desk[int(cor_right[0])][int(cor_right[-1])][0] == color_figure:
            list_moves.append(cor_right)

        return list_moves


class Rook(Figure):
    def list_available_moves(self, color, desk):
        numeric_field = letter_to_number1(self.field)
        list_moves = []
        color_figure = 'b'

        if self.field in self.board:
            if color == 'black':
                color_figure = 'w'

        for i in self.board:
            if i != numeric_field:
                avalible_field = desk[int(i[0])][int(i[-1])]
                if numeric_field[0] == i[0]:
                    list_moves.append(i)
                    try:
                        float(avalible_field)
                    except ValueError:
                        if avalible_field[0] == color_figure:
                            list_moves.append(i)
                        break
        for i in self.board:
            if i != numeric_field:
                avalible_field = desk[int(i[0])][int(i[-1])]
                if numeric_field[-1] == i[-1]:
                    list_moves.append(i)
                    try:
                        float(avalible_field)
                    except ValueError:
                        if avalible_field[0] == color_figure:
                            list_moves.append(i)
                        break
        return set(list_moves)


class Bishop(Figure):
    def list_available_moves(self, color, desk):
        list_moves = []
        numeric_field = letter_to_number1(self.field)
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
                    numeric_field = letter_to_number1(self.field)
                    break
                try:
                    field = desk[int(new_numeric_field[0])][int(new_numeric_field[-1])]
                    float(field)
                    list_moves.append(new_numeric_field)
                    numeric_field = new_numeric_field

                except ValueError:
                    if field[0] == color_figure:
                        list_moves.append(new_numeric_field)
                    numeric_field = letter_to_number1(self.field)
                    break

        return list_moves

class Knight(Figure):
    def list_available_moves(self, color, desk):
        numeric_field = letter_to_number1(self.field)
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
        if numeric_field in self.board:
            if color == 'black':
                color_figure = 'w'

            for i in list_cor:
                x = int(numeric_field[0]) + i[0]
                y = int(numeric_field[-1]) + i[-1]
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

        numeric_field = letter_to_number1(self.field)
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
        if numeric_field in self.board:
            if color == 'black':
                color_figure = 'w'

            for i in list_cor:
                x = int(numeric_field[0]) + i[0]
                y = int(numeric_field[-1]) + i[1]
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

    def validate_move(self, dest_field, color, desk): # król musi sprawdzić czy nie zagrożone jest pole na ktore pojdzie
        numeric_dest_field = letter_to_number1(dest_field)
        if numeric_dest_field not in self.list_available_moves(color, desk):
            return []

        color_figure = 'b'
        if color == 'black':
            color_figure = 'w'

        count_row = -1
        count_column = -1
        for row in desk:
            count_row += 1
            for col in row:
                count_column += 1
                if col[0] == color_figure:
                    field = number_to_letter([str(count_row) + '.' + str(count_column)])[0]

                    class_figure = get_figure(col)(field)
                    if numeric_dest_field in class_figure.list_available_moves(color, desk):
                        return []
            count_column = -1
        return numeric_dest_field
