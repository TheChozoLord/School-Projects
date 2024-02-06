# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:12:39 2024

@author: owen.merrill
"""

""" cards.py
    demonstrates functions
    manage a deck of cards db

"""
import random

NUMCARDS = 52
RANKNAME = ("Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King")

SUITNAME = ("clubs", "hearts", "spades", "diamonds")
HANDS = ("deck", "player", "computer")

DECK = 0
PLAYER = 1
COMPUTER = 2

def initCards():
    deck = []
    for i in range(NUMCARDS):
       deck.append(0)
    return deck
    
def assignCard():
    for 5:
        rand.int

def nameCards():

    
def main():
    cardDB = initCards()

    for i in range(5):
        assignCard(cardDB, PLAYER)
        assignCard(cardDB, COMPUTER)

    showDB(cardDB)

    showHand(cardDB, PLAYER)
    showHand(cardDB, COMPUTER)