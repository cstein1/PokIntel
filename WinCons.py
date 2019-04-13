
from Utils import window

class WinCon:
    def __init__(self, hand1):
        if not isinstance(hand1, list):
            raise Exception("WinCons expects a vector representation")
        # splitting into 4 lists for each suit
        newlist = []
        for i in range(4):
          newlist.append(hand1[:13])
          hand1 = hand1[13:]
        # Hand
        self.h = newlist

    def id(self):
        # In order of which is best
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
        # TODO: next_highest_card =
        for wincon in wincons:
            if wincon:
                return wincon#, highest_card_involved

    def _RoyalFlush(self):
        # if any of the suits in your hand have 1s for each of the highest 5 cards
        flush = False
        for suit in self.h:
            flush |= all(suit[-5:])
        return flush

    def _StraightFlush(self):
        # if any of the suits have 5 consecutive cards
        for suit in self.h:
            # Breaks up suit-vec into chunks of 5 for each possible consecutive card
            slider = window(suit, 5)
            for consec in slider:
                if all(consec):
                    return True
        return False

    def _Quads(self):
        quad = False
        for ind in range(len(self.h[0])):
            for suit in self.h:
                if all(suit[ind]):
                    return True
        return False
