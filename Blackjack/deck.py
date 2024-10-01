#Liam BRown
#790886481
#4/24/2022
import stdio
import stdarray
from cards import Card
import random

class Deck:
    def __init__(self):
        self._deck = []
        self._new_deck()
        self._shuffle()
        
        
    def _new_deck(self):
        suits = ['Spades', 'Dimonds', 'Hearts', 'Clubs']
        for i in range(len(suits)):
            self._deck.append(Card(suits[i], 'ace', 1))
            self._deck.append(Card(suits[i], '2', 2))
            self._deck.append(Card(suits[i], '3', 3))
            self._deck.append(Card(suits[i], '4', 4))
            self._deck.append(Card(suits[i], '5', 5))
            self._deck.append(Card(suits[i], '6', 6))
            self._deck.append(Card(suits[i], '7', 7))
            self._deck.append(Card(suits[i], '8', 8))
            self._deck.append(Card(suits[i], '9', 9))
            self._deck.append(Card(suits[i], '10', 10))
            self._deck.append(Card(suits[i], 'jack', 10))
            self._deck.append(Card(suits[i], 'queen', 10))
            self._deck.append(Card(suits[i], 'king', 10)) 
            
    def _shuffle(self):
        random.shuffle(self._deck)
    def deck_length():
        if len(self._deck) <= 20:
            return true

    def print_deck(self):
        print(self._deck)
        for c in self._deck:
            stdio.writeln(c)

    def deal(self):
        return self._deck.pop(0)
        
def main():
    s = Deck()
    s.print_deck()
    

if __name__ == '__main__':
    main()
