import random

# Variable <suits>, list type, containing unicodes for card symbols
suits = ['\u2660', '\u2661', '\u2662', '\u2663'] # Spades; Hearts; Diamonds; Clubs

# Variable <values>, dictionary type, comprising the name and the value of the card
values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, 
           "8":8, "9":9, "10": 10, "Ace":11, "Jack":10, "Queen":10, "King":10} 

## Class <Card> 
class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit 
    
    def __repr__(self):
        return self.value + " of " + self.suit


## Class <Deck>
class Deck:

    def __init__(self):
        self.deck = [] #empty list
        for t in suits:
            for v in values:
                self.deck.append(Card(v,t))
    
    #Method for shuffling the deck
    def shuffle_deck(self):
        random.shuffle(self.deck)
        
    
    #Method for dealing a card
    def deal_card(self):
        return self.deck.pop() 
        


## Class <Player>
class Player:
    
    def __init__(self, lname, fname, dofbirth, nationality, chips):
        self.hand = [] # lista in care vor fi adaugate cartile trase de jucator
        self.card_sum = 0 # setam valoarea initiala la 0, urmand sa se adauge valorile cartilor trase
        self.A = 0 # pentru cartea 'As'. Va avea valoarea 0 daca in mana nu se afla un 'As'
        self.lname = lname
        self.fname = fname
        self.dofbirth = dofbirth
        self.nationality = nationality
        self.chips = chips

    # Method for adding cards into player's hand
    def add_card(self, card): 
        self.card = card
        self.hand.append(self.card)
        return self.score()

    # Metoda prin care calculam valoarea cartilor din mana jucatorului
    def score(self): 
        self.card_sum += values[self.card.value]

        if "Ace" in str(self.card):
            self.A += 1

        while self.card_sum > 21 and self.A > 0:
            self.card_sum -= 10
            self.A -= 1
        
        return self.card_sum
    
    # Method for computing the won chips
    def add_chips(self,bet): 
        self.bet = bet
        self.chips += bet
    
    # Method for computing the lost chips
    def subtract_chips(self,bet): 
        self.bet = bet
        self.chips -= bet
