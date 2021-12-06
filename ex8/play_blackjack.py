from blackjack import *

continuous = ''
while continuous != 'no':
    new_BJ = Blackjack()
    new_BJ.start()
    while True:
        while new_BJ.player_hand_status == 'must draw':
            new_BJ.adjust_player_hand()
            new_BJ.display_player_hand()
        choice = input("More cards? (yes/no): ").lower()
        if choice == "yes":
            new_BJ.adjust_player_hand()
            new_BJ.display_player_hand()
        if choice == "no":
            while new_BJ.computer_hand_value < new_BJ.player_hand_value:
                if new_BJ.player_hand_status == 'dead':
                    if new_BJ.computer_hand_status == 'must draw':
                        new_BJ.adjust_computer_hand()
                else:
                    new_BJ.adjust_computer_hand()
            new_BJ.display_computer_hand()
            break
    new_BJ.decision()
    continuous = input('Play a new round: ')


