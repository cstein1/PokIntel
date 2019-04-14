
class Card:
    def __init__(self, suit: str, num: int):
        self.num = num
        suits = {"clubs":0, "diamonds":1, "hearts":2, "spades":3}
        if suit not in suits.keys():
            for key in suits.keys():
                if key.startswith(suit):
                    suit = key
                    break;
        if suit not in suits:
            raise Exception("Suit doesn't match any other suits")
        if num < 0 or num > 12:
            raise Exception("Number out of range 1 to 12")
        self.suit = suits[suit]
        self.strsuit = suit

    def __lt__(self, ocard):
        if not isinstance(ocard, Card):
            raise ValueError('please use int for amount')
        if self.suit == ocard.suit:
            return self.num < ocard.num
        else:
            return self.suit < ocard.suit

    def __gt__(self, ocard):
        if not isinstance(ocard, Card):
            raise ValueError('please use int for amount')
        if self.suit == ocard.suit:
            return self.num > ocard.num
        else:
            return self.suit > ocard.suit

    def __eq__(self, ocard):
        if not isinstance(ocard, Card):
            raise ValueError('please use int for amount')
        return self.suit == ocard.suit and self.num == ocard.num

    def __str__(self):
        return "Card({0}, {1})".format(self.strsuit, self.num)

    def __iter__(self):
        for i in self.matr:
            yield i

    @property
    def matr(self):
        a = [0 for i in range(52)]
        #print(self.suit * 13 + self.num)
        print(self.num)
        a[self.suit * 13 + self.num] = 1
        return a
