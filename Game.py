
from Deck import Deck
from Card import Card
from Hand import Hand
from Model import DiscardModel
import numpy as np
from tqdm import tqdm
from FiveCardDraw_Phases import FCDPhases

class Game:
    def __init__(self, player_num = 2):
        self.player_num = player_num
        self.pot = 0
        self.resetGame()

    def resetGame(self):
        nm = "Player{0}"
        self.players = {nm.format(i): Hand(nm.format(i)) for i in range(1,self.player_num+1)}
        self.deck = Deck()

    def draw(self):
        for p in self.players:
            self.players[p].fill(self.deck)

    def playPhases(self):
        fcd = FCDPhases()
        for phase in fcd.phases:
            phase()

    def determineWinner(self):
        winningInd = 0
        for ind, p in enumerate(self.players):
            if self.players[p] > self.players["Player{}".format(winningInd+1)]:
                winningInd = ind
        return winningInd

    def playRound(self):
        '''Draws a hand then determines winner.
        Use this when not using the "buyin" effect'''
        self.draw()
        winind = self.determineWinner()
        cards = []
        res = []
        for ind, p in enumerate(self.players):
            cards.append(self.players[p].getHandVector())
            if ind == winind:
                res.append(1)
            else:
                res.append(0)
        return cards, res

    def playRounds(self, numRounds=1):
        cards = []
        res = []
        for x in tqdm(range(numRounds)):
            c, r = self.playRound()
            cards += c
            res += r
            self.resetGame()
        return np.array(cards), np.array(res)

    def playDiscards(self, numRounds=1):
        cards = []
        res = []
        for x in tqdm(range(numRounds)):
            h = Hand()
            d = Deck()
            h.fill(d)
            cards.append(h.getHandVector())
            res.append(h.optimalDiscard(d))
        return np.array(cards), np.array(res)

    def playRoughDiscards(self, numRounds=1):
        cards = []
        res = []
       # x = 0
        for x in tqdm(range(numRounds)):
            h = Hand()
            d = Deck()
            h.fill(d)
            c = h.getHandVector()
            r, better = h.roughDiscard(d)
            if better:
                cards.append(c)
                res.append(r)
                #x += 1
            # if x%1000 == 0:
            #     print(x)
        print(np.array(cards).shape, np.array(res).shape)
        return np.array(cards), np.array(res)

    def playDiscardAgainstRandom(self, discardModel, numRounds=1):
        dm = discardModel
        oneWins = 0.
        for x in tqdm(range(numRounds)):
            d = Deck()
            h1 = Hand()
            h2 = Hand()

            h1.fill(d)
            h2.fill(d)

            h1Discard = dm.predict(h1.getHandVector())
            h2Discard = np.random.randint(2, size=(5))

            h1Ind = np.where(h1.getHandVector()==1)[0]
            h2Ind = np.where(h2.getHandVector()==1)[0]

            h1ls = []
            h2ls = []
            for y in range(5):
                if h1Discard[y] == 1:
                    h1ls.append(h1Ind[y])
                if h2Discard[y] == 1:
                    h2ls.append(h2Ind[y])

            h1.toss(h1ls)
            h2.toss(h2ls)

            h1.draw(d, 5-len(h1))
            h2.draw(d, 5-len(h2))

            if h1 > h2:
                oneWins += 1.
        print(oneWins/numRounds)
