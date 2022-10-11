from figures import Pawn, Rook, Bishop, Knight, King, Queen


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

def letter_to_number(field):
    # example: a1 > 1.1; c1 > 3.1
    letters_board = ["a", "b", "c", "d", "e", "f", "g", "h"]
    numbers_board = ['8', '7', '6', '5', '4', '3', '2', '1']
    board = [str(i) + str(j) for i in letters_board for j in numbers_board]
    if field in board:
        new_field = str(numbers_board.index(field[-1])) + '.' + str(letters_board.index(field[0]))
        return new_field


def get_figure_dest_field(cor_figures):

    figure = input('figure - ')
    field = input('start - ')
    step = input('step - ')

    numeric_field = letter_to_number(field)
    numeric_step = letter_to_number(step)
    for i in cor_figures:
        if i[1] == figure and i[-1] == numeric_field:
            return [i[0], numeric_step]


def change_pawn_with_any_figure(cor_figures, taken_figures, cor_figurs):
    color = 'white'
    pawn = 'w_p'
    index_desk = '0'
    if cor_figures[0][1] == 'b':
        color = 'black'
        pawn = 'b_p'
        index_desk = '7'
    choice_player = None

    if taken_figures:
        for i in cor_figurs:
            if i[1] == pawn and i[-1][0] == index_desk:
                print(taken_figures)
                while choice_player not in taken_figures:
                    choice_player = input('Please choose a figure: ')
                figure = get_figure(choice_player)(color, i[-1], choice_player)
                cor_figurs.remove(i)
                cor_figurs.append([figure, figure.name, figure.field])
                taken_figures.remove(choice_player)
                break