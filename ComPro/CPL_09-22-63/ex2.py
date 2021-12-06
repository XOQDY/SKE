def cal_win_rate(win, lose):
    win_rate = win / (win + lose)
    return win_rate


def read_name_team(team):
    name = team[0]
    return name


def read_win_team(team):
    win = int(team[1])
    return win


def read_lose_team(team):
    lose = int(team[2])
    return lose


def read_team_data_list(team, total_team):
    name_list = []
    win_list = []
    lose_list = []
    for x in range(total_team):
        each_team = team[x].split(",")
        name_list.append(read_name_team(each_team))
        win_list.append(read_win_team(each_team))
        lose_list.append(read_lose_team(each_team))
    return name_list, win_list, lose_list


def print_list(name_list, win_rate_list, total_team):
    print(f"Total team(s): {total_team}")
    for x in range(total_team):
        print(f"{name_list[x]}: got win rate {win_rate_list[x]:.5f}")
    print("=" * 10)


def maximum_win_rate(total_team, win_rate_list, max_win_rate, name_list):
    for x in range(total_team):
        if win_rate_list[x] == max_win_rate:
            print(f"{name_list[x]}: got maximum win rate {win_rate_list[x]:.5f}")


def minimum_win_rate(total_team, win_rate_list, min_win_rate, name_list):
    for x in range(total_team):
        if win_rate_list[x] == min_win_rate:
            print(f"{name_list[x]}: got minimum win rate {win_rate_list[x]:.5f}")


def menu_text(action, total_team, win_rate_list, win_rate_list2, max_win_rate, min_win_rate):
    if action == "x":
        maximum_win_rate(total_team, win_rate_list, max_win_rate, name_list)
    elif action == "m":
        minimum_win_rate(total_team, win_rate_list, min_win_rate, name_list)
    elif action == "r":
        win_rate_list.sort()
        print(f"Total team(s): {total_team}")
        for x in range(total_team):
            for i in range(total_team):
                if win_rate_list[x] == win_rate_list2[i]:
                    print(f"{name_list[i]}: got win rate {win_rate_list[i]:.5f}")
    elif action == "o":
        win_rate_list.sort(reverse=True)
        print(f"Total team(s): {total_team}")
        for x in range(total_team):
            for i in range(total_team):
                if win_rate_list[x] == win_rate_list2[i]:
                    print(f"{name_list[i]}: got win rate {win_rate_list[i]:.5f}")
    elif action == "q":
        print("Bye")


file_name = input("Enter a file name: ")

with open(file_name) as x:
    statistics_team_list = []
    for line in x:
        statistics_team_list.append(line[0:-1])

total_team = len(statistics_team_list)
name_list, win_list, lose_list = read_team_data_list(statistics_team_list, total_team)
win_rate_list = []

for x in range(total_team):
    win_rate = cal_win_rate(win_list[x], lose_list[x])
    win_rate_list.append(win_rate)

max_win_rate = max(win_rate_list)
min_win_rate = min(win_rate_list)
action = []
print_list(name_list, win_rate_list, total_team)
maximum_win_rate(total_team, win_rate_list, max_win_rate, name_list)
minimum_win_rate(total_team, win_rate_list, min_win_rate, name_list)
while action != "q":
    action = input("What do you want to know ? (m)in , ma(x), (o)rder max to min, o(r)der min to max, (q)uit : ")
    print("")
    menu_text(action, total_team, win_rate_list, win_rate_list, max_win_rate, min_win_rate)
    print("")
