import numpy as np
from itertools import combinations
from WinCons import WinCon
from Utils import filter_ind, last_occ
from Card import Card

class Hand:
    def __init__(self, playername = ""):
        self.cards = []
        self.name = playername

    def draw(self, deck, num_cards = 1):
        self.cards += deck.draw(num_cards)

    def optimalDiscard(self, deck):
        cardList = deck.draw(5)
        _, best, remove = self.optimizeHand(cardList)
        #get true index of each card
        inds = []
        bigInd = []
        removeInds = []
        for c in self.cards:
            bigInd.append(np.argmax(c.matr))
        for r in remove:
            removeInds.append(np.argmax(r.matr))
        for b in bigInd:
            inds.append(sum(i < b for i in bigInd))
        res = np.zeros(5)
        for x in range(5):
            if bigInd[x] in removeInds:
                res[inds[x]] = 1
        return res


    def optimizeHand(self, hypotheticals, verbose = False):
        '''
        hypotheticals is a list of cards
        given a list of cards, we want to see which cards would be best to discard
        '''
        cards = self.cards[:]
        cards.extend(hypotheticals)
        combos = combinations(cards, 5)
        highest_combo = 0, []
        for combo in combos:
            h = Hand()
            for card in combo:
                h + card
            score = h.evaluateHand(string_out = False, verbose = verbose)
            if score > highest_combo[0]:
                highest_combo = score, combo
        discarded = []
        for card in self.cards:
            if card not in highest_combo[1]:
                discarded.append(card)
        # High Score, List of cards in high score, List of discarded cards
        return highest_combo[0], highest_combo[1], discarded

    def toss(self, card_indices):
        '''Given a list of card.matr indices, remove each from the hand'''
        def smartRaise():
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
                except IndexError:
                    smartRaise()
                tossed += 1
        if len(self.cards) != olen - len(card_indices) or tossed != len(card_indices):
            smartRaise()

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

    def __contains__(self, inp):
        if isinstance(inp, Card):
            return inp in self.cards
        raise Exception("[Hand.py] Hand asked if holding a non-card object.")

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
    def evaluateHand(self, string_out = True, verbose = True):
        wc = WinCon(self.matr)
        val = wc.handRank()
        out_str = "This hand is at best a '{0}' valued at {1}"
        for ind, i in enumerate(wc.wincons):
            if val > (len(wc.wincons)-ind-1) * 52:
                out_str = out_str.format(i.__name__[1:], val)
                if verbose: print(out_str)
                if string_out: return i.__name__[1:]
                return val
        out_str = out_str.format("N/A", val)
        if verbose: print(out_str)
        if string_out: return out_str
        return val
