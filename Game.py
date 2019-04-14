
from Deck import Deck
from Card import Card
from Hand import Hand
import numpy as np

class Game:
    def __init__(self, player_num = 2):
        self.player_num = player_num
        self.resetGame()
        
    def resetGame(self):
        nm = "Player{0}"
        self.players = {nm.format(i): Hand(nm.format(i)) for i in range(1,self.player_num+1)}
        self.deck = Deck()

    def draw(self):
        for p in self.players:
            self.players[p].fill(self.deck)

    def determineWinner(self):
        winningInd = 0
        for ind, p in enumerate(self.players):
            print(self.players[p])
            print(self.players[p].evaluateHand())
            if self.players[p] > self.players["Player{}".format(winningInd+1)]:
                print(p, ind)
                winningInd = ind
        return winningInd

    def playRound(self):
        self.draw()
        winind = self.determineWinner()
        cards = []#np.zeros((self.player_num, 52))
        res = []#np.zeros(self.player_num)
        for ind, p in enumerate(self.players):
            cards.append(self.players[p].getHandVector())
            if ind == winind:
                res.append(1)
            else:
                res.append(0)
        #res[winind] = 1
        return cards, res

    def playRounds(self, numRounds=1):
        cards = []
        res = []
        for x in range(numRounds):
            c, r = self.playRound()
            cards += c
            res += r
        return np.array(cards), np.array(res)



