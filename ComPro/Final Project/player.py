class Player:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.status = ''
        self.win_lose = ''
        self.score = 0

    def update_score(self):
        if self.win_lose == 'wins':
            self.score += 1
        else:
            self.score -= 1
