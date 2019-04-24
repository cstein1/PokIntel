# Five Card Draw Phases
class FCDPhases:
    def __init__(self, game):
        self.g = game
        self.phase = 0
        if not self.g.players:
            raise Exception("[FiveCardDraw_Phases] Game variable doesn't have player variables")
        if not self.g.deck:
            raise Exception("[FiveCardDraw_Phases] Game variable doesn't have a deck")
        self.active_players = []
        self.phases = [
            self.Buyin,
            self.Draw,
            self.Bet,
            self.Discard,
            self.Bet,
            self.Announce
        ]

    def Buyin(self, amount = 1, autobuyin = True):
        for player in self.g.players.values():
            if player.funds <= amount:
                continue;
            if autobuyin:
                player.funds -= amount
            else:
                # Prompt user
                resp = ""
                while not resp.lower().startswith("y"):
                    resp = input("Buy in? [y/n]")
                    if resp.lower().startswith("n"):
                        continue;
            # Add player to active players
            self.active_players.append(player)
        return True

    def Draw(self):
        for player in self.active_players:
            player.fill(self.g.deck)
        return True

    def Discard(self):

        for player in self.active_players:
            card_indices = player.discard_decision()
            player.toss(card_indices)
            player.draw(self.g.deck, num_cards=5-len(new_hand))
        return True

    def Bet(self):
        # CNS: I'm going to be honest, I don't really know how this works
        ready = False
        while not ready:
            for player in self.active_players:
                if player.funds < player.bet_amount:
                    self.g.pot += player.bet(pot = self.g.pot)
            ready = True

    def Announce(self):
        player_scores = []
        if not self.active_players:
            return None
        for player in self.active_players:
            player_scores.append(player.evaluateHand())
        # index of the highest score
        index_highest_score = player_scores.index(max(player_scores))
        return self.active_players[index_highest_score]
