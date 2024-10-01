#Liam Brown
#790886481
#2/24/2022

import stdio
import sys
class Card:

    def __init__(self, suit, face, value):
        self._suit = suit
        self._face = face
        self._value = value
        return

    def get_value(self):
        return self._value

    def set_value(self, i):
        self._value = i
        return

    def __str__(self):
        return ('{} of {}'.format(self._face, self._suit))

def main():
    c1 = Card("heart","two",2)
    c2 = Card("Clubs","ace", 1)
    print(c1)
    print(c2)

if __name__ == "__main__":
    main()
        
