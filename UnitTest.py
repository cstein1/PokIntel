
from Card import Card
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



runTest = {
    "mkcard": card_inst,
    "metric_card":measure_cards,
    "see cards": see_all_cards,
    "see cards matr": see_matr_version
}

if __name__ == "__main__":
    runTest["see cards matr"]()
