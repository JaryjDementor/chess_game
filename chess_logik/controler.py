from models.figures import Boards_field, King, Queen, Rook, Bishop, Pawn, Knight, letter_to_number1, number_to_letter
from models.model import Player1, Player2, Move

def get_field(field):
    board_field = Boards_field()

    numeric_field = letter_to_number1(field)
    if numeric_field in board_field.board:
        return numeric_field
    else:
        raise ValueError

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


class Game():
    def get(self, name_player1, name_player2):
        game = Move()
        player1 = Player1()
        player1.name, cordinates_figures_player1 = name_player1, player1.figures()

        player2 = Player2()
        player2.name, cordinates_figures_player2 = name_player2, player2.figures()

        board = game.start(cordinates_figures_player1, cordinates_figures_player2)
        print(board)
        value_for_while = 0
        queue = 'player1'

        while value_for_while == 0:

            figure = input('figure - ')

            try:
                get_figure(figure)
            except ValueError:
                print('Not exist figure')
            else:  # nie potrzebny
                field = input('start - ')
                try:
                    get_field(field)
                except ValueError:
                    print('Not exist field')
                else:
                    numeric_field = get_field(field)
                    if numeric_field and board.at[int(field[1]), field[0]] == figure:
                        step = input('step - ')

                        class_figure = get_figure(figure)(numeric_field)
                        numeric_dest_field = get_field(step)
                        dest_field = class_figure.validate_move(numeric_dest_field)
                        if dest_field:
                            if queue == 'player1':
                                for i in cordinates_figures_player1:
                                    if i[1] == field:
                                        i[1] = step
                                queue = 'player2'
                            elif queue == 'player2':
                                for i in cordinates_figures_player2:
                                    if i[1] == field:
                                        i[1] = step
                                queue = 'player1'
                            start_game = game.start(cordinates_figures_player1, cordinates_figures_player2)
                            print(start_game)
                        else:
                            print('Invalid move')

                    else:
                        print('There is no {} figure on the {} field'.format(figure, field))




# a=Game()
#
# print(a.get('bob', 'rob'))