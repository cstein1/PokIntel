
from Utils import window, last_occ, filter_ind

class WinCon:
    def __init__(self, hand1):
        if not isinstance(hand1, list):
            raise Exception("WinCons expects a vector representation")
        # splitting into 4 lists for each suit
        self.flat = hand1[:]
        newlist = []
        for i in range(4):
          newlist.append(hand1[:13])
          hand1 = hand1[13:]
        # Hand
        self.h = newlist
        # List of lists of cards with the same numerical value
        self.bynum = [[i*13 + j for i in range(0,4)] for j in range(0,13)]
        self.wincons = [
            self._RoyalFlush,
            self._StraightFlush,
            self._Quads,
            self._FullHouse,
            self._Flush,
            self._Straight,
            self._Trips,
            self._TwoPair,
            self._Pair,
            self._HighCard
        ]

    def handRank(self):
        # In (reverse_indexed) order of which is best
        # If wincon is true, it will return the highest relevant card,
        # O/w it will return -1 and try the next wincon
        for ind, wincon in enumerate(self.wincons):
            print(wincon)
            win_ind = wincon()
            if win_ind >= 0:
                # print("[WC] Returned from Win Check {0}".format(win_ind))
                # print("[WC] Win con found by Win Check index {0}".format(ind))
                # First element should be largest num
                return (len(self.wincons)-ind-1)*52 + win_ind

    def _RoyalFlush(self):
        # if any of the suits in your hand have 1s for each of the highest 5 cards
        for ind, suit in enumerate(self.h):
            #print("AA " + str(suit[-5:]))
            if all(suit[-5:]):
                return last_occ(self.flat, 1)
        return -1

    def _StraightFlush(self):
        # if any of the suits have 5 consecutive cards
        for suit in self.h:
            # Breaks up suit-vec into chunks of 5 for each possible consecutive card
            slider = window(suit, 5)
            for consec in slider:
                if all(consec):
                    return last_occ(self.flat, 1)
        return -1

    def _Quads(self):
        # Four of the same card number
        for num_list in self.bynum:
            # [(card_ind, card_presence_val)]
            cards = list(map(lambda card_ind: (card_ind, self.flat[card_ind]), num_list))
            clist = []
            for cind, cval in cards:
                if cval == 1:
                    clist.append(cind)
                if len(clist) == 4:
                    return max(clist)
        return -1

    def _FullHouse(self):
        # One pair, One Trip
        ignore_ind, trp = self._Trips()
        pp = self._Pair(fullHouse = ignore_ind)
        if trp >= 0 and pp >= 0:
            return max([trp,pp])
        return -1;

    def _Flush(self):
        # Four of a suit
        for suit in self.h:
            if suit.count(1) == 5:
                return last_occ(self.flat, 1)
        return -1

    def _Straight(self):
        # Five Numerically adjacent cards, suits are irrelevant
        count = []
        # bynum holds the index of each card sharing a num value
        for indlst in self.bynum:
            tmpln = len(count)
            # Look through the indices of value=iteration number of bynum
            for ind in indlst:
                # If the index is a 1 in the hand
                if self.flat[ind]:
                    count.append(ind)
                    break;
            # If we have found 5 in a row, return the highest index val found
            if len(count) == 5:
                return max(count)
            # If we didn't find a card consecutive to the previous ones.
            if len(count)<=tmpln:
                count = []
        return -1

    def _Trips(self, fullHouse = False):
        # Three of the same number
        for ind, num_list in enumerate(self.bynum):
            # [(card_ind, card_presence_val)]
            cards = list(map(lambda card_ind: (card_ind, self.flat[card_ind]), num_list))
            clist = []
            for cind, cval in cards:
                if cval == 1:
                    clist.append(cind)
                if fullHouse: # We need the card num to ignore for the second tuple of fullHouse
                    return ind, max(clist)
                if len(clist) == 3:
                    return max(clist)
        return -1

    def _TwoPair(self):
        # Two different pairs
        pairs = []
        for num_list in self.bynum:
            # [(card_ind, card_presence_val)]
            cards = list(map(lambda card_ind: (card_ind, self.flat[card_ind]), num_list))
            clist = []
            for cind, cval in cards:
                if cval == 1:
                    clist.append(cind)
                if len(clist) == 2:
                    pairs.extend(clist)
                if len(pairs) == 4:
                    return max(pairs)
        return -1

    def _Pair(self, fullHouse = -1):
        # Three of the same number
        # If fullHouse is true then we look for a double that isn't whatever fullHouse Passed
        # Specifically, we are removing whatever was a triple
        bnum = self.bynum[:]
        if fullHouse>=0:
            del bnum[fullHouse]
        for num_list in bnum:
            # [(card_ind, card_presence_val)]
            cards = list(map(lambda card_ind: (card_ind, self.flat[card_ind]), num_list))
            clist = []
            for cind, cval in cards:
                if cval == 1:
                    clist.append(cind)
                if len(clist) == 2:
                    return max(clist)
        return -1

    def _HighCard(self):
        return last_occ(self.flat, 1)
