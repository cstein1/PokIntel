
from Deck import Deck
from Card import Card
from Hand import Hand

class Game:
    def __init__(self, player_num = 2):
        self.deck = Deck()
        nm = "Player{0}"
        self.players = {nm.format(i): Hand(self.deck,nm.format(i)) for i in range(1,player_num+1)}
