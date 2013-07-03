import random
from Game import The_Game
from Card import Card
from Tableau import Tableau


class Deck(object):
  def __init__(self,list_of_cards):
    self.list_of_cards=list_of_cards
 
  def get_cards(self):
  	return self.list_of_cards

   
