
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

    def id(self):
        # In (reverse_indexed) order of which is best
        # If wincon is true, it will return the highest relevant card,
        # O/w it will return -1 and try the next wincon
        wincons = [
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
        for ind, wincon in enumerate(wincons):
            win_ind = wincon()
            if win_ind >= 0:
                # First element should be largest num
                return (len(wincons)-ind)*51 + highest_relevant_card

    def _RoyalFlush(self):
        # if any of the suits in your hand have 1s for each of the highest 5 cards
        for ind, suit in enumerate(self.h):
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
            for cind, cval in cards:
                clist = []
                if cval == 1:
                    clist.append(cind)
                if len(clist) == 4:
                    return max(clist)
        return -1

    def _FullHouse(self):
        # One pair, One Trip
        pass;

    def _Flush(self):
        # Four of a suit
        for suit in self.h:
            if suit.count(1) == 5:
                return last_occ(self.flat, 1)
        return -1

    def _Straight(self):
        # Five Numerically adjacent cards, suits are irrelevant
        for ind, card in enumerate(self.flat):
            if card:
                # Ace can only be highest (ind%13==12) or lowest (ind%13==8)
                if ind%13 <= 8:
                    itr = range(ind,ind+5)
                elif ind%13==12:
                    itr = range(ind-12,ind-7)
                else:
                    continue;
                straight = True
                for i in itr:
                    straight &= any(
                        list(map(lambda suit: suit[i], self.h))
                        )
                if straight:
                    return last_occ(self.flat, 1)
        return -1

    def _Trips(self):
        # Three of the same number
        for num_list in self.bynum:
            # [(card_ind, card_presence_val)]
            cards = list(map(lambda card_ind: (card_ind, self.flat[card_ind]), num_list))
            for cind, cval in cards:
                clist = []
                if cval == 1:
                    clist.append(cind)
                if len(clist) == 3:
                    return max(clist)
        return -1

    def _TwoPair(self):
        # Two different pairs
        for num_list in self.bynum:
            # [(card_ind, card_presence_val)]
            cards = list(map(lambda card_ind: (card_ind, self.flat[card_ind]), num_list))
            pairs = []
            for cind, cval in cards:
                clist = []
                if cval == 1:
                    clist.append(cind)
                if len(clist) == 2:
                    pairs.extend(clist)
                if len(pairs) == 4:
                    return max(pairs)
        return -1

    def _Pair(self):
        # Three of the same number
        for num_list in self.bynum:
            # [(card_ind, card_presence_val)]
            cards = list(map(lambda card_ind: (card_ind, self.flat[card_ind]), num_list))
            for cind, cval in cards:
                clist = []
                if cval == 1:
                    clist.append(cind)
                if len(clist) == 2:
                    return max(clist)
        return -1

    def _HighCard(self):
        return max(self.flat)
