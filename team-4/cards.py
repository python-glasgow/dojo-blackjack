#!/usr/bin/python
# card.py
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

""" cards look like {'val': 1, 'face': 'ace', 'suit': 'clubs'} """

import random

class Deck():
    """ generate a deck of 52 cards,
        favouring speed of development over elegance        

        count   = number of decks to shuffle
        shuffle = whether to shuffle or not
"""
    def __init__(self, count=1, shuffle = True):
        self.deck = []
        for i in range(count):
            d = self.generate_deck()
            if shuffle:
                random.shuffle(d)
            self.deck += d



    def generate_deck(self):
        deck = []
        
        # construct a list of "faces"
        faces = ['ace']
        for i in range(2, 11):
            faces.append(str(i)) # ick
        faces.append('jack')
        faces.append('queen')
        faces.append('king')

        for suit in ('hearts', 'spades', 'diamonds', 'clubs'):
            for (val, face) in enumerate(faces, 1):
                if (val>10): val = 10
                card = {'val': val, 'face': face, 'suit': suit}
                deck.append(card)
        return deck

if __name__ == '__main__':

    d = Deck(count=2)
    
    print d.deck
    print len(d.deck)
