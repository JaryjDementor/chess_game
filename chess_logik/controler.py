from models import Player1, Player2, Move
from figures import get_figure, get_field, letter_to_number1


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
        opponents_figure = None
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

                        class_figure = get_figure(figure)(numeric_field)
                        dest_field = class_figure.validate_move(step, color, start_game)
                        if dest_field:
                            if queue == 'player1':
                                for i in cordinates_figures_player1:
                                    if i[1] == numeric_field:
                                        numeric_step = letter_to_number1(step)
                                        i[1] = numeric_step
                                        opponents_figure = start_game[int(numeric_step[0])][int(numeric_step[-1])]
                                        if [opponents_figure, numeric_step] in cordinates_figures_player2:
                                            cordinates_figures_player2.remove([opponents_figure, numeric_step])
                                            player1.taken_figure.append(opponents_figure)

                                queue = 'player2'
                                color = 'black'

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
                            start_game = game.start(cordinates_figures_player1, cordinates_figures_player2)
                            print('oponents figure', player2.taken_figure)
                            for i in start_game:
                                print(i)
                            print('oponents figure', player1.taken_figure)
                            opponents_figure = None
                except ValueError:
                    print('Not exist field')
            except ValueError:
                print('Not exist figure')





a=Game()

print(a.get('bob', 'rob'))