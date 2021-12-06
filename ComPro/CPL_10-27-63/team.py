import random
from player import *


class Team:
    def __init__(self, filename, team_name='No name'):
        self.__player_list = self.__read_team(filename)
        self.__team_name = team_name
        self.__team_points = 0
        self.current_player = 'None'

    def __read_team(self, filename):
        player_list = []
        table = []
        with open(filename) as f:
            for line in f:
                table.append(line.split(','))
        for row in table:
            temp_player = Player(row[0], int(row[1]), int(row[2]))
            player_list.append(temp_player)
        return player_list

    def __str__(self):
        print(f'Team {self.__team_name}')
        print(f'Team Points: {self.__team_points}')
        data = ''
        for x in self.__player_list:
            data += f'{x.get_name()}: Wins = {x.get_num_wins()}: Plays = {x.get_num_plays()}: Hand = {x.get_hand()}\n'
        return data

    def select_player(self):
        self.current_player = self.__player_list[random.randint(0, len(self.__player_list) - 1)]
        self.current_player.randomize_hand()

    def update_team_points(self, value):
        if value == 'win':
            self.__team_points += 1
            self.current_player.set_num_wins(int(self.current_player.get_num_wins()) + 1)
        self.current_player.num_plays = int(self.current_player.num_plays)
        self.current_player.num_plays += 1

    def get_team_points(self):
        return self.__team_points
