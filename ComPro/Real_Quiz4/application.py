from routes import *


class Application:
    def __init__(self):
        self.__num_route = 0
        self.__routes_list = []
        # self.__bus_list = []

    def add_route(self, route):
        self.__routes_list.append(Routes(route))

    def add_bus(self, bus):
        # self.__bus_list.append(Busses(bus))
        self.__routes_list[self.__num_route].add_bus_list(Busses(bus))

    def run_stop_bus(self, num_bus, time):
        bus = self.__routes_list[self.__num_route].bus_list[num_bus - 1]
        if bus.run is False:
            bus.run = True
            bus.start_run = time
        else:
            bus.run = False
            bus.all_time += time - bus.start_run

    def update_bus(self, time):
        bus = self.__routes_list[self.__num_route].bus_list
        for x in range(len(bus)):
            if bus[x].run is True:
                bus[x].current_time = time - self.__routes_list[self.__num_route].bus_list[x].start_run
            else:
                bus[x].current_time = 0

    @property
    def num_route(self):
        return self.__num_route

    @num_route.setter
    def num_route(self, value):
        self.__num_route = value

    @property
    def routes_list(self):
        return self.__routes_list

    @routes_list.setter
    def routes_list(self, value):
        self.__routes_list.append(value)

    def __str__(self):
        d = ''
        for x in range(len(self.__routes_list)):
            d += f"Route {x + 1} : {self.__routes_list[x]}\n"
        return d
