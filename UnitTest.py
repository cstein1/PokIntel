
from Card import Card


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


runTest = {
    "mkcard": card_inst,
    "metric_card":
}

if __name__ == "__main__":
    runTest["mkcard"]()
