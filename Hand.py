
class Hand:
    def __init__(self, deck, playername = ""):
        self.cards = deck.draw(5)
        self.name = playername

    def draw(self, deck, num_cards = 1):
        self.cards.append(deck.draw(num_cards))

    def __str__(self):
        ostr = "{0} contains the following cards:\n".format(self.name if self.name else "Hand")
        for card in self.cards:
            ostr += "\t{0}\n".format(str(card))
        return ostr

    def __iter__(self):
        for card in self.cards:
            yield card

#    @property
#    def matr(self):
