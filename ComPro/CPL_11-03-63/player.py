import random


class Player:
    def __init__(self, name):
        self.__name = name
        self.__current_pos = 0
        self.__current_hold = False
        self.__current_move = 0

    def move(self, board):
        if self.__current_move > (int(board.cell_list[-1].id) - self.__current_pos):
            self.__current_pos = int(board.cell_list[-1].id)
            self.__current_move = 0
        else:
            self.__current_pos += self.__current_move
            self.__current_move = 0

    def obtain_cell_status(self, board):
        self.__current_hold = board.access_cell(self.__current_pos).hold
        self.__current_move = int(board.access_cell(self.__current_pos).move)

    def randomize_dice(self):
        self.__current_move = random.randint(1, 6)

    @property
    def name(self):
        return self.__name

    @property
    def current_pos(self):
        return self.__current_pos

    @property
    def current_hold(self):
        return self.__current_hold

    @property
    def current_move(self):
        return self.__current_move

    @current_move.setter
    def current_move(self, value):
        self.__current_move = value

    def __str__(self):
        return "{0}: Pos = {1}: Hold = {2}: Move = {3}".format(self.__name, self.__current_pos, self.__current_hold,
                                                               self.__current_move)
