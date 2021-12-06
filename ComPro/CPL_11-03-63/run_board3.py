from player import *
from board import *
from cell import *


a = Player('A')
b = Player('B')
board = Board('board1.txt')
board.add_player(a)
board.add_player(b)
### For testing function move
print('>>> A moves')
print(a)
# Set player A to move 4 steps
a.current_move = 4
print(a)
a.move(board)
print(a)
print()
print('>>> B moves 1 step and obtains new cell status')
print(b)
# Set player B to move 1 step
b.current_move = 1
print(b)
b.move(board)
print(b)
print('>>> Print B\'s cell 1 status.')
cell = board.access_cell(b.current_pos)
print(cell)
### For testing function obtain_cell_status
print('>>> B obtains current cell 1 status')
b.obtain_cell_status(board)
print(b)
# B is still at cell 1. Function obtain_cell_statusdoes not move B.
# To update move=4 obtained from cell 1, we need tocall function move again.
print('>>> After obtaining cell 1 status and movingB:')
b.move(board)
print(b)
print()
print('>>> A moves 5 steps and obtains new cellstatus')
print(a)
# Set player A to move 5 steps
a.current_move = 5
print(a)
a.move(board)
print(a)
a.obtain_cell_status(board)
print(a)
print('>>> Print current A\'s cell')
cell = board.access_cell(a.current_pos)
print(cell)
### For testing function randomize_dice
print()
print('>>> B randomizes dice, moves, and obtain new cell status')
print(b)
b.randomize_dice() # randomizes dice. Your randomized value may not be 6, like the sample output.
print(b)
b.move(board) # move
print(b)
b.obtain_cell_status(board) # obtain new cell status
print(b)
print('>>> Print current B\'s cell')
cell = board.access_cell(b.current_pos)
print(cell)
print('>>> B moves more than what is inside the board. B will move to the last cell.')
b.current_move = 30
print(b)
b.move(board)
print(b)
winning_cell_id = board.cell_list[-1].id # Fill ? yourself
winning_cell = board.access_cell(winning_cell_id)
print(len(winning_cell.get_occupy_list_str()))
# The result is zero although b is at the winning cell.
# This happens because function move does not add the player t0 occupy_list of the cell. We must explicitly
# update occupy_list after running function move.
print(board.check_winner())
print(board.get_winner())
