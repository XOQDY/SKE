class Player:
    def __init__(self, name, num_wins, num_plays):  # __ == private (must change in code)
        self.name = name
        self.num_wins = num_wins
        self.num_plays = num_plays
        self.hand = 'None'

    def __str__(self):
        return f'{self.name}: Wins = {self.num_wins}: Plays = {self.num_plays}: Hand = {self.hand}'

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

    # @property
    def get_hand(self):
        return self.hand

    # @hand.setter
    def set_hand(self, value):
        self.hand = value

    def randomize_hand(self):
        import random
        x = random.randint(1, 3)
        if x == 1:
            self.hand = 'Rock'
        elif x == 2:
            self.hand = 'Paper'
        elif x == 3:
            self.hand = 'Scissors'

# a = Player('a',1,2)
# print(a)
