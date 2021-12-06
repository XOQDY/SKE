class Busses:
    def __init__(self, code):
        self.__code = code
        self.__run = False
        self.__current_time = 0
        self.__all_time = 0
        self.__start_run = 0

    @property
    def code(self):
        return self.__code

    @property
    def run(self):
        return self.__run

    @property
    def current_time(self):
        return self.__current_time

    @property
    def all_time(self):
        return self.__all_time

    @property
    def start_run(self):
        return self.__start_run

    @code.setter
    def code(self, value):
        self.__code = value

    @run.setter
    def run(self, value):
        self.__run = value

    @current_time.setter
    def current_time(self, value):
        self.__current_time = value

    @all_time.setter
    def all_time(self, value):
        self.__all_time = value

    @start_run.setter
    def start_run(self, value):
        self.__run = value

    def __str__(self):
        if self.__run is False:
            return f"{self.__code} is Stop (Current {self.__current_time:.0f} secs / All{self.__all_time:.0f} secs"
