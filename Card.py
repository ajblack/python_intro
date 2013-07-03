import random
from Game import The_Game
from Tableau import Tableau
from Deck import The_Deck

class Card(object):
 def __init__(self,suit,rank,id):
  self.suit=suit
  self.rank=rank
  self.id=id

 def get_card_info(self):
  if self.rank > 1 and self.rank < 11:
    print self.rank, "of ",self.suit
  elif self.rank == 1:
    print "ace of ",self.suit
  elif self.rank == 11:
    print "jack of ", self.suit
  elif self.rank == 12:
    print "queen of ", self.suit
  elif self.rank == 13:
    print "king of ",self.suit


