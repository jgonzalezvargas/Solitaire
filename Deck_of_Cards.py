# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 00:55:09 2021

@author: jgonz
"""
import random

class Card():
    card_value = {1:"A", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8",
                      9:"9", 10:"10", 11:"J", 12:"Q", 13:"K"}
    
    def __init__(self, suit, val):
        self.suit = suit
        self.name = self.card_value[val]
        self.value = val
        
    def show(self):
        print("{} of {}".format(self.value, self.suit))
    
    def isBelow(self, card):
        #Card is the upper card to self
        if self.value == card.value - 1:
            return True
    
    def oppositeColor(self, card):
        if self.suit == "Clubs" or self.suit == "Spades":
            if card.suit == "Diamonds" or card.suit == "Hearts":
                return True
        else:
            if card.suit == "Clubs" or card.suit == "Spades":
                return True
            
    def attachConstraint(self, card):
        if self.isBelow(card) and self.oppositeColor(card):
            return True
    
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