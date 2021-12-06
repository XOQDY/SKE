import random


class MasterMindBoard:
    def __init__(self):
        """Initializing the randomized winning number
        >>> m = MasterMindBoard()
        >>> len(m.solution) == 4
        True
        >>> m.clue
        ''
        >>> m.num_guesses
        0
        """
        str = ''
        for i in range(4):
            str += f"{random.randint(1, 6)}"
        self.solution = str
        self.clue = ''
        self.num_guesses = 0

    def display_clue(self, input_guess):
        """Initializing the randomized winning number
        >>> m = MasterMindBoard()
        >>> m.display_clue(m.solution)
        '****'
        >>> m.display_clue('45')
        row is not complete
        """
        if len(input_guess) != 4:
            print('row is not complete')
        else:
            check = [y for y in self.solution]
            num_pos, num, wrong = 0, 0, 0
            for i in range(len(input_guess)):
                if input_guess[i] == self.solution[i]:
                    check[i] = ''
                    num_pos += 1
            for x in range(len(input_guess)):
                if input_guess[x] in check:
                    num += 1
                    check[check.index(input_guess[x])] = ''
                elif check[x] != '':
                    wrong += 1
            self.clue = f"{'*' * num_pos}{'o' * num}{'_' * wrong}"
            self.num_guesses += 1
            return self.clue

    def done(self):
        """Return True when guess number is correct
        >>> m = MasterMindBoard()
        >>> m.clue = m.display_clue(m.solution)
        >>> m.done()
        True
        >>> m.clue = m.display_clue('45')
        >>> m.done()

        """
        if self.clue == '****':
            return True


if __name__ == '__main__':
    import doctest

    doctest.testmod()
