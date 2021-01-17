# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 00:55:09 2021

@author: jgonz
"""
import random

class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
        
    def show(self):
        print("{} of {}".format(self.value, self.suit))
    
class Deck():
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range (1,14):
                self.cards.append(Card(s,v))
    
    def show(self):
        for c in self.cards:
            c.show()
            
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    def draw(self):
        return self.cards.pop()
        
class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.draw())
        
    def showHand(self):
        for card in self.hand:
            card.show()
        

deck = Deck()
deck.shuffle()


john = Player("John")
john.draw(deck)
john.draw(deck)
john.showHand()