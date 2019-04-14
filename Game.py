
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
        for x in self.players.keys():
            print(x)
        self.deck = Deck()

    def draw(self):
        for p in self.players:
            self.players[p].fill(self.deck)
            print(self.players[p].count(0))

    def determineWinner(self):
        winningInd = 0
        for ind, p in enumerate(self.players):
            if self.players[p] > self.players["Player{}".format(winningInd+1)]:
                winningInd = ind
        return ind

    def playRound(self):
        self.draw()
        ind = self.determineWinner()
        cards = np.zeros(self.player_num, 52)
        res = np.zeros(self.player_num)
        for ind, p in enumerate(self.players):
            cards[ind] = self.players[p].count()
        res[ind] = 1
        return cards, res




