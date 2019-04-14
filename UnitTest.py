
from Card import Card
from Hand import Hand
from Deck import Deck
from Model import BasicModel
from Game import Game
import numpy as np
# {"clubs":0, "diamonds":1, "hearts":2, "spades":3}

suits = ["s","h","d","c"]

def pprint(txt, char ="*", width = 80, buffer = 4):
    print(char*width)
    print((txt.center(len(txt)+buffer, " ")).center(width, char))
    print(char*width)

def card_inst():
    c1 = Card("spades", 0)
    c2 = Card("sp", 13)
    c3 = Card("h", 1)
    try:
        c3 = Card("h", 60)
        assert(False)
    except:
        print("Did not make card")
        assert(True)

def measure_cards():
    c1 = Card("spades", 0)
    c2 = Card("sp", 13)
    c3 = Card("h", 1)
    print (c1>c2)
    print (c1<c2)
    print (c2>c3)

def see_all_cards():
    allcards = [[Card(suit, num) for num in range(1,14)] for suit in suits]
    for pile in allcards:
        for card in pile:
            print(str(card))

def see_matr_version():
    allcards = [[Card(suit, num) for num in range(1,14)] for suit in suits]
    for pile in allcards:
        for card in pile:
            print(card.matr)

def hand_matr():
    for _ in range(100):
        d = Deck()
        h = Hand()
        h.fill(d)
        for i in h:
            print(str(i))
            print(i.matr)
        print("*"*55)
        assert(len(h) == 5)
        assert(h.count(1) == 5)
    print(h.matr)

def test_model():
    m = BasicModel(3, 128, 52)
    m.printModel()
    m.build()
    m.printModel()
    print(m.predict(np.ones(52)))
    print(m.predict(np.random.rand(4,52)))

def test_game():
    g = Game(player_num=2)
    g.draw()

# self._RoyalFlush,
# self._StraightFlush,
# self._Quads,
# self._FullHouse,
# self._Flush,
# self._Straight,
# self._Trips,
# self._TwoPair,
# self._Pair,
# self._HighCard
def test_wincons():
    pprint("Royal Flush")
    RoyalFlush()
    pprint("StraightFlush")
    StraightFlush()

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

def LowestScore():
    h = Hand()
    h + Card("")

def compareHands():
    h = Hand()
    for i in range(8,13):
        h + Card('d', i)
    h2 = Hand()
    for i in range(7,12):
        h2 + Card('d', i)
    print(str(h))
    print(str(h.evaluateHand()))
    print(str(h2))
    print(str(h2.evaluateHand()))
    assert(h>h2)
    pprint("h>h2")

runTest = {
    "mkcard": card_inst,
    "metric_card":measure_cards,
    "see cards": see_all_cards,
    "see cards matr": see_matr_version,
    "hand matr": hand_matr,
    "model test": test_model,
    "game test": test_game,
    "wincon test": test_wincons,
    "compare hands": compareHands
}

if __name__ == "__main__":
    runTest["wincon test"]()
