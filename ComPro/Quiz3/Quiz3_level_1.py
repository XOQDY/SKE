import urllib.request
import csv
import codecs
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.DictReader(codecs.iterdecode(data_byte, 'utf-8'))
team_list = []
for i in data_str:
    team_list.append(i)


def calculate(team_list):
    score_table = []
    check_score_table = []
    for y in range(len(team_list) - 1):
        if team_list[y + 1][0] not in check_score_table:
            score_table.append([team_list[y + 1][0], 0, 0, 0, 0, 0, 0, 0, 0])
            check_score_table.append(team_list[y + 1][0])
    for y in range(len(team_list) - 1):
        if team_list[y + 1][1] not in check_score_table:
            score_table.append([team_list[y + 1][0], 0, 0, 0, 0, 0, 0, 0, 0])
            check_score_table.append(team_list[y + 1][0])
    for x in range(len(team_list) - 1):
        if team_list[x + 1][2] > team_list[x + 1][3]:
            for z in range(len(score_table)):
                if team_list[x + 1][0] == score_table[z][0]:
                    score_table[z][1] += 1
                    score_table[z][2] += 1
                    score_table[z][5] += int(team_list[x + 1][2])
                    score_table[z][6] += int(team_list[x + 1][3])
                    score_table[z][8] += 3
                if team_list[x + 1][1] == score_table[z][0]:
                    score_table[z][1] += 1
                    score_table[z][4] += 1
                    score_table[z][5] += int(team_list[x + 1][3])
                    score_table[z][6] += int(team_list[x + 1][2])
        elif team_list[x + 1][2] < team_list[x + 1][3]:
            for z in range(len(score_table)):
                if team_list[x + 1][0] == score_table[z][0]:
                    score_table[z][1] += 1
                    score_table[z][4] += 1
                    score_table[z][5] += int(team_list[x + 1][2])
                    score_table[z][6] += int(team_list[x + 1][3])
                if team_list[x + 1][1] == score_table[z][0]:
                    score_table[z][1] += 1
                    score_table[z][2] += 1
                    score_table[z][5] += int(team_list[x + 1][3])
                    score_table[z][6] += int(team_list[x + 1][2])
                    score_table[z][8] += 3
        elif team_list[x + 1][2] == team_list[x + 1][3]:
            for z in range(len(score_table)):
                if team_list[x + 1][0] == score_table[z][0]:
                    score_table[z][1] += 1
                    score_table[z][3] += 1
                    score_table[z][5] += int(team_list[x + 1][2])
                    score_table[z][6] += int(team_list[x + 1][3])
                    score_table[z][8] += 1
                if team_list[x + 1][1] == score_table[z][0]:
                    score_table[z][1] += 1
                    score_table[z][3] += 1
                    score_table[z][5] += int(team_list[x + 1][3])
                    score_table[z][6] += int(team_list[x + 1][2])
                    score_table[z][8] += 1
        for i in range(len(score_table)):
            score_table[i][7] = score_table[i][5] - score_table[i][6]
    return score_table


def current_score(score_table):
    list_score = []
    word = ["Team Name", "MP", "W", "D", "L"]
    for x in range(len(score_table)):
        list_score.append(score_table[x][0:5])
    print(f"{word[0]:24}{word[1]:5}{word[2]:5}{word[3]:5}{word[4]:5}")
    for i in range(len(list_score)):
        print(f"{list_score[i][0]:20}{list_score[i][1]:5}{list_score[i][2]:5}{list_score[i][3]:5}"
              f"{list_score[i][4]:5}")


score_table = calculate(team_list)
current_score(score_table)