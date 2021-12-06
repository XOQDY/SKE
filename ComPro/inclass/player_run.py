from player import *

# Problem 1
print('Problem 1')
ann = Player('Ann', 2, 4)
bob = Player('Bob', 3, 5)
print(ann)
print(bob)
print(ann.name)
print(bob.num_wins)


# Problem 2
print()
print('Problem 2')
ann = Player('Ann', 2, 4)
bob = Player('Bob', 3, 5)
print(ann)
print(bob)
ann.name = 'Anna'
print(ann)
ann.num_wins = 0
print(ann)

# Problem 3
print()
print('Problem 3')
ann = Player('Ann', 2, 4)
bob = Player('Bob', 3, 5)
print(ann)
print(bob)
ann.name = 'Anna'
print(ann)
ann.num_wins = 0
print(ann)

# Problem 4
print()
print('Problem 4')
ann = Player('Ann', 2, 4)
bob = Player('Bob', 3, 5)
print(ann)
print(bob)
ann.set_name('Anna')
print(ann)
ann.set_num_wins(3)
print(ann)
print(ann.get_num_wins())
print(ann.get_name())
print(bob.get_name())

# Problem 5
print()
print('Problem 5')
ann = Player('Ann', 2, 4)
bob = Player('Bob', 3, 5)
print(ann)
print(bob)
ann.set_name('Anna')
print(ann)
ann.set_num_wins(3)
print(ann)
print(ann.get_num_wins())
ann.num_plays = 5
print(ann)
print(ann.num_plays)

# Problem 6
print()
print('Problem 6')
ann = Player('Ann', 2, 4)
bob = Player('Bob', 3, 5)
print(ann)
print(bob)
print(ann.hand)
print(bob.hand)

# Problem 7
print()
print('Problem 7')
ann = Player('Ann', 2, 4)
bob = Player('Bob', 3, 5)
print(ann)
print(bob)
ann.randomize_hand()
print(ann)
bob.randomize_hand()
print(bob)
