from busses import *


class Routes:
    def __init__(self, route):
        self.__route = route
        self.__bus_list = []

    def add_bus_list(self, bus):
        self.__bus_list.append(bus)

    @property
    def route_list(self):
        return self.__route

    @property
    def bus_list(self):
        return self.__bus_list

    @route_list.setter
    def route_list(self, value):
        self.__route.append(value)

    @bus_list.setter
    def bus_list(self, value):
        self.__bus_list.append(value)

    def __str__(self):
        return self.__route
