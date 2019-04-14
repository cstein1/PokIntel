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
    print(g.determineWinner())
    g.resetGame()
    print("NEW GAME")
    print(g.playRound())

def test_rounds():
    g = Game(player_num=2)
    c, r = g.playRounds(2)
    print(c)
    print(r)

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

def discardCards():
    h = Hand()
    for s in suits:
        for i in range(13):
            h + Card(s,i)
    print(str(h))
    h.toss([i for i in range(52)])
    print(str(h))

    h = Hand()
    h + Card('c', 0)
    h + Card('d', 1)
    h + Card('s', 12)
    h + Card('s', 10)
    print(str(h))
    h.toss([0,14])
    print(str(h))
    h.toss([3,5])
    print(str(h))

def deckCheck():
    d = Deck()
    print(str(d))
    print(d.matr)

def handHold():
    h = Hand()
    c = Card('c', 0)
    h + Card('c', 0)
    assert(c in h)
    print(c in h)

def card_in_list():
    a = [Card('c',0), Card('h', 5)]
    assert(Card('c',0) in a)
    print(Card('c',0) in a)

def optimizeHand():
    h = Hand()
    h + Card('s', 8)
    h + Card('s', 9)
    h + Card('s', 10)
    h + Card('s', 11)
    h + Card('h', 8)
    highest_score, cards_post_toss, card_tossed = h.optimizeHand(
        [Card('h',4), Card('h',5), Card('h',6), Card('h',7), Card('s',12)]
        )
    print("High score is " + str(highest_score))
    print("Tossed card is " + str(card_tossed[0]))
    for card in cards_post_toss:
        print(str(card))


runTest = {
    "mkcard": card_inst,
    "metric_card":measure_cards,
    "see cards": see_all_cards,
    "see cards matr": see_matr_version,
    "hand matr": hand_matr,
    "model test": test_model,
    "game test": test_game,
    "rounds test": test_rounds,
    "compare hands": compareHands,
    "discard test": discardCards,
    "deck check": deckCheck,
    "hand hold": handHold,
    "card in list check": card_in_list,
    "optimizeHand": optimizeHand
}

if __name__ == "__main__":
    runTest["optimizeHand"]()
    #runTest["wincon test"]()


#suits = ["s","h","d","c"]
