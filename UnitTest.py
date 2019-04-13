
from Card import Card
from Hand import Hand
from Deck import Deck
from Model import BasicModel
from Game import Game
import numpy as np
# {"clubs":0, "diamonds":1, "hearts":2, "spades":3}

def card_inst():
    c1 = Card("spades", 1)
    c2 = Card("sp", 14)
    c3 = Card("h", 1)
    try:c3 = Card("h", 60)
    except: print("Did not make card")

def measure_cards():
    c1 = Card("spades", 1)
    c2 = Card("sp", 14)
    c3 = Card("h", 1)
    print (c1>c2)
    print (c1<c2)
    print (c2>c3)

def see_all_cards():
    allcards = [[Card(suit, num) for num in range(1,14)] for suit in ["s","h","c","d"]]
    for pile in allcards:
        for card in pile:
            print(str(card))

def see_matr_version():
    allcards = [[Card(suit, num) for num in range(1,14)] for suit in ["c","d","h","s"]]
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
    ## todo
    return False

runTest = {
    "mkcard": card_inst,
    "metric_card":measure_cards,
    "see cards": see_all_cards,
    "see cards matr": see_matr_version,
    "hand matr": hand_matr,
    "model test": test_model,
    "game test": test_game,
    "wincon test": test_wincons
}

if __name__ == "__main__":
    runTest["game test"]()
