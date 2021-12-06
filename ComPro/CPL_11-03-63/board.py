from cell import *


class Board:
    def __init__(self, file_name):
        self.__width = 0
        self.__length = 0
        self.__cell_list = self.__read_board(file_name)

    def __read_board(self, file_name):
        d = []
        f = open(file_name, 'r')
        self.__width = int(f.readline())
        self.__length = int(f.readline())
        for y in f:
            x = y.split(',')
            d.append(Cell(x[0], x[1], x[2].strip()))
        return d

    def add_player(self, player):
        self.__cell_list[0].add_occupy_list(player)

    def access_cell(self, id):
        return self.__cell_list[int(id)]

    def check_winner(self):
        if self.access_cell(self.__cell_list[-1].id).get_occupy_list_str() == "":
            return False
        else:
            return True

    def get_winner(self):
        if self.check_winner():
            return f'Game over. {self.__cell_list[-1].get_occupy_list_str()[0]} wins!'
        else:
            return None

    def update_board(self, player):
        if player.current_hold is not True:
            self.access_cell(player.current_pos).remove_occupy_list(player)
            player.move(self)
            player.obtain_cell_status(self)
            if player.current_hold is not True:
                player.move(self)
            self.access_cell(player.current_pos).add_occupy_list(player)

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def cell_list(self):
        return self.__cell_list

    def __str__(self):
        display = []
        for row in range(self.__length):
            display.append("- - - - - - -  " * self.__width)
            display.append("".join([f"|   {i.id:2}   |"
                                    if self.__cell_list.index(i) == (row + 1) *
                                    (len(self.__cell_list[self.__width * row:self.__width * (row + 1)])) - 1
                                    else f"|   {i.id:2}   "
                                    for i in self.__cell_list[self.__width * row:self.__width * (row + 1)]]))
            display.append("".join([f"|  {i.move:2},{i.hold[0]:2} |"
                                    if self.__cell_list.index(i) == (row + 1) *
                                    (len(self.__cell_list[self.__width * row:self.__width * (row + 1)])) - 1
                                    else f"|  {i.move:2},{i.hold[0]:2} "
                                    for i in self.__cell_list[self.__width * row:self.__width * (row + 1)]]))
            display.append("".join([f"|     {i.get_occupy_list_str():2} |"
                                    if self.__cell_list.index(i) == (row + 1) *
                                    (len(self.__cell_list[self.__width * row:self.__width * (row + 1)])) - 1
                                    else f"|    {i.get_occupy_list_str():2}  "
                                    for i in self.__cell_list[self.__width * row:self.__width * (row + 1)]]))

            if row == self.__length - 1:
                display.append(" - - - - - - - " * self.__width)
        return "\n".join(display)
