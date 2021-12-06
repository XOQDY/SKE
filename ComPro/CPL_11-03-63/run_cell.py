from cell import *
from player import *

c1 = Cell(1, 2, True)
print(c1)

a = Player('A')
b = Player('B')
print(a)
print(b)
# Testing get_occupy_list_str and add_occupy_list
print(c1.get_occupy_list_str()) # no player in the occupy_list, so this line prints empty string
c1.add_occupy_list(a)
print(c1.get_occupy_list_str())
c1.add_occupy_list(b)
print(c1.get_occupy_list_str())
# Testing remove_occupy_list
c1.remove_occupy_list(a)
print(c1.get_occupy_list_str())
c1.remove_occupy_list(b)
print(c1.get_occupy_list_str()) # no more player in the occupy_list, so this line prints empty string
