from Card import Card
import random
class Deck:
  def __init__(self):

      self.numbers = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
      self.suit = ["h","c","s","d"]
      self.deck = []

      for i in range(13):
          c = Card("h", self.numbers[i])
          self.deck.append(c.toString())
      for i in range(13):
          c = Card("c", self.numbers[i])
          self.deck.append(c.toString())
      for i in range(13):
          c = Card("s", self.numbers[i])
          self.deck.append(c.toString())
      for i in range(13):
          c = Card("d", self.numbers[i])
          self.deck.append(c.toString())


  def shuffle(self):
      for a in range(300):
          value=random.randint(0,51)
          if a !=value:
              self.deck.insert(value,self.deck[0])
              del self.deck[0]


  def getFromList(self, num):
    return self.deck[num]
