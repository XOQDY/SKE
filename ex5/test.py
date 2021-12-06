import urllib.request
import csv
import codecs
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))
list = []
for i in data_str:
    list.append(i)


def show_matches(h_t_l, a_t_l, h_g_l, a_g_l):
    for x in range(len(h_t_l)):
        print(f"{x + 1}.{h_t_l[x]}({h_g_l[x]}){a_t_l[x]}({a_g_l[x]})")


def show_team(team_list):
    for x in range(len(team_list)):
        print(f"{x + 1}.{team_list[x]}")


def take_action(action, h_t_l, a_t_l, h_g_l, a_g_l, team_list):
    if action == "m":
        show_matches(h_t_l, a_t_l, h_g_l, a_g_l)
    elif action == "t":
        show_team(team_list)


home_team_list = []
away_team_list = []
home_goals_list = []
away_goals_list = []
team_list = []

for x in range(len(list) - 1):
    if list[x + 1][0] not in team_list:
        team_list.append(list[x + 1][0])
    if list[x+1][1] not in team_list:
        team_list.append(list[x+1][1])
team_list.sort()

for x in range(len(list) - 1):
    home_team_list.append(list[x + 1][0])
    away_team_list.append(list[x + 1][1])
    home_goals_list.append(list[x + 1][2])
    away_goals_list.append(list[x + 1][3])

while True:
    action_input = input("(M)atches (T)eams (Q)uit : ")
    action = action_input.lower()
    if action == "m" or action == "t":
        take_action(action, home_team_list, away_team_list, home_goals_list, away_goals_list, team_list)
    elif action == "q":
        print("Bye")
        break
    else:
        print("Incorrect Menu")
