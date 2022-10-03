
class Figure():
    move = True
    board = [str(i) + "." + str(j) for i in range(0, 8) for j in range(0, 8)]

    def __init__(self, color, field, name):
        self.name = name
        self.color = color
        self.field = field

    def list_available_moves(self, desk):
        pass

    def make_move(self, dest_field, desk):  # informującą, czy możliwy jest ruch na wskazane pole.
        if dest_field in self.list_available_moves(desk):
            self.move = False
            self.field = dest_field
            return True



class Pawn(Figure):



    def first_move(self, list_move, desk):
        first_step = -2
        if self.color == 'black':
            first_step = 2
        field = str(int(self.field[0]) + first_step) + self.field[1:]
        step = desk[int(field[0])][int(field[-1])]
        try:
            float(step)
            list_move.append(field)
        except IndexError:
            pass
        except ValueError:
            pass

    def kill_figure(self, list_move, desk):
        cor_left = str(int(self.field[0]) - 1) + '.' + str(int(self.field[-1]) - 1)
        cor_right = str(int(self.field[0]) - 1) + '.' + str(int(self.field[-1]) + 1)
        color_figure = 'b'
        if self.color == 'black':
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

    def list_available_moves(self, desk):
        # example figure on board 'w_p'/'b_p' - white/black pawn

        list_moves = []
        cor_x = -1

        if self.color == 'black':
            cor_x = 1
        try:
            step = desk[int(self.field[0]) + cor_x][int(self.field[-1])][0]
            if step != 'w' or step != 'b':
                list_moves.append(str(int(self.field[0]) + cor_x) + '.' + self.field[-1])
        except IndexError:
            pass
        if self.move:
            self.first_move(list_moves, desk)

        self.kill_figure(list_moves, desk)

        return list_moves


class Rook(Figure):
    def list_available_moves(self, desk):
        list_moves = []
        field = self.field
        opponents_figure = 'b'
        cor = [-1, 1]
        if self.color == 'black':
            opponents_figure = 'w'

        for i in cor:
            while True:
                new_field = str(int(field[0]) + i) + '.' + field[-1]

                if new_field not in self.board:
                    break
                try:
                    float(desk[int(new_field[0])][int(new_field[-1])])
                    list_moves.append(new_field)
                    field = new_field
                except ValueError:
                    if desk[int(new_field[0])][int(new_field[-1])][0] == opponents_figure:
                        list_moves.append(new_field)
                    break
            field = self.field

        for i in cor:
            while True:
                new_field = field[0] + '.' + str(int(field[-1]) + i)

                if new_field not in self.board:
                     break
                try:
                    float(desk[int(new_field[0])][int(new_field[-1])])
                    list_moves.append(new_field)
                    field = new_field
                except ValueError:
                    if desk[int(new_field[0])][int(new_field[-1])][0] == opponents_figure:
                        list_moves.append(new_field)
                    break
            field = self.field
        return list_moves

class Bishop(Figure):
    def list_available_moves(self, desk):
        list_moves = []
        numeric_field = self.field
        opponents_figure = 'b'
        field = ''
        cor_move_bishop = [[1, 1], [-1, -1], [1, -1], [-1, 1]]

        if self.color == 'black':
            opponents_figure = 'w'

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
                    if field[0] == opponents_figure:
                        list_moves.append(new_numeric_field)
                    numeric_field = self.field
                    break
        return list_moves

class Knight(Figure):

    def list_available_moves(self, desk):
        list_moves = []
        opponents_figure = 'b'
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
        if self.color == 'black':
            opponents_figure = 'w'

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
                    if field[0] == opponents_figure:
                        list_moves.append(cor_xy)
        return list_moves