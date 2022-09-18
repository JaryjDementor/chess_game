from models import Player1, Player2, Move
from figures import get_figure, get_field, letter_to_number1, Watcher, move_player, change_pawn_with_any_figure, make_castling


class Game():
    def get(self, name_player1, name_player2):
        game = Move()
        player1 = Player1()
        player1.name, cordinates_figures_player1 = name_player1, player1.figures()
        taken_figures_player1 = player1.taken_figure

        player2 = Player2()
        player2.name, cordinates_figures_player2 = name_player2, player2.figures()
        taken_figures_player2 = player2.taken_figure
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
            move = move_player(start_game)
            if move and not list_avoiding_checkmate or move in list_avoiding_checkmate:
                class_figure = get_figure(move[0])(move[1])
                dest_field = class_figure.validate_move(move[-1], color, start_game)
                # print(dest_field)
                if dest_field and queue == 'player1':
                    try:
                        float(dest_field)
                        for i in cordinates_figures_player1:
                            if i[1] == move[1]:
                                i[1] = dest_field
                                opponents_figure = start_game[int(dest_field[0])][int(dest_field[-1])]
                                if [opponents_figure, dest_field] in cordinates_figures_player2:
                                    cordinates_figures_player2.remove([opponents_figure, dest_field])
                                    player1.taken_figure.append(opponents_figure)
                    except ValueError:
                        make_castling(color, cordinates_figures_player1, dest_field)

                    change_pawn_with_any_figure(color, player2.taken_figure, cordinates_figures_player1)
                    queue = 'player2'
                    color = 'black'
                    king = 'b_k'
                elif dest_field and queue == 'player2':
                    try:
                        float(dest_field)
                        for i in cordinates_figures_player2:
                            if i[1] == move[1]:
                                i[1] = dest_field
                                opponents_figure = start_game[int(dest_field[0])][int(dest_field[-1])]
                                if [opponents_figure, dest_field] in cordinates_figures_player2:
                                    cordinates_figures_player1.remove([opponents_figure, dest_field])
                                    player2.taken_figure.append(opponents_figure)
                    except ValueError:
                        make_castling(color, cordinates_figures_player2, dest_field)

                    change_pawn_with_any_figure(color, player1.taken_figure, cordinates_figures_player2)
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
                    list_avoiding_checkmate = watcher.avoiding_checkmate([king, kings_field], start_game, move[-1])
                    print('vozmoznye vychody s mata', list_avoiding_checkmate)
                    if list_avoiding_checkmate == []:
                        value_for_while = 1
                    else:
                        list_avoiding_checkmate = []
        return print('Winner {}'.format(queue))


a=Game()

print(a.get('bob', 'rob'))