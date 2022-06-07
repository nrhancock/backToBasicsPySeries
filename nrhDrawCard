import pymel.core as pm
import maya.cmds as cmds
import random


class cardGenerate():
    
    
    def __init__(self):
        
        suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        cardValue = ['Ace','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        
        self.suit = random.choice(suit)
        self.cardValue = random.choice(cardValue)

        
        #Card = [(cardValue, suit) for value in random.range(0) for suit in cardValue]
        
        Card = (self.cardValue + ' of ' + self.suit)
        
        print (Card)

cardGenerate()
