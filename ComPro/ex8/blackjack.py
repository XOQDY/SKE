from card_deck import *
from player import *


class Blackjack:
    """This class describes the game of Blackjack itself"""
    def __init__(self, num_player):
        deck = CardDeck()
        deck.shuffle()
        self.bj_deck = deck
        self.player = []
        self.computer_hand = []
        self.computer_hand_value = 0       # can have multiple values when hand involves Aces
        self.computer_hand_status = ''     # [stay or dead or can_stay or must_draw_more]
        for x in range(num_player):
            self.player.append(Player())

    def check_value(self, hand):
        value = 0
        for i in range(len(hand)):
            if 'King' in hand[i] or 'Queen' in hand[i] or 'Jack' in hand[i] or '10' in hand[i]:
                value += 10
            elif '9' in hand[i]:
                value += 9
            elif '8' in hand[i]:
                value += 8
            elif '7' in hand[i]:
                value += 7
            elif '6' in hand[i]:
                value += 6
            elif '5' in hand[i]:
                value += 5
            elif '4' in hand[i]:
                value += 4
            elif '3' in hand[i]:
                value += 3
            elif '2' in hand[i]:
                value += 2
            if 'Ace' in hand[i] and value > 10:
                value += 1
            elif 'Ace' in hand[i]:
                value += 11
        return value

    def check_status(self, value):
        if value < 16:
            return 'must draw'
        elif value > 21:
            return 'dead'
        else:
            return 'can stay'

    def start(self):
        """This method starts the game by drawing from the card deck (represented by self.bj_deck)
        two cards for player and two cards for computer; then it proceed to update all
        the values and statuses for both hands"""
        for x in range(2):
            self.computer_hand.append(self.bj_deck.draw_card())
            for i in range(len(self.player)):
                self.player[i].hand.append(self.bj_deck.draw_card())
            if x == 0:
                self.display_computer_hand()
        self.display_player_hand()
        self.player_hand_value = self.check_value(self.player_hand)
        self.computer_hand_value = self.check_value(self.computer_hand)
        self.player_hand_status = self.check_status(self.player_hand_value)
        self.computer_hand_status = self.check_status(self.computer_hand_value)

    def adjust_player_hand(self):
        """This method draws an additional card and reevalute the value and status of the player hand"""
        self.player_hand.append(self.bj_deck.draw_card())
        self.player_hand_value = self.check_value(self.player_hand)
        self.player_hand_status = self.check_status(self.player_hand_value)

    def adjust_computer_hand(self):
        """This method draws an additional card and reevalute the value and status of the computer hand"""
        self.computer_hand.append(self.bj_deck.draw_card())
        self.computer_hand_value = self.check_value(self.computer_hand)
        self.computer_hand_status = self.check_status(self.computer_hand_value)

    def display_player_hand(self):
        """This method reveals the player hand"""
        result_hand = "player hand is "
        for i in self.player_hand:
            i = i.split()
            if i[1] == "Clubs":
                result_hand += f"{i[0]}\u2663 "
            elif i[1] == "Diamonds":
                result_hand += f"{i[0]}\u2666 "
            elif i[1] == "Hearts":
                result_hand += f"{i[0]}\u2660 "
            elif i[1] == "Spades":
                result_hand += f"{i[0]}\u2665 "
        print(result_hand)

    def display_computer_hand(self):
        """This method reveals the computer hand"""
        result_hand = "computer hand is "
        for i in self.computer_hand:
            i = i.split()
            if i[1] == "Clubs":
                result_hand += f"{i[0]}\u2663 "
            elif i[1] == "Diamonds":
                result_hand += f"{i[0]}\u2666 "
            elif i[1] == "Hearts":
                result_hand += f"{i[0]}\u2660 "
            elif i[1] == "Spades":
                result_hand += f"{i[0]}\u2665 "
        print(result_hand)

    def decision(self):
        """This method makes a decision if the player wins, looses, or ties with the computer"""
        if self.player_hand_status == 'dead':
            print("You loose!")
            return True
        elif self.computer_hand_status == 'dead':
            print("You win!")
            return True
        elif self.player_hand_value == 21:
            print("You win!")
            return True
        elif self.computer_hand_value == 21:
            print("You loose!")
            return True
        elif self.player_hand_value > self.computer_hand_value:
            print("You win!")
            return True
        elif self.player_hand_value < self.computer_hand_value:
            print("You loose!")
            return True
        elif self.player_hand_value == self.computer_hand_value:
            print("You tie with the computer!")
            return True
