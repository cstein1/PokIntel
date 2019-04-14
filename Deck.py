
from random import randint
from Card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["s","h","c","d"]:
            for num in range(0,13):
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

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        out_str = ""
        for c in self.cards:
            out_str += str(c)+"\n"
        return out_str

    @property
    def matr(self):
        out = []
        for ind, _ in enumerate(self.cards[0]):
            # If any card in your hand has a 1 at location `ind`
            if any(map(lambda card: card.matr[ind], self.cards)):
                out.append(1)
            else:
                out.append(0)
        return out
