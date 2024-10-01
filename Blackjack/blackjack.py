#Liam BRown
#790886481
#4/23/2022

from player import Player
from deck import Deck
import stdio
import sys

#_______________________________________
#Intructions put python blackjack.py into the command line and enjoy
#_________________________________________


#I could get enverything but the ace value change to work so the ace value is set to 1


#introduction
stdio.writeln("/////////////////////////////////////////////")
stdio.writeln("/          welcome to blackjack             /")
stdio.writeln("/        your dealers name is jean          /")
stdio.writeln("/        Win the game by getting 21         /")
stdio.writeln("/        dont go over 21 or you lose        /")
stdio.writeln("/ win the game by beating the dealers points/")
stdio.writeln('/ lose by getting under the dealers points  /')
stdio.writeln('/////////////////////////////////////////////')
stdio.writeln('Please input your name')
n = stdio.readString()
stdio.writeln("please input the amount chips you wish to start with")
a = stdio.readInt()
d = Deck()
#game function placed in function so it can call its self for another game
def blackjack(n,a, d):
#sets the initial amounts
    if d.deck_length == 'true':
        d = deck()

    p1 = Player(n, a)
    dealer = Player("jean", 10000)
    hit = "y"
    p1.print_balance()
    #asks for bet amount
    stdio.writeln("how much would you like to bet")
    b = stdio.readInt()
    while b > a:
        stdio.writeln("please input something less than or equal to your balance")
        b = stdio.readInt()
    p1.bet(b)
#sets base hands
    p1.deal_card(d)
    p1.deal_card(d)
    p1._print_hand()
    stdio.writeln(p1._add_points())
    p1.print_balance()
    dealer.deal_card(d)
    dealer.deal_card(d)
    dealer._print_hand()
    stdio.writeln(dealer._add_points())
    #game check while loop
    while hit == 'y':
        if d.deck_length == 'true':
            d = deck()

#game code would you like to hit or not
        stdio.writeln("would you like to hit: enter y or n")
        hit = stdio.readString()
        if hit == 'y':
            p1.deal_card(d)
            p1._print_hand()
            stdio.writeln(p1._add_points())
            dealer._print_hand()
            stdio.writeln(dealer._add_points())
        else:
            hit = 'n'
        #ace point value change
        #if p1._add_points <= 10:
        #    pass
        #else:
        #    pass
        #checks true blackjack
        if dealer.true_blackjack() == 'true' and p1.true_blackjack() == 'true':
            hit == 'n'
        elif p1.true_blackjack() == 'true':
            hit == 'n'
        elif dealer.true_blackjack() == 'true':
            hit == 'n'
        #checks if player has blackjack
        if p1._add_points() == 21:
            hit = 'n'
        if p1._add_points() > 21:
            hit = 'n'

            
#dealers code
    hit = 'y'
    dealerpoints = dealer._add_points()
    playerpoints = p1._add_points()
    while hit == 'y' and playerpoints < 21:

        if d.deck_length == 'true':
            d = deck()

        #soft 17
        if dealer.hand_length == 2 and dealerpoints == 17:
            hit = 'n'
        #soft 17
        elif dealer.hand_length == 3 and dealerpoints == 17:
            hit = 'n'
        #is it nessicary to hit for dealer
        elif dealerpoints <= playerpoints and dealerpoints < 21:
            dealer.deal_card(d)
            dealerpoints = dealer._add_points()
            hit = 'y'
        else:
            hit = 'n'
    #prints all ending hands and points
    dealerpoints = dealer._add_points()
    playerpoints = p1._add_points()
    p1._print_hand()
    stdio.writeln(playerpoints)
    dealer._print_hand()
    stdio.writeln(dealerpoints)
            

#checks win if all player are done
    if dealer.true_blackjack() == 'true' and p1.true_blackjack() == 'true':
        stdio.writeln("push")
        p1.win(b)
    elif p1.true_blackjack() == 'true':
        stdio.writeln('BlackJack!')
        p1.win(b*1.5)
    elif dealer.true_blackjack() == 'true':
        stdio.writeln('BlackJack!')
        a -= b
    elif dealerpoints > playerpoints and dealerpoints < 21:
        stdio.writeln("dealer wins!")
        a -= b
    elif playerpoints > dealerpoints and playerpoints < 21:
        stdio.writeln("You win")
        p1.win(b)
    elif dealerpoints > 21:
        stdio.writeln("You win")
        p1.win(b)
    #checks for bust
    elif p1._add_points() > 21:
        stdio.writeln("You lose")
        a -= b
    elif playerpoints == dealerpoints:
        stdio.writeln("push")
    elif p1._add_points() == 21:
        stdio.writeln("Blackjack")
        p1.win(b)
            

    
        
    p1.print_balance()
#next game or done playing
    stdio.writeln("play again: enter y or n")
    again = stdio.readString()
    if again == 'y':
        #recalls function if player wants to go again
        blackjack(n, a,d)
        p1.clear()
    else:
        stdio.writeln("thank you for playing")

blackjack(n,a,d)
    
