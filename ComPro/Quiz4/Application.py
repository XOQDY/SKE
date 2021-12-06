class Application:
    def __init__(self):
        self.__device = []
        self.__watt = []
        self.__on_off = []

    def add(self, device, watt, on_off):
        self.__device.append(device)
        self.__watt.append(watt)
        self.__on_off.append(on_off)

    def __str__(self):
        d = ''
        for x in range(len(self.__device)):
            d += f"{self.__device[x]} {self.__watt[x]} Watts is {self.__on_off[x]}.\n"
        return d


app = Application()
while True:
    action = input("(a)dd device, (s)how device, (q)uit\n").lower()
    if action == 'a':
        device = input("Device name : ")
        watt = input("Watt : ")
        on_off = input("On or Off? : ")
        app.add(device, watt, on_off)
    elif action == 's':
        print(app)
    elif action == 'q':
        print("bye")
        break
