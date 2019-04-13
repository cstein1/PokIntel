import numpy as np

class Hand:
    def __init__(self, playername = ""):
        self.cards = []
        self.name = playername

    def draw(self, deck, num_cards = 1):
        self.cards += deck.draw(num_cards)

    def count(self, cnt):
        list_matr_cards = list(map(lambda card: card.matr, self.cards))
        out = 0
        for cardmatr in list_matr_cards:
            out += np.array(cardmatr)#.count(cnt)
        return out

    def fill(self, deck, num_cards=5):
        self.draw(deck, num_cards)

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        ostr = "{0} contains the following cards:\n".format(self.name if self.name else "Hand")
        for card in self.cards:
            ostr += "\t{0}\n".format(str(card))
        return ostr

    def __iter__(self):
        for card in self.cards:
            yield card

    def __len__(self):
        return len(self.cards)

    @property
    def matr(self):
        if not self.cards:
            raise Exception("[Hand.py] No cards in hand.")
        out = []
        for ind, _ in enumerate(self.cards[0]):
            # If any card in your hand has a 1 at location `ind`
            if any(map(lambda card: card.matr[ind], self.cards)):
                out.append(1)
            else:
                out.append(0)
        return out

    #Here's where it gets hard
    def __gt__(self, ohand):
        pass;

    def __lt__(self,ohand):
        pass;
