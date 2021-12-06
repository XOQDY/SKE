class Cell:
    def __init__(self, id, move, hold):
        self.__id = id
        self.__move = move
        self.__hold = hold
        self.__occupy_list = []

    def get_occupy_list_str(self):
        occupy_str = ''
        for x in self.__occupy_list:
            occupy_str += f'{x.name},'
        return occupy_str

    def add_occupy_list(self, player):
        self.__occupy_list.append(player)

    def remove_occupy_list(self, player):
        self.__occupy_list.remove(player)

    @property
    def occupy_list(self):
        return self.__occupy_list

    @property
    def id(self):
        return self.__id

    @property
    def hold(self):
        return self.__hold

    @property
    def move(self):
        return self.__move

    def __str__(self):
        return "{0},{1},{2}".format(self.__id, self.__move, self.__hold)

