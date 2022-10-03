
def letter_to_number(field):  # example: a1 > 1.1; c1 > 3.1
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




    # try:
    #     figure_from_desk = desk[int(numeric_field[0])][int(numeric_field[-1])]
    #     float(numeric_field)
    #     float(numeric_step)
    #     if figure_from_desk != figure:
    #         for i in cor_figures:
    #             if i[-1] == numeric_field:
    #                 return [i[0], numeric_step]
    #     else:
    #         print('Not exist figure')
    #
    # except TypeError:
    #     print('Not exist field')



    #     try:
    #         get_field(field)
    #         numeric_field = get_field(field)
    #         if desk[int(numeric_field[0])][int(numeric_field[-1])] == figure:
    #             step = input('step - ')
    #             if step == 'short castling' or step == 'long castling':
    #                 return [figure, numeric_field, step]
    #             numeric_step = letter_to_number1(step)
    #             return [figure, numeric_field, numeric_step]
    #
    #         print('Not exist figure')
    #     except ValueError:
    #         print('Not exist field')
    #     except IndexError:
    #         print('Not exist field')
    # except ValueError:
    #     print('Not exist figure')
