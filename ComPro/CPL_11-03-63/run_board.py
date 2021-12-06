from board import *
from player import *
import random


a = Player('A')
b = Player('B')
board = Board('board1.txt')
print('Starting. . .')
if random.randint(0, 1) == 0:
    board.add_player(a)
    board.add_player(b)
    first = 'A'
else:
    board.add_player(b)
    board.add_player(a)
    first = 'B'
print(board)
round = 0
while True:
    round += 1
    print(">>> Round " + str(round))
    if first == 'A':
        player = a
        player.randomize_dice()
        print(player.name + '\'s position = ' + str(player.current_pos) + '. ' +
              player.name + ' moves ' + str(player.current_move) + ' steps.')
        board.update_board(player)
        print(board)
        if board.check_winner():
            print(board.get_winner())
            break
        player = b
        player.randomize_dice()
        print(player.name + '\'s position = ' + str(player.current_pos) + '. ' +
              player.name + ' moves ' + str(player.current_move) + ' steps.')
        board.update_board(player)
        print(board)
        if board.check_winner():
            print(board.get_winner())
            break
    elif first == 'B':
        player = b
        player.randomize_dice()
        print(player.name + '\'s position = ' + str(player.current_pos) + '. ' +
              player.name + ' moves ' + str(player.current_move) + ' steps.')
        board.update_board(player)
        print(board)
        if board.check_winner():
            print(board.get_winner())
            break
        player = a
        player.randomize_dice()
        print(player.name + '\'s position = ' + str(player.current_pos) + '. ' +
              player.name + ' moves ' + str(player.current_move) + ' steps.')
        board.update_board(player)
        print(board)
        if board.check_winner():
            print(board.get_winner())
            break
