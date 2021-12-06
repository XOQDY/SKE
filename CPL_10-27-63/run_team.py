from team import *


# Problem 8
print('Problem 8')
print()
team_a = Team('team_a.txt', 'A')
print(team_a)
team_b = Team('team_b.txt', 'B')
print(team_b)


# Problem 9
print('Problem 9')
print()
team_a = Team('team_a.txt', 'A')
print(team_a)
team_b = Team('team_b.txt', 'B')
print(team_b)
team_a.select_player()
print(team_a.current_player)
team_b.select_player()
print(team_b.current_player)


# Problem 10
print('Problem 10')
print()


def find_winner(first_player, second_player):
    if first_player.hand == second_player.hand:
        return 0
    elif first_player.hand == "Rock" and second_player.hand == "Scissors"\
            or first_player.hand == "Scissors" and second_player.hand == "Paper"\
            or first_player.hand == "Paper" and second_player.hand == "Rock":
        return 1
    elif second_player.hand == "Rock" and first_player.hand == "Scissors"\
            or second_player.hand == "Scissors" and first_player.hand == "Paper"\
            or second_player.hand == "Paper" and first_player.hand == "Rock":
        return 2


team_a = Team('team_a.txt', 'A')
print(team_a)
team_b = Team('team_b.txt', 'B')
print(team_b)
team_a.select_player()
print(team_a.current_player)
team_b.select_player()
print(team_b.current_player)
winning_team = find_winner(team_a.current_player, team_b.current_player)
print(winning_team)


# Problem 11
print('Problem 11')
print()
team_a = Team('team_a.txt', 'A')
print(team_a)
team_b = Team('team_b.txt', 'B')
print(team_b)
team_a.select_player()
print(team_a.current_player)
team_b.select_player()
print(team_b.current_player)
team_a.update_team_points('win')
print(team_a)
team_b.update_team_points('lose')
print(team_b)

# Problem 12
print('Problem 12')
print()


def update_points(winning_team, first_team, second_team):
    if winning_team == 1:
        print("A wins.")
        first_team.update_team_points('win')
    elif winning_team == 2:
        print("B wins.")
        second_team.update_team_points('win')
    else:
        print("Both team tie")


team_a = Team('team_a.txt', 'A')
print(team_a)
team_b = Team('team_b.txt', 'B')
print(team_b)
team_a.select_player()
print(team_a.current_player)
team_b.select_player()
print(team_b.current_player)
winning_team = find_winner(team_a.current_player, team_b.current_player)
print(winning_team)
update_points(winning_team, team_a, team_b)
print(team_a)
print(team_b)

# Problem 13
print('Problem 13')
print()


def update_points(winning_team, team_a, team_b):
    if winning_team == 1:
        print("A wins.")
        team_a.update_team_points('win')
    elif winning_team == 2:
        print("B wins.")
        team_b.update_team_points('win')
    else:
        print("A and B tie.")


team_a = Team('team_a.txt', 'A')
print(team_a)
team_b = Team('team_b.txt', 'B')
print(team_b)
while True:
    print("")
    team_a.select_player()
    print(team_a.current_player)
    team_b.select_player()
    print(team_b.current_player)
    winning_team = find_winner(team_a.current_player, team_b.current_player)
    update_points(winning_team, team_a, team_b)
    print(team_a)
    print(team_b)
    if team_a.get_team_points() == 5:
        print('Teams A wins!')
        break
    if team_b.get_team_points() == 5:
        print('Teams B wins!')
        break
