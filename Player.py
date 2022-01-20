from Deck import Deck
class Player:
    def __init__(self):
        self.hand=[]
        #d=Deck().shuffle()
    def addCard(self,card):
        self.hand.append(card)
    def cardCount(self):
        return len(self.hand)
    def pickCard(self):
        for a in range(len(self.hand)):
            if self.hand[a][0:3] == 'Ace':
                return a
        for b in range(len(self.hand)):
            if self.hand[b][0:4] == 'King':
                return b
        for c in range(len(self.hand)):
            if self.hand[c][0:5] == 'Queen':
                return c
        for d in range(len(self.hand)):
            if self.hand[d][0:4] == 'Jack':
                return d
        for e in range(len(self.hand)):
            if self.hand[e][0:2] == '10':
                return e
        return 0
