import copy

class Figure():
    move = True
    board = [str(i) + "." + str(j) for i in range(0, 8) for j in range(0, 8)]

    def __init__(self, color, field, name):
        self.name = name
        self.color = color
        self.field = field

    def list_available_moves(self, desk):
        pass

    def make_move(self, dest_field, desk, cor_opponents_figures, cor_figures):
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


class Queen(Figure):
    def list_available_moves(self, desk):
        b = 'w_b'
        r = 'w_r'
        if self.color == 'black':
            b = 'b_b'
            r = 'b_r'
        bishop = Bishop(self.color, self.field, b)
        rook = Rook(self.color, self.field, r)
        list_moves_bishop = bishop.list_available_moves(desk)
        list_moves_rook = rook.list_available_moves(desk)
        list_move_queen = list_moves_bishop.__add__(list_moves_rook)

        return list_move_queen


class King(Figure):
    def list_available_moves(self, desk):

        list_moves = []
        opponents_figure = 'b'
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

        if self.color == 'black':
            opponents_figure = 'w'

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
                    if field[0] == opponents_figure:
                        list_moves.append(cor_xy)
        return list_moves

    def castling_king(self, list_moves, cor_opponents_figures, cor_figures, desk):
        # sprawdza czy mozliwa jest roszada
        king_cor = '7.4'
        rook = 'w_r'
        if self.color == 'black':
            king_cor = '0.4'
            rook = 'b_r'
        cor = [-1, 1]
        castling = 'long'
        watcher = Watcher()
        opponents_figure_move = watcher.dict_avalible_move_figures(cor_opponents_figures, desk)
        for i in cor:
            cor_for_castling = king_cor
            while cor_for_castling in self.board:
                cor_for_castling = cor_for_castling[:2] + str(int(cor_for_castling[-1]) + i)
                figure = desk[int(cor_for_castling[0])][int(cor_for_castling[-1])]
                if figure == rook:
                    for key in cor_figures.keys():
                        if figure in key and cor_for_castling in key:
                            if key[0].move:
                                list_moves.append('{} castling'.format(castling))
                try:
                    float(figure)
                    for value in opponents_figure_move.values():
                        if figure in value:
                            break
                except ValueError:
                    break

    def make_castling(self, cor_figures, step):
        # robie roszade na desce (wpisuje odpowiednie kordynaty do krola i wierzy)
        short_castling = [['w_k', '7.4', '7.6'], ['w_r', '7.7', '7.5']]
        long_castling = [['w_k', '7.4', '7.1'], ['w_r', '7.0', '7.2']]

        if self.color == 'black':
            short_castling = [['b_k', '0.4', '0.6'], ['b_r', '0.7', '0.5']]
            long_castling = [['b_k', '0.4', '0.1'], ['b_r', '0.0', '0.2']]
        castling = short_castling
        if step == 'long castling':
            castling = long_castling

        for key in cor_figures:
            if castling[0][0] in key:
                key[0].field = castling[0][-1]
            elif castling[1][0] in key and castling[1][1] in key:
                key[0].field = castling[1][-1]

    def make_move(self, dest_field, desk, cor_opponents_figures, cor_figures):
        # wykonuje ruch
        list_moves = self.list_available_moves(desk)

        watcher = Watcher()
        dict_avalible_moves_opponents = watcher.dict_avalible_move_figures(cor_opponents_figures, desk)
        for i in  list_moves[-1::1]:
            for value in dict_avalible_moves_opponents.values():
                if i in value:
                    list_moves.remove(i)

        if self.move:
            self.castling_king(list_moves, cor_opponents_figures, cor_figures, desk)

        if dest_field in list_moves:
            try:
                float(dest_field)
                self.move = False
                self.field = dest_field
            except ValueError:
                self.make_castling(cor_figures, dest_field)
            return True



class Watcher():
    def dict_avalible_move_figures(self, cor_figures, desk):
        #zwraca dict key-figure, value-list_avalible_move
        dict_avalible_moves = {}

        for i in cor_figures:
            figure = i[0]
            list_moves = figure.list_available_moves(desk)
            dict_avalible_moves[tuple(i)] = list_moves

        return dict_avalible_moves

    def search_possible_fields(self, kings_cor, field):
        # sprawdzam jakie pola są pomiędzy Królem i zagrażającą figurą

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

    def search_possible_figure(self, cor_figures, kings_cor, desk, possible_fields):
        # wyszukuje figure ktora moze uratowac krola od zagrazenia
        list_possible_figure = []

        dict_avalible_move = self.dict_avalible_move_figures(cor_figures, desk)
        dict_avalible_move.pop(tuple(kings_cor))

        for i in possible_fields:
            for kej, value in dict_avalible_move.items():
                if i in value:
                    list_possible_figure.append([kej[0], kej[1], kej[-1], i])

        return list_possible_figure

    def check_list_avoiding_checkmate(self, list_avoiding_checkmate, kings_cor, desk, cor_opponents_figures):
        # tworze kopie deski i robie krok z list_avoiding_checkmate
        for i in list_avoiding_checkmate[-1::-1]:
            desk_checmate_check = copy.deepcopy(desk)
            desk_checmate_check[int(i[2][0])][int(i[2][-1])] = i[2]
            desk_checmate_check[int(i[-1][0])][int(i[-1][-1])] = i[1]
            kings_field = None

            # wyciagam aktualne kordynaty krola
            for j in desk_checmate_check:
                for k in j:
                    if k == kings_cor[0]:
                        kings_field = str(desk_checmate_check.index(j)) + '.' + str(j.index(k))

            dict_avalible_move_oponents = self.dict_avalible_move_figures(cor_opponents_figures, desk_checmate_check)

            # sprawcdazam czy po zrobionym kroku, krol dalej jest zagrozony
            for j in dict_avalible_move_oponents.values():
                if kings_field in j:
                    list_avoiding_checkmate.remove(i)
                    break
        return list_avoiding_checkmate

    def avoiding_checkmate(self, kings_cor, desk, field, cor_figures, cor_opponents_figures):
        # funkcja szuka wszystkie mozliwe ruchy ktorzy moga urotowac krola
        # + w tym mozliwy ruchy krola ktore moga zapobiec zagrozenia
        king = None
        list_move_king = []
        possible_fields = self.search_possible_fields(kings_cor, field)
        possible_figure = self.search_possible_figure(cor_figures, kings_cor, desk, possible_fields)

        for i in cor_figures:
            if kings_cor[0] in i:
                king = i[0]
        list_available_moves_king = king.list_available_moves(desk)

        for i in list_available_moves_king:
            list_move_king.append([king, king.name, king.field, i])

        list_avoiding_checkmate = possible_figure.__add__(list_move_king)

        verified_list_avoiding_checkmate = self.check_list_avoiding_checkmate(list_avoiding_checkmate, kings_cor, desk, cor_opponents_figures)

        return verified_list_avoiding_checkmate