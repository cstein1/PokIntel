'''
Non-Deterministic tests are the best we've got
RoyalFlush, and StraightFlush are the only deterministic tests
'''

import random
import numpy as np

from Card import Card
from Hand import Hand
from Deck import Deck
from Model import BasicModel
from Game import Game
# {"clubs":0, "diamonds":1, "hearts":2, "spades":3}

suits = ["s","h","d","c"]

def pprint(txt, char ="*", width = 80, buffer = 4):
    print(char*width)
    print((txt.center(len(txt)+buffer, " ")).center(width, char))
    print(char*width)

def test_wincons():
    level = 5
    maxlev = 5
    watching = False
    wincons = [
        'RoyalFlush','StraightFlush','Quads','FullHouse','Flush',
        'Straight','Trips','TwoPair','Pair','HighCard'
    ]
    for ind, wc in enumerate(wincons):
        pprint(wc)
        if level <= ind:
            exec("{0}()".format(wc))
            pprint("{0} Succ".format(wc))
            if watching:input("Hit enter to continue")
        if maxlev == ind: return

def RoyalFlush():
    for suit in suits:
        h = Hand()
        for i in range(8,13):
            h + Card(suit, i)
        print(str(h))
        evl = h.evaluateHand()
        print()
        assert("RoyalFlush" in evl)

def StraightFlush():
    from Utils import window
    # Make every possible straight flush
    for suit in suits:
        for i in window(list(range(0,12)), 5):
            h = Hand()
            for j in range(i[0],i[-1]+1):
                h+Card(suit,j)
            print(str(h))
            evl = h.evaluateHand()
            assert("StraightFlush" in evl)
        print()

def Quads():
    for i in range(0,13):
        h = Hand()
        for suit in suits:
            h + Card(suit, i)
        ready = False
        while not ready:
            val_sample = random.randint(0,12)
            ready = val_sample != i
        h + Card(random.sample(suit,1)[0], val_sample)
        print(str(h))
        evl = h.evaluateHand()
        assert("Quads" in evl)

def FullHouse():
    h = Hand()
    h + Card('s',0)
    h + Card('h',0)
    h + Card('d', 0)
    h + Card('s', 1)
    h + Card('h', 1)
    print(str(h))
    evl = h.evaluateHand()
    assert("FullHouse" in evl)

def Flush():
    for _ in range(1000):
        for suit in suits:
            h = Hand()
            itr = random.sample(list(range(13)), 5)
            for i in itr:
                h + Card(suit, i)
            evl = h.evaluateHand()
            assert("Flush" in evl)
    print("\n\nTested 4000 samples")

def Straight():
    for _ in range(500):
        for i in range(9):
            h = Hand()
            for ind in range(i,i+5):
                h + Card(random.sample(suits,1)[0], ind)
            evl = h.evaluateHand()
            assert("Straight" in evl or "RoyalFlush" in evl)
    print("\n\nTested {} samples".format(500*7))




if __name__ == "__main__":
    test_wincons()
