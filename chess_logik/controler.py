from models import Player1, Player2, Move
from figures import get_figure, get_field, letter_to_number1, King, Watcher


class Game():
    def get(self, name_player1, name_player2):
        game = Move()
        player1 = Player1()
        player1.name, cordinates_figures_player1 = name_player1, player1.figures()

        player2 = Player2()
        player2.name, cordinates_figures_player2 = name_player2, player2.figures()

        start_game = game.start(cordinates_figures_player1, cordinates_figures_player2)
        for i in start_game:
            print(i)
        value_for_while = 0
        queue = 'player1'
        color = 'white'
        color_figure = 'b'
        king = 'b_k'
        opponents_figure = None
        list_avoiding_checkmate = []
        while value_for_while == 0:

            figure = input('figure - ')

            try:
                get_figure(figure)
                field = input('start - ')
                try:
                    get_field(field)
                    numeric_field = get_field(field)
                    if start_game[int(numeric_field[0])][int(numeric_field[-1])] == figure:
                        step = input('step - ')
                        numeric_step = letter_to_number1(step)
                        print('du', list_avoiding_checkmate)
                        if not list_avoiding_checkmate or [figure, numeric_field,numeric_step] in list_avoiding_checkmate:
                            class_figure = get_figure(figure)(numeric_field)
                            dest_field = class_figure.validate_move(numeric_step, color, start_game)
                            if dest_field:
                                if queue == 'player1':
                                    for i in cordinates_figures_player1:
                                        if i[1] == numeric_field:
                                            i[1] = numeric_step
                                            opponents_figure = start_game[int(numeric_step[0])][int(numeric_step[-1])]
                                            if [opponents_figure, numeric_step] in cordinates_figures_player2:
                                                cordinates_figures_player2.remove([opponents_figure, numeric_step])
                                                player1.taken_figure.append(opponents_figure)


                                    queue = 'player2'
                                    color = 'black'
                                    king = 'b_k'
                                elif queue == 'player2':
                                    for i in cordinates_figures_player2:
                                        if i[1] == numeric_field:
                                            numeric_step = letter_to_number1(step)
                                            i[1] = numeric_step
                                            opponents_figure = start_game[int(numeric_step[0])][int(numeric_step[-1])]
                                            if [opponents_figure, numeric_step] in cordinates_figures_player1:
                                                cordinates_figures_player1.remove([opponents_figure, numeric_step])
                                                player2.taken_figure.append(opponents_figure)
                                    queue = 'player1'
                                    color = 'white'
                                    king = 'w_k'
                            start_game = game.start(cordinates_figures_player1, cordinates_figures_player2)
                            print(queue)
                            print('oponents figure', player2.taken_figure)
                            kings_field = ''
                            count = 0
                            for i in start_game:
                                print(i)
                                for j in i:
                                    if j == king:
                                        kings_field = str(start_game.index(i)) + '.' + str(count)
                                    count+=1
                                count = 0
                            print('oponents figure', player1.taken_figure)
                            opponents_figure = None
                            watcher = Watcher()
                            dict_avalible_move_oponents = watcher.dict_avalible_move_oponents(color, start_game)
                            for i in dict_avalible_move_oponents.values():

                                if kings_field in i:
                                    print('ugroza korolu', i)
                                    list_avoiding_checkmate = watcher.avoiding_checkmate([king, kings_field], start_game, numeric_step)
                                    print('vozmoznye vychody s mata', list_avoiding_checkmate)
                                    if list_avoiding_checkmate == []:
                                        value_for_while = 1
                                else:
                                    list_avoiding_checkmate = []


                except ValueError:
                    print('Not exist field')
                except IndexError:
                    print('Not exist field')
            except ValueError:
                print('Not exist figure')

        return print('Winner {}'.format(queue))





a=Game()

print(a.get('bob', 'rob'))