from models import Player1, Player2, Move
from figures import get_figure, get_field


class Game():
    def get(self, name_player1, name_player2):
        game = Move()
        player1 = Player1()
        player1.name, cordinates_figures_player1 = name_player1, player1.figures()

        player2 = Player2()
        player2.name, cordinates_figures_player2 = name_player2, player2.figures()

        start_game = game.start(cordinates_figures_player1, cordinates_figures_player2)
        print(start_game)
        value_for_while = 0
        queue = 'player1'
        color = 'white'
        while value_for_while == 0:

            figure = input('figure - ')

            try:
                get_figure(figure)
            except ValueError:
                print('Not exist figure')
            else:
                field = input('start - ')
                try:
                    get_field(field)
                except ValueError:
                    print('Not exist field')
                else:
                    numeric_field = get_field(field)
                    if numeric_field and start_game.at[int(field[1]), field[0]] == figure:
                        step = input('step - ')

                        class_figure = get_figure(figure)(numeric_field)
                        numeric_dest_field = get_field(step)
                        dest_field = class_figure.validate_move(numeric_dest_field, color, start_game)
                        if dest_field:
                            if queue == 'player1':
                                for i in cordinates_figures_player1:
                                    if i[1] == field:
                                        i[1] = step
                                queue = 'player2'
                                color = 'black'
                            elif queue == 'player2':
                                for i in cordinates_figures_player2:
                                    if i[1] == field:
                                        i[1] = step
                                queue = 'player1'
                                color = 'white'
                            start_game = game.start(cordinates_figures_player1, cordinates_figures_player2)
                            print(start_game)
                        else:
                            print('Invalid move')

                    else:
                        print('There is no {} figure on the {} field'.format(figure, field))




a=Game()

print(a.get('bob', 'rob'))