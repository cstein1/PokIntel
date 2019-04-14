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

def test_wincons(level = 5, maxlev = 5, watching = False):
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

def Trips():
    for _ in range(500):
        for i in range(13):
            h = Hand()
            suits_ = random.sample(suits,3)
            for s in suits_:
                h + Card(s, i)
            ready = False
            other_two = []
            while not ready:
                val_sample = random.randint(0,12)
                if val_sample != i:
                    other_two.append(val_sample)
                    ready =  len(other_two) == 2
            suits2 = random.sample(suits,2)
            for s2, o2 in zip(suits2,other_two):
                h + Card(s2, o2)
            evl = h.evaluateHand()
            assert("Trips" in evl or "FullHouse" in evl)

def TwoPair():
    for _ in range(500):
        for i in range(13):
            h = Hand()
            suits_ = random.sample(suits,2)
            for s in suits_:
                h + Card(s, i)
            suits_ = random.sample(suits,2)
            ready = False
            while not ready:
                other_val = random.randint(0,12)
                ready = other_val != i
            for s in suits_:
                h + Card(s, other_val)
            lonersuit = random.sample(suits,1)[0]
            ready = False
            # Make sure the last card isn't already in the hand
            while not ready:
                lonerCard = Card(lonersuit, random.randint(0,12))
                rov = True
                for card in h:
                    rov &= not (card == lonerCard)
                ready = rov
            h + lonerCard
            evl = h.evaluateHand()
            assert("TwoPair" in evl or "FullHouse")

def Pair():
    for _ in range(500):
        for i in range(13):
            h = Hand()
            suits_ = random.sample(suits,2)
            for s in suits_:
                h + Card(s, i)
            ready = False
            other_three = []
            while not ready:
                val_sample = random.randint(0,12)
                if val_sample != i:
                    other_three.append(val_sample)
                    ready = len(other_three) == 3
            suits3 = random.sample(suits,3)
            for s3, o3 in zip(suits3,other_three):
                h + Card(s3, o3)
            evl = h.evaluateHand()
            assert("Pair" in evl or "FullHouse" in evl)

if __name__ == "__main__":
    test_wincons(level = 7, maxlev = 8, watching = False)
