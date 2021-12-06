from mastermind import *


game = MasterMindBoard()
print('Choose numbers from 1 to 6 (4 digit number)')
print('*** Start ***')
print('____')

while True:
    print(game.solution)
    input_guess = input("What is your guess?: ")
    print('Your guess is', input_guess)
    game.display_clue(input_guess)
    print(game.clue)
    if game.done():
        print()
        print(f'You solve it after {game.num_guesses} rounds.')
        break
