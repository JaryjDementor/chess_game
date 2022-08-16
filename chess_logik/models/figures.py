from ..controler import number_to_letter, letter_to_number1

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
    def list_available_moves(self):
        list_moves = []
        for i in self.board:
            if self.field[0] == i[0] or self.field[-1] == i[-1]:
                list_moves.append(i)
        list_moves.remove(self.field)
        return list_moves


class Bishop(Figure):
    def list_available_moves(self):
        super().list_available_moves()
        number_field_for_while = self.field

        list_moves = []
        while number_field_for_while in self.board:
            x = int(number_field_for_while[0])
            y = int(number_field_for_while[-1])
            new_number_field_for_while = str(x + 1) + "." + str(y + 1)
            if new_number_field_for_while in self.board:
                list_moves.append(new_number_field_for_while)
                number_field_for_while = new_number_field_for_while
            else:
                number_field_for_while = self.field
                break
        while number_field_for_while in self.board:
            x = int(number_field_for_while[0])
            y = int(number_field_for_while[-1])
            new_number_field_for_while = str(x - 1) + "." + str(y - 1)
            if new_number_field_for_while in self.board:
                list_moves.append(new_number_field_for_while)
                number_field_for_while = new_number_field_for_while
            else:
                number_field_for_while = self.field
                break
        while number_field_for_while in self.board:
            x = int(number_field_for_while[0])
            y = int(number_field_for_while[-1])
            new_number_field_for_while = str(x + 1) + "." + str(y - 1)
            if new_number_field_for_while in self.board:
                list_moves.append(new_number_field_for_while)
                number_field_for_while = new_number_field_for_while
            else:
                number_field_for_while = self.field
                break
        while number_field_for_while in self.board:
            x = int(number_field_for_while[0])
            y = int(number_field_for_while[-1])
            new_number_field_for_while = str(x - 1) + "." + str(y + 1)
            if new_number_field_for_while in self.board:
                list_moves.append(new_number_field_for_while)
                number_field_for_while = new_number_field_for_while
            else:
                number_field_for_while = new_number_field_for_while
                break

        return list_moves


class King(Figure):
    def list_available_moves(self):

        list_moves = []
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
        for i in list_cor:
            x = int(self.field[0]) + i[0]
            y = int(self.field[-1]) + i[1]
            cor_xy = str(x) + "." + str(y)
            if x != 0 and y != 0 and cor_xy in self.board:
                list_moves.append(cor_xy)
        return list_moves


class Queen(Figure):
    def list_available_moves(self):
        bishop = Bishop(self.field)
        rook = Rook(self.field)
        list_moves_bishop = bishop.list_available_moves()
        list_moves_rook = rook.list_available_moves()
        for i in list_moves_rook:
            list_moves_bishop.append(i)
        return list_moves_bishop

class Knight(Figure):
    def list_available_moves(self):
        list_moves = []
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
        for i in list_cor:
            x = int(self.field[0]) + i[0]
            y = int(self.field[-1]) + i[-1]
            cor_xy = str(x) + "." + str(y)
            if x > 0 and y > 0 and cor_xy in self.board:
                list_moves.append(cor_xy)
        return list_moves


# class Pawn(Figure):
#     def list_available_moves(self):
#
#         if self.field in self.board and self.field[-1] != "8":
#             list_moves = []
#             y = int(self.field[-1]) + 1
#
#             list_moves.append(self.field[:2] + str(y))
#             return list_moves
#         else:
#             return []


