from player import *

ann = Player('Ann', 2, 4)
bob = Player('Bob', 3, 5)
print(ann)
print(bob)
# print(ann.name)
# print(bob.name)

# ann.name = 'Anna'
# print(ann)
# ann.num_wins = 0
# print(ann)

# ann.set_name('Anna')
# print(ann)
# ann.set_num_wins(3)
# print(ann)
# print(ann.get_num_wins())
# print(ann.get_name())
# print(bob.get_name())
#
# ann.num_plays = 5
# print(ann)
# print(ann.num_plays)

# print(ann.hand)
# print(bob.hand)

ann.randomize_hand()
print(ann)
bob.randomize_hand()
print(bob)
