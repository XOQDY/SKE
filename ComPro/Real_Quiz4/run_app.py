from routes import *
from busses import *
from application import *
import time


def current_time():
    return time.time()


app = Application()
while True:
    action = input("(n)ew Route, (s)how, (c)hoose, (q)uit: ")
    if action == 'n':
        route = input("Enter route name: ")
        app.add_route(route)
        print(app)
    elif action == 'c':
        app.num_route = int(input("Enter a route number: ")) - 1
        while True:
            route_action = input("(a)dd bus, (p)rint, (r)un/stop, (m)ain menu: ")
            if route_action == 'a':
                bus_code = input("Bus Code: ")
                app.add_bus(bus_code)
            elif route_action == 'p':
                app.update_bus(current_time())
                for x in app.routes_list[app.num_route]:
                    print(x)
            elif route_action == 'r':
                num_bus = int(input("Bus Number? : ")) - 1
                app.run_stop_bus(num_bus, current_time())
                app.update_bus(current_time())
                for x in app.routes_list[app.num_route]:
                    print(x)
            elif route_action == 'm':
                break
    elif action == 's':
        print(app)
    elif action == 'q':
        break
