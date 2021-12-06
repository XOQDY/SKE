class Item:
    def __init__(self, id, type, color):
        self.__id = id
        self.__type = type
        self.__color = color

    def __eq__(self, other):
        if self.__id == other.id:
            return True
        else:
            return False

    @property
    def id(self):
        return self.__id

    @property
    def type(self):
        return self.__type

    @property
    def color(self):
        return self.__color

    def __str__(self):
        return '{0},{1},{2}'.format(self.__id, self.__type, self.__color)


