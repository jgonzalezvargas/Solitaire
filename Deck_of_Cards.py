# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 00:55:09 2021

@author: jgonz
"""

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
    
class Player():
    def __init__(self):
        print("P")
        

deck = Deck()
deck.show()