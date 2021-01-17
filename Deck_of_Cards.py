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
        print(self.value + " of " + self.suit)
    
class Deck():
    def __init__(self):
        print("D")
    
class Player():
    def __init__(self):
        print("P")
        
    