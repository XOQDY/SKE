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
score_table = {}
check_score_table = []
for y in range(len(team_list)):
    if team_list[y]['HomeTeam'] not in check_score_table:
        score_table[team_list[y]['HomeTeam']] = 0, 0, 0, 0
        check_score_table.append(team_list[y]['HomeTeam'])
for y in range(len(team_list)):
    if team_list[y]['AwayTeam'] not in check_score_table:
        score_table[team_list[y]['AwayTeam']] = 0, 0, 0, 0
        check_score_table.append(team_list[y]['AwayTeam'])
print(score_table)