import stdio
#Liam Brown
#790886481
#4/24/2022

import sys
from deck import Deck


class Player:

    def __init__(self,name, balence):
        self._hand = []
        self._name = name
        self._balence = balence
        self._total = 0
        return
        
    def deal_card(self,d):
        self._hand.append(d.deal())
        return

    def _add_points(self):
        self._total = 0
        for c in self._hand:
            self._total += c.get_value()
        return self._total

    def _print_hand(self):
        stdio.writeln("***********************")
        stdio.writeln(self._name + "'s hand")
        for i in self._hand:
            stdio.writeln(i)
        stdio.writeln("***********************")
        stdio.writeln("")
        return
    def hand_length():
        return len(self._hand)

    def clear(self):
        self._hand = []
        return

    def print_balance(self):
        stdio.writeln("$$$$$$$$$$$$$$$$$$$$$$$$")
        stdio.writeln(self._name + "'s balence is: " + str(self._balence))
        stdio.writeln("$$$$$$$$$$$$$$$$$$$$$$$$")
        stdio.writeln("")
        return
    def get_balence(self):
        return self._balence

    def bet(self, amount):
        if self._balence >= amount:
            self._balence -= amount
            return

    def win(self, amount):
        self._balence += amount
        return

    def true_blackjack(self):
        if len(self._hand) == 2 and self._total == 21:
            return true

    def blackjack(self):
        if self._total == 21:
            return true

def main():
    d = Deck()
    p1 = Player("Liam", 1000)
    p1.deal_card(d)
    p1.print_balance()
    p1._print_hand()

if __name__ == "__main__":
    main()
    
