import random
from Game import The_Game
from Card import Card
from Deck import The_Deck

class Tableau(object):
  def __init__(self):
    self.isEmpty = False
    self.tableau_stack=[]

  def add_card(the_card):
  	self.tableau_stack.insert(0,the_card)

  def get_length():
  	return len(self.tableau_stack)

  def isnt_empty():
  	if len(self.tableau_stack) > 0:
  		return True
  	else:
  		return False

  def get_card_at(index):
  	return self.tableau_stack[index]







