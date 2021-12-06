from board import *
from player import *
board = Board('board1.txt')
a = Player('A')
b = Player('B')
board.add_player(a)
board.add_player(b)
print('Starting...')
print(board.cell_list[0].get_occupy_list_str())
round = 1
print('>>> Round ' + str(round))
player = a
player.randomize_dice()
print(player.name + '\'s position = ' + str(player.current_pos) + '. ', end='')
print(player.name + ' moves ' + str(player.current_move) + ' steps.')
board.update_board(player)
print(player)
print(board.cell_list[a.current_pos])
print(board.cell_list[a.current_pos].get_occupy_list_str())
print(board.cell_list[0].get_occupy_list_str())
