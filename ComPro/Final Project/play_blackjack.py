from blackjack import *
import random


def cal_computer_win(player):
    computer_win = 0
    for x in range(player):
        if new_BJ.player[x].win_lose == 'loose':
            computer_win += 1
    return computer_win


continuous = ''
player = int(input("How many players to deal? "))
new_BJ = Blackjack(player)
while continuous != 'no':
    new_BJ.start()
    for y in range(player):
        new_BJ.num_player = y
        new_BJ.display_player_hand()
    new_BJ.num_player = 0
    print()
    while new_BJ.num_player != player:
        while True:
            new_BJ.display_player_hand()
            while new_BJ.player[new_BJ.num_player].status == 'must draw':
                new_BJ.adjust_player_hand()
                new_BJ.display_player_hand()
            choice = input("More cards? (yes/no): ").lower()
            if choice == "yes":
                new_BJ.adjust_player_hand()
            if choice == "no":
                print()
                break
        new_BJ.num_player += 1
    new_BJ.num_player = 0
    for z in range(player):
        new_BJ.decision()
        new_BJ.num_player += 1
    first_score = cal_computer_win(player)
    while cal_computer_win(player) < (player / 2):
        for u in range(random.randint(1, 2)):
            new_BJ.adjust_computer_hand()
            new_BJ.display_computer_hand()
            new_BJ.num_player = 0
        break
    print(new_BJ)
    continuous = input('Next round? ').lower()
