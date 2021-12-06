import random


class Player:

    def __init__(self,  name='None', win=0, plays=0):
        self.name = name
        self.num_wins = win
        self.num_plays = plays
        self.hand = "None"

    def __str__(self):
        return "({0}: Wins = {1}: Plays = {2}: Hand = {3})".format(self.name, self.num_wins, self.num_plays, self.hand)

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_num_wins(self):
        return self.num_wins

    def set_num_wins(self, value):
        self.num_wins = value

    # @property
    def get_num_plays(self):
        return self.num_plays

    # @num_plays.setter
    def set_num_plays(self, value):
        self.num_plays = value

    def get_hand(self):
        return self.hand

    def set_hand(self, value):
        self.hand = value

    @property
    def hand(self):
        return self.hand

    @hand.setter
    def hand(self, value):
        self.hand = value

    def randomize_hand(self):
        x = random.randint(1, 3)
        if x == 1:
            self.hand = 'Rock'
        elif x == 2:
            self.hand = 'Paper'
        elif x == 3:
            self.hand = 'Scissors'
