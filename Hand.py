import numpy as np
from WinCons import WinCon
from Utils import filter_ind, last_occ

class Hand:
    def __init__(self, playername = ""):
        self.cards = []
        self.name = playername

    def draw(self, deck, num_cards = 1):
        self.cards += deck.draw(num_cards)

    def toss(self, card_indices):
        '''Given a list of card.matr indices, remove each from the hand'''
        def smartRaise(e):
            raise Exception("[Hand.py] Removing cards failure. \nCard input {0}\nHand {1}\nHand vector {2}"
                            .format(card_indices, str(self),
                                    list(map(lambda c:  c.matr.index(1), self.cards))))
        olen = len(self.cards)
        tossed = 0
        for cind in card_indices:
            # Returns a list (len 1) of a card that has the same vector representatioin as input
            hand_cind = filter_ind(itr = self.cards,
                                   # The card index is the same as a a card in the hand
                                   cond = lambda card: card.matr.index(1) == cind
                                   )
            # We want only 1 card... If more than 1 card is found then something is wrong
            if len(hand_cind) > 1:
                raise Exception("[Hand.py] Somehow multiple cards of same value in one hand")
            # If we did find a card in hand in common, then go ahead and attempt to delete it
            if hand_cind:
                try: del self.cards[hand_cind[0]]
                except IndexError as e:
                    smartRaise(e)
                tossed += 1
        if len(self.cards) != olen - len(card_indices) or tossed != len(card_indices):
            smartRaise(e)

    def count(self, cnt):
        list_matr_cards = list(map(lambda card: card.matr, self.cards))
        out = 0
        for cardmatr in list_matr_cards:
            out += cardmatr.count(cnt)
        return out

    def getHandVector(self):
        list_matr_cards = list(map(lambda card: card.matr, self.cards))
        out = 0
        for cardmatr in list_matr_cards:
            out += np.array(cardmatr)
        return out

    def fill(self, deck, num_cards=5):
        self.draw(deck, num_cards)

    def __add__(self, card):
        self.cards.append(card)

    def __str__(self):
        ostr = "{0} contains the following cards:\n".format(self.name if self.name else "Hand")
        for ind, card in enumerate(self.cards):
            ostr += "\t{0}".format(str(card))
            if ind < len(self.cards)-1:
                ostr+='\n'
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

    # We call WinCon enough to merit assigning it to a Hand.WC variable
    def __gt__(self, ohand):
        return WinCon(self.matr).handRank() > WinCon(ohand.matr).handRank()
    def __lt__(self,ohand):
        return WinCon(self.matr).handRank() < WinCon(ohand.matr).handRank()
    def evaluateHand(self):
        wc = WinCon(self.matr)
        val = wc.handRank()
        out_str = "This hand is at best a '{0}' valued at {1}"
        for ind, i in enumerate(wc.wincons):
            if val > (len(wc.wincons)-ind-1) * 52:
                out_str = out_str.format(i.__name__[1:], val)
                print(out_str)
                return i.__name__[1:]
        out_str = out_str.format("N/A", val)
        print(out_str)
