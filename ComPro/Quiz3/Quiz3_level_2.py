import urllib.request
import csv
import codecs
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))
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


def display_score(score_table):
    list_for_sort = []
    d = []
    display_word = ["Club", "MP", "W", "D", "L", "GF", "GA", "GO", "Pts"]
    for x in range(len(score_table)):
        list_for_sort.append([score_table[x][-1], score_table[x][0:8]])
    list_for_sort.sort(reverse=True)
    for y in range(len(list_for_sort)):
        for z in range(len(score_table)):
            if list_for_sort[y][1][0] == score_table[z][0]:
                d.append(score_table[z])
    print(f"{display_word[0]:26}{display_word[1]:5}{display_word[2]:5}{display_word[3]:5}{display_word[4]:5}"
          f"{display_word[5]:5}{display_word[6]:5}{display_word[7]:5}{display_word[8]:5}")
    for z in range(9):
        print(f"{z + 1} {d[z][0]:20}{d[z][1]:5}{d[z][2]:5}{d[z][3]:5}{d[z][4]:5}{d[z][5]:5}{d[z][6]:5}{d[z][7]:5}"
              f"{d[z][8]:5}")
    for k in range(10,20):
        print(f"{k + 1} {d[k][0]:19}{d[k][1]:5}{d[k][2]:5}{d[k][3]:5}{d[k][4]:5}{d[k][5]:5}{d[k][6]:5}{d[k][7]:5}"
              f"{d[k][8]:5}")


display_score(calculate(team_list))
