import urllib.request
import csv
import codecs
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.DictReader(codecs.iterdecode(data_byte, 'utf-8'))
team_list = []
for i in data_str:
    team_list.append(i)
print(team_list)


def calculate(team_list):
    score_table = {}
    check_score_table = []
    for y in range(len(team_list)):
        if team_list[y]['HomeTeam'] not in check_score_table:
            score_table[team_list[y]['HomeTeam']] = [0, 0, 0, 0, 0, 0, 0, 0]
            check_score_table.append(team_list[y]['HomeTeam'])
    for y in range(len(team_list)):
        if team_list[y]['AwayTeam'] not in check_score_table:
            score_table[team_list[y]['AwayTeam']] = [0, 0, 0, 0, 0, 0, 0, 0]
            check_score_table.append(team_list[y]['AwayTeam'])
    for x in range(len(team_list)):
        if team_list[x]['HomeGoals'] > team_list[x]['AwayGoals']:
            for z in score_table.keys():
                if team_list[x]['HomeTeam'] == z:
                    score_table[z][0] += 1
                    score_table[z][1] += 1
                    score_table[z][3] += int(team_list[x]['HomeGoals'])
                    score_table[z][5] += int(team_list[x]['AwayGoals'])
                    score_table[z][7] += 3
                if team_list[x]['AwayTeam'] == z:
                    score_table[z][0] += 1
                    score_table[z][3] += 1
                    score_table[z][4] += int(team_list[x]['AwayGoals'])
                    score_table[z][5] += int(team_list[x]['HomeGoals'])
        elif team_list[x]['HomeGoals'] < team_list[x]['AwayGoals']:
            for z in score_table.keys():
                if team_list[x]['HomeTeam'] == z:
                    score_table[z][0] += 1
                    score_table[z][3] += 1
                    score_table[z][4] += int(team_list[x]['HomeGoals'])
                    score_table[z][5] += int(team_list[x]['AwayGoals'])
                if team_list[x]['AwayTeam'] == z:
                    score_table[z][0] += 1
                    score_table[z][3] += 1
                    score_table[z][4] += int(team_list[x]['AwayGoals'])
                    score_table[z][5] += int(team_list[x]['HomeGoals'])
                    score_table[z][7] += 3
        elif team_list[x]['HomeGoals'] < team_list[x]['AwayGoals']:
            for z in score_table.keys():
                if team_list[x]['HomeTeam'] == z:
                    score_table[z][0] += 1
                    score_table[z][3] += 1
                    score_table[z][4] += int(team_list[x]['HomeGoals'])
                    score_table[z][5] += int(team_list[x]['AwayGoals'])
                    score_table[z][7] += 1
                if team_list[x]['AwayTeam'] == z:
                    score_table[z][0] += 1
                    score_table[z][3] += 1
                    score_table[z][4] += int(team_list[x]['AwayGoals'])
                    score_table[z][5] += int(team_list[x]['HomeGoals'])
                    score_table[z][7] += 1
        for i in score_table.keys():
            score_table[i][7] = score_table[i][5] - score_table[i][6]
    return score_table


def current_score(score_table):
    list_score = []
    word = ["Team Name", "MP", "W", "D", "L"]
    for x in score_table.keys():
        list_score.append(score_table[x][0:5])
    print(f"{word[0]:24}{word[1]:5}{word[2]:5}{word[3]:5}{word[4]:5}")
    for i in score_table.keys():
        print(f"{list_score[i][0]:20}{list_score[i][1]:5}{list_score[i][2]:5}{list_score[i][3]:5}"
              f"{list_score[i][4]:5}")



print(calculate(team_list))
print(current_score(calculate(team_list)))