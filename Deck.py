
from random import randint
from Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["s","h","c","d"]:
            for num in range(1,14):
                self.cards.append(Card(suit,num))

    def draw(self, num_cards):
        ret_cards = []
        if len(self.cards) < num_cards: raise Exception("Tried to draw from empty deck.")

        for card in range(num_cards):
            ret_cards.append(
                self.cards.pop(
                    randint(0,len(self.cards)-1)
                    )
                )
        return ret_cards

    def __iter__(self):
        for card in self.cards:
            yield card
